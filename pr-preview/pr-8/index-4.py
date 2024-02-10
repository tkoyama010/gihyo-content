import pyvista as pv
from pyvista import examples

pl = pv.Plotter()
image_path = examples.planets.download_stars_sky_background(
    load=False
)
pl.add_background_image(image_path)
mesh = examples.planets.load_moon()
texture = examples.planets.download_moon_surface(texture=True)
_ = pl.add_mesh(mesh, texture=texture)
pl.show()