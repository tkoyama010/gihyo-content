from itertools import product
import pyvista as pv
from pyvista import examples

cubemap = examples.download_sky_box_cube_map()
colors = ['red', 'teal', 'black', 'orange', 'silver']

p = pv.Plotter()
p.set_environment_texture(cubemap)

for i, j in product(range(5), range(6)):
    sphere = pv.Sphere(radius=0.5, center=(0.0, 4 - i, j))
    p.add_mesh(sphere, color=colors[i], pbr=True, metallic=i / 4, roughness=j / 5)

p.view_vector((-1, 0, 0), (0, 1, 0))
p.show()