_base_ = '../../default.py'

expname = 'dvgo_mic_pwl'
basedir = './logs/nerf_synthetic'

data = dict(
    datadir='./data/nerf_synthetic/mic',
    dataset_type='blender',
    white_bkgd=True,
)

model_class="dvgo_pwl"