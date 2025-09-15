import pyvista as pv
from pyvista import examples

pl = pv.Plotter()
mesh = examples.planets.load_moon()
texture = examples.planets.download_moon_surface(texture=True)
_ = pl.add_mesh(mesh, texture=texture)
pl.show()