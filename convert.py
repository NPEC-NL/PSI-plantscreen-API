
str = """
            calibration_id=obj.get("CalibrationID"),
            calibration_light_id=obj.get("CalibrationLightID"),
            calibration_light_level=obj.get("CalibrationLightLevel"),
            light_caption=obj.get("LightCaption"),
            light_id=obj.get("LightID"),
            light_set_id=obj.get("LightSetID")
"""

new_lines = ""
for line in str.split('\n'):
    if line == '':
        continue
    line = line.strip()
    var = line.split('=')[0]
    json = line.split("\"")[1]
    new = f"self.assertEqual(exp_class.{var}, exp_dict['{json}'])\n"
    new_lines = new_lines + new
print(new_lines)