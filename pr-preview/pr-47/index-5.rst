import pyvista as pv
from pyvista import examples
mesh = examples.planets.load_moon()
texture = examples.planets.download_moon_surface(texture=True)
pl = pv.Plotter()
pl.background_color = 'k'
_ = pl.add_mesh(mesh, texture=texture)
pl.show()