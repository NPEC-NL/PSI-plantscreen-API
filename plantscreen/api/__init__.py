# flake8: noqa

import inspect
from functools import wraps
from typing import get_type_hints, get_origin, Annotated, get_args, Any


def allow_single_for_first_list_param(func):
    def unwrap_annotated(annotation: Any) -> Any:
        if get_origin(annotation) is Annotated:
            return get_args(annotation)[0]
        return annotation

    def first_data_param_accepts_list(func, signature) -> tuple[bool, str]:
        hints = get_type_hints(func, include_extras=True)

        for param in signature.parameters.values():
            if param.name in {"self", "cls"}:
                continue

            annotation = unwrap_annotated(hints[param.name])
            accepts_list = annotation is list or get_origin(annotation) is list
            return accepts_list, param.name

        raise ValueError("Function has no non-self/cls parameters")

    sig = inspect.signature(func)
    accepts_list, target_param_name = first_data_param_accepts_list(func, sig)

    def _normalize_bound_arguments(bound):
        if target_param_name is None or not accepts_list:
            return bound

        if target_param_name in bound.arguments:
            value = bound.arguments[target_param_name]
            # if the passed value is not a list but should be one
            if value is not None and not isinstance(value, list):
                bound.arguments[target_param_name] = [value]

        return bound

    if inspect.iscoroutinefunction(func):
        @wraps(func)
        async def async_wrapper(*args, **kwargs):
            bound = sig.bind_partial(*args, **kwargs)
            bound = _normalize_bound_arguments(bound)
            return await func(*bound.args, **bound.kwargs)

        return async_wrapper

    @wraps(func)
    def sync_wrapper(*args, **kwargs):
        bound = sig.bind_partial(*args, **kwargs)
        bound = _normalize_bound_arguments(bound)
        return func(*bound.args, **bound.kwargs)

    return sync_wrapper


# import apis into api package
from plantscreen.api.action_api import ActionApi
from plantscreen.api.buffer_api import BufferApi
from plantscreen.api.device_api import DeviceApi
from plantscreen.api.experiment_api import ExperimentApi
from plantscreen.api.fc_api import FcApi
from plantscreen.api.file_api import FileApi
from plantscreen.api.hc_api import HcApi
from plantscreen.api.ir_api import IrApi
from plantscreen.api.msc_api import MscApi
from plantscreen.api.plant_api import PlantApi
from plantscreen.api.probe_api import ProbeApi
from plantscreen.api.profile_api import ProfileApi
from plantscreen.api.rgb_api import RgbApi
from plantscreen.api.round_api import RoundApi
from plantscreen.api.scales_api import ScalesApi
from plantscreen.api.scan3d_api import Scan3dApi
from plantscreen.api.spectrum_device_api import SpectrumDeviceApi
from plantscreen.api.spray_api import SprayApi
from plantscreen.api.system_log_api import SystemLogApi
from plantscreen.api.tray_api import TrayApi
from plantscreen.api.version_info_api import VersionInfoApi

