_base_ = '../default.py'

expname = 'dvgo_lego_render200_to_800'
basedir = './logs/nerf_synthetic'

data = dict(
    datadir='./data/nerf_synthetic/lego_render200_to_800',
    dataset_type='blender',
    white_bkgd=True,
)

