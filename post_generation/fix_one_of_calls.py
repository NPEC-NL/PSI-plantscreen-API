
import re


def update_probe_api_source():
    filename = "plantscreen/api/probe_api.py"
    with open(filename, "r", encoding="utf-8") as f:
        source_code = f.read()

    # Replaces the import of Probe200Response with JsonProbeByIDResult and JsonProbeResult in probe_api.py.
    pattern = re.compile(r"from plantscreen.models.probe200_response import Probe200Response\n", re.MULTILINE)
    replacement = (
        "from plantscreen.models.json_probe_by_id_result import JsonProbeByIDResult\n"
        "from plantscreen.models.json_probe_result import JsonProbeResult\n"
        "import json"
    )
    source_code, n = pattern.subn(replacement, source_code)
    if n > 0:
        print("Updated imports in probe_api.py")
    else:
        raise Exception("No matching imports found in probe_api.py")

    # Replace all references to Probe200Response with JsonProbeResult | JsonProbeByIDResult
    source_code, n = re.subn(r'\bProbe200Response\b', 'JsonProbeResult | JsonProbeByIDResult', source_code)
    if n > 0:
        print("Updated references to Probe200Response in probe_api.py")
    else:
        raise Exception("No matching references to Probe200Response found in probe_api.py")

    # Replace the response_types_map assignment block with the new logic
    pattern = re.compile(
        r"(^\s*_response_types_map: Dict\[str, Optional\[str\]\] = \{\s*\n\s*'200': \"JsonProbeResult \| JsonProbeByIDResult\",\s*\n\s*\}\s*\n\s*response_data = self\.api_client\.call_api\(\s*\n\s*\*_param,\s*\n\s*_request_timeout=_request_timeout\s*\n\s*\))",
        re.MULTILINE
    )
    replacement = (
        "        _response_types_map: Dict[str, Optional[str]] = {\n"
        "            '200': \"JsonProbeResult | JsonProbeByIDResult\"\n"
        "        }\n"
        "        response_data = self.api_client.call_api(\n"
        "            *_param,\n"
        "            _request_timeout=_request_timeout\n"
        "        )\n"
        "        _response_types_map = self.check_resp_type(response_data)\n"
    )
    source_code, n = pattern.subn(replacement, source_code)
    if n > 0:
        print("Updated response_types_map assignment in probe_api.py")
    else:
        raise Exception("No matching response_types_map assignment found in probe_api.py")

    # Insert the check_resp_type method into the ProbeApi class after the init method
    lines = source_code.splitlines(keepends=True)
    if not re.search(r'def check_resp_type', source_code):
        probe_resp_type_check = [
            '\n',
            '    def check_resp_type(self, response_data: bytearray):\n',
            '        response_json = response_data.data\n',
            '        if response_json is None:\n',
            '            return {\'200\': "JsonProbeResult"}\n',
            '        if isinstance(response_json, bytes):\n',
            '            response_dict = json.loads(response_json.decode())\n',
            '        if isinstance(response_dict, dict):\n',
            '            if "JsonProbeResult" in response_dict.keys():\n',
            '                return {\'200\': "JsonProbeResult"}\n',
            '            elif "JsonProbeByIDResult" in response_dict.keys():\n',
            '                return {\'200\': "JsonProbeByIDResult"}\n',
            '        return {\'200\': "JsonProbeResult | JsonProbeByIDResult"}'
        ]
        method_pattern = re.compile(r"(^\s+def __init__\(.*?\n)([\s\S]*?)(?=^\s+def |^\s*class |^\s*@|\Z)", re.MULTILINE)
        init_match = method_pattern.search(source_code)

        # Insert after __init__ function
        if init_match:
            insert_at = len(source_code[:init_match.end()].splitlines())
            lines = lines[:insert_at] + probe_resp_type_check + lines[insert_at:]
            print("Inserted check_resp_type method in probe_api.py")
        else:
            raise Exception("No __init__ method found in probe_api.py to insert check_resp_type method after.")
    else:
        print("check_resp_type method already exists in probe_api.py, skipping update to avoid overwriting existing method.")

    with open(filename, "w", encoding="utf-8") as f:
        f.write("".join(lines))


