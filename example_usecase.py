from os import getenv, makedirs, sep
from dotenv import load_dotenv

import plantscreen
from plantscreen.xml_decoder import parse_xml


if __name__ == "__main__":
    """Ëxample implementation of downloading the last meassurement results of the latest experiment"""
    load_dotenv()
    # Create an instance of the API class
    api = plantscreen.CompleteAPIClient(getenv('URL'))

    # Retreive a list with all experiments
    experiment_list = api.experiment_id()
    experiment_id = experiment_list[-1]

    # List the active devices with their family
    device_list = api.device_active()
    active_device_captions = {}
    for ind, device in enumerate(device_list):
        active_device_captions[device.device_caption.replace(' ', '').lower()] = ind
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
        protocol_class = parse_xml(protocol.protocol_body)
        if protocol_class.measure.prescription.analyse is None:
            print(f"Round {round.round_id} has no analyse section, skipping...")
            continue
        analyse_fields = list(type(protocol_class.measure.prescription.analyse).model_fields.keys())
        for device_caption, index in active_device_captions.items():
            # Use model_fields from the Analyse class, not the instance
            if device_caption in analyse_fields:
                # for the last tray
                tray_id = protocol_class.measure.trays[-1].id

                # Get the filenames of the measurement results, could be from any device
                device = device_list[index]
                data = []
                if device.device_family == 'FluorCam':
                    imaging_reply = api.fc_imaging(device.device_id, round.round_id, tray_id)
                    for imaging in imaging_reply:
                        data.append({'.tar': imaging.tar_path})
                elif device.device_family == 'Hypercam':
                    imaging_reply = api.hc_imaging(device.device_id, round.round_id, tray_id)
                    for imaging in imaging_reply:
                        data.append({'.hdr': imaging.data_header_path,
                                     '.bil': imaging.data_content_path,
                                     'white.hdr': imaging.calibration_white_header_path,
                                     'white.bil': imaging.calibration_white_content_path,
                                     'dark.hdr': imaging.calibration_dark_header_path,
                                     'dark.bil': imaging.calibration_dark_content_path,
                                     })
                elif device.device_family == 'ThermalCam':
                    imaging_reply = api.ir_imaging(device.device_id, round.round_id, tray_id)
                    for imaging in imaging_reply:
                        data.append({'.raw': imaging.image_path})
                elif device.device_family == 'MSC':
                    imaging_reply = api.msc_imaging(device.device_id, round.round_id, tray_id)
                    for imaging in imaging_reply:
                        data.append({'.usraw': imaging.image_path})
                elif device.device_family == 'RgbCam':
                    imaging_reply = api.rgb_imaging(device.device_id, round.round_id, tray_id)
                    for imaging in imaging_reply:
                        data.append({'.png': imaging.image_path})
                elif device.device_family == 'Scan3d':
                    imaging_reply = api.scan3d_imaging(device.device_id, round.round_id, tray_id)
                    for imaging in imaging_reply:
                        data.append({'.pcd': imaging.scan3_d_model_path})

                # Download the files
                for record in data:
                    for f_type, filename in record.items():
                        test = api.file_changelog()
                        file_content = api.file(filename)
                        folder_path = f"{experiment_id}{sep}{device.device_family}"
                        makedirs(folder_path, exist_ok=True)
                        with open(f"{folder_path}{sep}round{round.round_id}_tray{tray_id}{f_type}", "wb") as f:
                            f.write(file_content.getbuffer())
