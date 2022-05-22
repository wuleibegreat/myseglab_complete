from functools import partial

import torch

TORCH_VERSION = torch.__version__

def is_rocm_pytorch() -> bool:
    is_rocm = False
    try:
        from torch.utils.cpp_extension import ROCM_HOME
        is_rocm = True if ((torch.version.hip is not None) and
                           (ROCM_HOME is not None)) else False
    except ImportError:
        pass
    return is_rocm

def _get_cuda_home():
    if is_rocm_pytorch():
        from torch.utils.cpp_extension import ROCM_HOME
        CUDA_HOME = ROCM_HOME
    else:
        from torch.utils.cpp_extension import CUDA_HOME
    return CUDA_HOME

def get_build_config():
    return torch.__config__.show()

def _get_conv():
    from torch.nn.modules.conv import _ConvNd, _ConvTransposeMixin
    return _ConvNd, _ConvTransposeMixin


def _get_dataloader():
    if TORCH_VERSION == 'parrots':
        from torch.utils.data import DataLoader, PoolDataLoader
    else:
        from torch.utils.data import DataLoader
        PoolDataLoader = DataLoader
    return DataLoader, PoolDataLoader


def _get_extension():
    from torch.utils.cpp_extension import (BuildExtension, CppExtension,
                                               CUDAExtension)
    return BuildExtension, CppExtension, CUDAExtension


def _get_pool():
    from torch.nn.modules.pooling import (_AdaptiveAvgPoolNd,
                                              _AdaptiveMaxPoolNd, _AvgPoolNd,
                                              _MaxPoolNd)
    return _AdaptiveAvgPoolNd, _AdaptiveMaxPoolNd, _AvgPoolNd, _MaxPoolNd


def _get_norm():
    from torch.nn.modules.instancenorm import _InstanceNorm
    from torch.nn.modules.batchnorm import _BatchNorm
    SyncBatchNorm_ = torch.nn.SyncBatchNorm
    return _BatchNorm, _InstanceNorm, SyncBatchNorm_


_ConvNd, _ConvTransposeMixin = _get_conv()
DataLoader, PoolDataLoader = _get_dataloader()
BuildExtension, CppExtension, CUDAExtension = _get_extension()
_BatchNorm, _InstanceNorm, SyncBatchNorm_ = _get_norm()
_AdaptiveAvgPoolNd, _AdaptiveMaxPoolNd, _AvgPoolNd, _MaxPoolNd = _get_pool()


class SyncBatchNorm(SyncBatchNorm_):

    def _check_input_dim(self, input):
        if TORCH_VERSION == 'parrots':
            if input.dim() < 2:
                raise ValueError(
                    f'expected at least 2D input (got {input.dim()}D input)')
        else:
            super()._check_input_dim(input)