def update_msc_api_source():
    filename = "plantscreen/api/msc_api.py"
    with open(filename, "r", encoding="utf-8") as f:
        source_code = f.read()

    # Replaces the import of Probe200Response with JsonProbeByIDResult and JsonProbeResult in probe_api.py.
    pattern = re.compile(r"from plantscreen.models.msc_calibration_light200_response import MscCalibrationLight200Response\n", re.MULTILINE)
    replacement = (
        "from plantscreen.models.json_msc_calibration_light_by_id_result import JsonMscCalibrationLightByIDResult\n"
        "from plantscreen.models.json_msc_calibration_light_result import JsonMscCalibrationLightResult\n"
        "import json"
    )
    source_code, n = pattern.subn(replacement, source_code)
    if n > 0:
        print("Updated imports in msc_api.py")
    else:
        raise Exception("No matching imports found in msc_api.py")

    # Replace all references to MscCalibrationLight200Response with JsonMscCalibrationLightResult | JsonMscCalibrationLightByIDResult
    source_code, n = re.subn(r'\bMscCalibrationLight200Response\b', 'JsonMscCalibrationLightResult | JsonMscCalibrationLightByIDResult', source_code)
    if n > 0:
        print("Updated references to MscCalibrationLight200Response in msc_api.py")
    else:
        raise Exception("No matching references to MscCalibrationLight200Response found in msc_api.py")

    # Replace the check_resp_type method with the new logic to determine the correct response type based on the presence of specific keys in the response JSON.
    pattern = re.compile(
        r"(^\s*_response_types_map: Dict\[str, Optional\[str\]\] = \{\s*\n\s*'200': \"JsonMscCalibrationLightResult \| JsonMscCalibrationLightByIDResult\",\s*\n\s*\}\s*\n\s*response_data = self\.api_client\.call_api\(\s*\n\s*\*_param,\s*\n\s*_request_timeout=_request_timeout\s*\n\s*\))",
        re.MULTILINE
    )
    replacement = (
        "        _response_types_map: Dict[str, Optional[str]] = {\n"
        "            '200': \"JsonMscCalibrationLightResult | JsonMscCalibrationLightByIDResult\"\n"
        "        }\n"
        "        response_data = self.api_client.call_api(\n"
        "            *_param,\n"
        "            _request_timeout=_request_timeout\n"
        "        )\n"
        "        _response_types_map = self.check_resp_type(response_data)\n"
    )
    source_code, n = pattern.subn(replacement, source_code)
    if n > 0:
        print("Updated check_resp_type method in msc_api.py")
    else:
        raise Exception("No matching check_resp_type method found in msc_api.py")

    # Insert the check_resp_type method into the ProbeApi class after the init method
    lines = source_code.splitlines(keepends=True)
    if not re.search(r'def check_resp_type', source_code):
        probe_resp_type_check = [
            '\n',
            '    def check_resp_type(self, response_data: bytearray):\n',
            '        response_json = response_data.data\n',
            '        if response_json is None:\n',
            '            return {\'200\': "JsonMscCalibrationLightResult"}\n',
            '        if isinstance(response_json, bytes):\n',
            '            response_dict = json.loads(response_json.decode())\n',
            '        if isinstance(response_dict, dict):\n',
            '            if "JsonMscCalibrationLightResult" in response_dict.keys():\n',
            '                return {\'200\': "JsonMscCalibrationLightResult"}\n',
            '            elif "JsonMscCalibrationLightByIDResult" in response_dict.keys():\n',
            '                return {\'200\': "JsonMscCalibrationLightByIDResult"}\n',
            '        return {\'200\': "JsonMscCalibrationLightResult | JsonMscCalibrationLightByIDResult"}'
        ]
        method_pattern = re.compile(r"(^\s+def __init__\(.*?\n)([\s\S]*?)(?=^\s+def |^\s*class |^\s*@|\Z)", re.MULTILINE)
        init_match = method_pattern.search(source_code)

        # Insert after __init__ function
        if init_match:
            insert_at = len(source_code[:init_match.end()].splitlines())
            lines = lines[:insert_at] + probe_resp_type_check + lines[insert_at:]
            print("Inserted check_resp_type method in msc_api.py")
        else:
            raise Exception("No __init__ method found in msc_api.py to insert check_resp_type method after.")
    else:
        print("check_resp_type method already exists in msc_api.py, skipping update to avoid overwriting existing method.")

    with open(filename, "w", encoding="utf-8") as f:
        f.write("".join(lines))


