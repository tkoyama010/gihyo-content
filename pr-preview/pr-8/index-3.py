import pyvista as pv
from pyvista import examples

mesh = pv.Sphere()
tex = examples.download_masonry_texture()

mesh.texture_map_to_sphere(inplace=True)
mesh.plot(texture=tex)