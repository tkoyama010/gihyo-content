import pyvista as pv
freq = (1, 1, 1)
noise = pv.perlin_noise(1, freq, (0, 0, 0))
grid = pv.sample_function(noise, [0, 3.0, -0, 1.0, 0, 1.0], dim=(120, 40, 40))
out = grid.threshold(0.02)
mn, mx = [out['scalars'].min(), out['scalars'].max()]
clim = (mn, mx * 1.8)

out.plot(
    cmap='gist_earth_r',
    background='white',
    show_scalar_bar=False,
    lighting=True,
    clim=clim,
    show_edges=False,
)