def replace_probe_method(source: str) -> str:
    """
    Replaces the probe() method in CompleteAPIClient with the correct oneOf unwrapping logic.
    """
    pattern = re.compile(
        r'(def probe\(self, id: Optional\[int\] = None, _request_timeout: Optional\[Union\[float, Tuple\[float, float\]\]\] = None, _request_auth: Optional\[Dict\[str, Any\]\] = None, _content_type: Optional\[str\] = None, _headers: Optional\[Dict\[str, Any\]\] = None, _host_index: int = 0\) -> JsonProbeResult:\n)'
        r'(\s+)([\s\S]*?)(?:(\s+"""[\s\S]*?"""\n)?)(\s+)result = self\._ProbeApi\.probe\(id, _request_timeout, _request_auth, _content_type, _headers, _host_index\)\n'
        r'\s+return getattr\(result, "oneof_schema_1_validator", None\)',
        re.MULTILINE
    )

    def repl(match):
        funcdef = 'def probe(self, id: int = None, _request_timeout: Optional[Union[float, Tuple[float, float]]] = None, _request_auth: Optional[Dict[str, Any]] = None, _content_type: Optional[str] = None, _headers: Optional[Dict[str, Any]] = None, _host_index: int = 0) -> Probe:\n'
        indent = match.group(2)
        docstring = match.group(4) or ''
        body = (
            f'{indent}result = self._ProbeApi.probe(id, _request_timeout, _request_auth, _content_type, _headers, _host_index)\n'
            f'{indent}value = getattr(result, "json_probe_result", None)\n'
            f'{indent}if value is None:\n'
            f'{indent}    value = getattr(result, "json_probe_by_id_result", None)\n'
            f'{indent}return value'
        )
        return funcdef + (docstring if docstring else '') + body
    source, n = pattern.subn(repl, source)
    if n > 0:
        print("Updated probe method in complete_api_client.py (docstring preserved if present)")
    else:
        raise Exception("No matching probe method found in complete_api_client.py")
    return source


def replace_msc_calibration_light_method(source: str) -> str:
    """
    Replaces the msc_calibration_light() method in CompleteAPIClient with the correct oneOf unwrapping logic.
    """
    pattern = re.compile(
        r'(def msc_calibration_light\(self, id: Optional\[int\] = None, _request_timeout: Optional\[Union\[float, Tuple\[float, float\]\]\] = None, _request_auth: Optional\[Dict\[str, Any\]\] = None, _content_type: Optional\[str\] = None, _headers: Optional\[Dict\[str, Any\]\] = None, _host_index: int = 0\) -> JsonMscCalibrationLightByIDResult:\n)'
        r'(\s+)([\s\S]*?)(?:(\s+"""[\s\S]*?"""\n)?)(\s+)result = self\._MscApi\.msc_calibration_light\(id, _request_timeout, _request_auth, _content_type, _headers, _host_index\)\n'
        r'\s+return getattr\(result, "oneof_schema_1_validator", None\)',
        re.MULTILINE
    )

    def repl(match):
        funcdef = 'def msc_calibration_light(self, id: int = None, _request_timeout: Optional[Union[float, Tuple[float, float]]] = None, _request_auth: Optional[Dict[str, Any]] = None, _content_type: Optional[str] = None, _headers: Optional[Dict[str, Any]] = None, _host_index: int = 0) -> MscCalibrationLight:\n'
        indent = match.group(2)
        docstring = match.group(4) or ''
        body = (
            f'{indent}result = self._MscApi.msc_calibration_light(id, _request_timeout, _request_auth, _content_type, _headers, _host_index)\n'
            f'{indent}value = getattr(result, "json_msc_calibration_light_by_id_result", None)\n'
            f'{indent}if value is None:\n'
            f'{indent}    value = getattr(result, "json_msc_calibration_light_result", None)\n'
            f'{indent}return value'
        )
        return funcdef + (docstring if docstring else '') + body
    source, n = pattern.subn(repl, source)
    if n > 0:
        print("Updated msc_calibration_light method in complete_api_client.py (docstring preserved if present)")
    else:
        raise Exception("No matching msc_calibration_light method found in complete_api_client.py")
    return source


# Update CompleteAPIClient
with open("plantscreen/complete_api_client.py", "r", encoding="utf-8") as f:
    source_code = f.read()
source_code = replace_msc_calibration_light_method(source_code)
source_code = replace_probe_method(source_code)
with open("plantscreen/complete_api_client.py", "w", encoding="utf-8") as f:
    f.write(source_code)

# Update ProbeApi
update_probe_api_source()

# Update MscApi
update_msc_api_source()
