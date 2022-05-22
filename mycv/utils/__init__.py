from .config import Config, DictAction
from .misc import (check_prerequisites, concat_list, deprecated_api_warning,
                   has_method, import_modules_from_strings, is_list_of,
                   is_method_overridden, is_seq_of, is_str, is_tuple_of,
                   iter_cast, list_cast, requires_executable, requires_package,
                   slice_list, to_1tuple, to_2tuple, to_3tuple, to_4tuple,
                   to_ntuple, tuple_cast)
from .path import (check_file_exist, mkdir_or_exist)
from .version_utils import digit_version, get_git_hash


try:
    import torch
except ImportError:
    __all__ = [
        'Config',  'DictAction', 'is_str', 'iter_cast',
        'list_cast', 'tuple_cast', 'is_seq_of', 'is_list_of', 'is_tuple_of',
        'slice_list', 'concat_list', 'check_prerequisites', 'requires_package',
        'requires_executable',  'check_file_exist','mkdir_or_exist', 'deprecated_api_warning',
        'digit_version', 'get_git_hash', 'import_modules_from_strings',
        'to_1tuple', 'to_2tuple', 'to_3tuple', 'to_4tuple', 'to_ntuple',
        'is_method_overridden', 'has_method'
    ]
else:
    from .device_type import IS_IPU_AVAILABLE, IS_MLU_AVAILABLE
    from .logging import get_logger, print_log
    from .env import collect_env
    from .registry import Registry, build_from_cfg
    __all__ = [
        'Config', 'DictAction', 'collect_env', 'get_logger',
        'print_log', 'is_str', 'iter_cast', 'list_cast', 'tuple_cast',
        'is_seq_of', 'is_list_of', 'is_tuple_of', 'slice_list', 'concat_list',
        'check_prerequisites', 'requires_package', 'requires_executable',
        'check_file_exist', 'mkdir_or_exist', 'Registry',
        'build_from_cfg', 'deprecated_api_warning', 'digit_version', 'get_git_hash',
        'import_modules_from_strings', 'is_method_overridden',
        'has_method', 'IS_MLU_AVAILABLE', 'IS_IPU_AVAILABLE'
    ]