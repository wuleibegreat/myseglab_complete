_base_ = [
    './_base_/default_runtime.py',
    './_base_/datasets/chase_db1.py'
]

data_root = 'data/222222'
data = dict(
    samples_per_gpu=4,
    workers_per_gpu=4,
    train=dict(
        type='RepeatDataset',
        times=40000,
        dataset=dict(
            data_root=data_root,)),
    val=dict(
        data_root=data_root,),
    test=dict(
        data_root=data_root,))