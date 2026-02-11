import re


""" Open API expects to get a data or NONE value for datetime fields
    PSI's API returns an empty string when the value is null.
    This helper functions update the from_dict methods in the models to handle this
    by changing obj.get("FieldName") to obj.get("FieldName") or None for datetime
    fields
"""


def update_fields_with_or_none(file_path, field_names):
    """
    For each field name in field_names, update the assignment in the file so
    that obj.get("FieldName") becomes obj.get("FieldName") or None
    """
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    updated_fields = []
    for field in field_names:
        pattern = rf'("{field}": obj.get\("{field}"\))'
        new_content, n = re.subn(pattern, r'\1 or None', content)
        if n > 0:
            updated_fields.append(field)
            content = new_content
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

    if len(updated_fields) == len(field_names):
        print(f"Updated {', '.join(updated_fields)} in {file_path}")
    else:
        not_found = [f for f in field_names if f not in updated_fields]
        print(
            (
                f"No matching fields found for {', '.join(not_found)} "
                f"in {file_path}."
            )
        )


update_fields_with_or_none(
    'plantscreen/models/action.py',
    ['ActionDateStart', 'ProtocolDateChanged']
)
update_fields_with_or_none(
    'plantscreen/models/device.py',
    ['DeviceValidityStart', 'DeviceValidityEnd']
)
update_fields_with_or_none(
    'plantscreen/models/experiment.py',
    ['StatusChangedDate']
)
update_fields_with_or_none(
    'plantscreen/models/experiment.py',
    ['StatusChangedDate']
)
update_fields_with_or_none(
    'plantscreen/models/experiment_note.py', ['NoteCreatedDate']
)
update_fields_with_or_none('plantscreen/models/fc_imaging.py', ['MeasureDate'])
update_fields_with_or_none('plantscreen/models/imaging.py', ['MeasureDate'])
update_fields_with_or_none(
    'plantscreen/models/msc_calibration.py',
    ['CalibrationDate']
)
update_fields_with_or_none(
    'plantscreen/models/measure_extended_data.py',
    ['MeasureDate']
)
update_fields_with_or_none('plantscreen/models/plant_height.py', ['HeightDate'])
update_fields_with_or_none('plantscreen/models/plant_mask.py', ['MeasureDate'])
update_fields_with_or_none(
    'plantscreen/models/plant_weight_reference.py',
    ['ReferenceWeightDate']
)
update_fields_with_or_none('plantscreen/models/probe_value.py', ['RecordDate'])
update_fields_with_or_none(
    'plantscreen/models/owner.py',
    ['CreateDate', 'LastFailedDate', 'LastSuccessLogin']
)
update_fields_with_or_none(
    'plantscreen/models/round.py',
    ['RoundDateStart', 'RoundDateStop']
)
update_fields_with_or_none(
    'plantscreen/models/rgb_greening_mask_image.py',
    ['MeasureDate']
)
update_fields_with_or_none('plantscreen/models/scales_data.py', ['MeasureDate'])
update_fields_with_or_none(
    'plantscreen/models/scan3_d_analyzed_model.py',
    ['MeasureDate']
)
update_fields_with_or_none(
    'plantscreen/models/scan3_d_imaging.py',
    ['MeasureDate']
)
update_fields_with_or_none(
    'plantscreen/models/spectrum_values.py',
    ['SpectrumRecordDate']
)
update_fields_with_or_none(
    'plantscreen/models/spray_action.py',
    ['SprayActionDate', 'SprayTime']
)
update_fields_with_or_none('plantscreen/models/system_log.py', ['LogDate'])
update_fields_with_or_none('plantscreen/models/tray.py', ['TrayStatusChanged'])
update_fields_with_or_none(
    'plantscreen/models/tray_profile.py',
    ['ProfileDateStart', 'ProfileDateStop']
)
