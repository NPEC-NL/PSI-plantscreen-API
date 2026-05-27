from os import getenv, makedirs, sep

from dotenv import load_dotenv

import plantscreen
from plantscreen.xml_decoder import xml_to_dict


if __name__ == "__main__":
    """Ëxample implementation of downloading the last meassurement results.

    Uses the latest experiment.
    """
    load_dotenv()
    # Create an instance of the API class
    api = plantscreen.CompleteAPIClient(getenv("HOST"))

    # Retreive a list with all experiments
    experiment_list = api.experiment_id()
    experiment_id = experiment_list[-1]

    # List the active devices with their family
    device_list = api.device_active()
    active_device_captions = {}
    for ind, device in enumerate(device_list):
        caption = device.device_caption.replace(" ", "").lower()
        active_device_captions[caption] = ind

    # Get all rounds of the experiment
    round_list = api.round_experiment(experiment_id)

    # For the last 5 rounds of the experiment if available
    if len(round_list) < 5:
        first_shown_round = -len(round_list)
    else:
        first_shown_round = -6
    # Retreive the protocol
    for round in round_list[first_shown_round:-1]:
        # Alternativeway is to download the txt file, utf-16 encoded
        # protocol = api.file(round.round_protocol_path).decode("utf-16")
        protocol = api.action_protocol_round(round.round_id)
        protocol_dict = xml_to_dict(protocol.protocol_body)
        if protocol_dict["Protocol"]["Measure"] is None:
            print(
                f"Round {round.round_id} has no meassurement section, "
                "skipping..."
            )
            continue

        # For all perscriptions in all measurrements
        for protocol, prescription in (
            (protocol, prescription)
            for protocol in protocol_dict["Protocol"]["Measure"]
            for prescription in protocol["Prescription"]
        ):
            # For all active camera systems
            for device_caption, index in active_device_captions.items():
                if (
                    device_caption in prescription.keys()
                    or device_caption.upper() in prescription.keys()
                ):
                    device = device_list[index]
                    if device.device_family == 'Scales':
                        continue

                    # for the last tray
                    # if no batch is defined for the round protocol["Tray"] does not exist and we must fetch the trays
                    # for the round from the API
                    if protocol.get("Tray") is not None:
                        tray_id = int(protocol["Tray"][-1]["id"])
                    else:
                        ray_id = round.trays[-1].tray_id

                    data = []
                    imaging_reply = api.imaging(device, round, tray_id)
                    # Get the filenames of the measurement results.
                    # These could be from any camera device.
                    if device.device_family == "FluorCam":
                        for imaging in imaging_reply:
                            data.append({".tar": imaging.tar_path})
                    elif device.device_family == "Hypercam":
                        for imaging in imaging_reply:
                            data.append(
                                {
                                    ".hdr": imaging.data_header_path,
                                    ".bil": imaging.data_content_path,
                                    "white.hdr": (
                                        imaging.calibration_white_header_path
                                    ),
                                    "white.bil": (
                                        imaging.calibration_white_content_path
                                    ),
                                    "dark.hdr": (
                                        imaging.calibration_dark_header_path
                                    ),
                                    "dark.bil": (
                                        imaging.calibration_dark_content_path
                                    ),
                                }
                            )
                    elif device.device_family == "ThermalCam":
                        for imaging in imaging_reply:
                            data.append({".raw": imaging.image_path})
                    elif device.device_family == "MSC":
                        for imaging in imaging_reply:
                            data.append({".usraw": imaging.image_path})
                    elif device.device_family == "RgbCam":
                        for imaging in imaging_reply:
                            data.append({".png": imaging.image_path})
                    elif device.device_family == "Scan3d":
                        for imaging in imaging_reply:
                            data.append({".pcd": imaging.scan3_d_model_path})

                    # Download the files
                    for record in data:
                        for f_type, filename in record.items():
                            test = api.file_changelog()
                            file_content = api.file(filename)
                            folder_path = (
                                f"{experiment_id}{sep}{device.device_family}"
                            )
                            makedirs(folder_path, exist_ok=True)
                            output_path = (
                                f"{folder_path}{sep}"
                                f"round{round.round_id}_tray{tray_id}{f_type}"
                            )
                            with open(output_path, "wb") as f:
                                f.write(file_content.getbuffer())
