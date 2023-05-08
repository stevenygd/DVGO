_base_ = '../default.py'

expname = 'dvgo_pwl_lego'
basedir = './logs/nerf_synthetic'

data = dict(
    datadir='./data/nerf_synthetic/lego',
    dataset_type='blender',
    white_bkgd=True,
)

# No Coarse training
coarse_train = {
    "N_iters": 0, 
    # "ray_sampler": "random"
    "disable_cache": True
}
model_class="dvgo_pwl"

fine_train = {
    "disable_cache": True,
    "pg_scale": [], # no scaling
}
