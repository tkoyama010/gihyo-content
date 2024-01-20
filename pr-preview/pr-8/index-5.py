import numpy as np

import pyvista
from pyvista import examples

mesh = examples.download_dragon()
mesh.rotate_x(90, inplace=True)
mesh.rotate_z(120, inplace=True)

light1 = pyvista.Light(
    position=(0, 0.2, 1.0),
    focal_point=(0, 0, 0),
    color=[1.0, 1.0, 0.9843, 1.0],  # Color temp. 5400 K
    intensity=0.3,
)

light2 = pyvista.Light(
    position=(0, 1.0, 1.0),
    focal_point=(0, 0, 0),
    color=[1.0, 0.83921, 0.6666, 1.0],  # Color temp. 2850 K
    intensity=1,
)

# Add a thin box below the mesh
bounds = mesh.bounds
rnge = (bounds[1] - bounds[0], bounds[3] - bounds[2], bounds[5] - bounds[4])

expand = 1.0
height = rnge[2] * 0.05
center = np.array(mesh.center)
center -= [0, 0, mesh.center[2] - bounds[4] + height / 2]

width = rnge[0] * (1 + expand)
length = rnge[1] * (1 + expand)
base_mesh = pyvista.Cube(center, width, length, height)

# rotate base and mesh to get a better view
base_mesh.rotate_z(30, inplace=True)
mesh.rotate_z(30, inplace=True)

# create the plotter with custom lighting
pl = pyvista.Plotter(lighting=None, window_size=(800, 800))
pl.add_light(light1)
pl.add_light(light2)
pl.add_mesh(
    mesh,
    ambient=0.2,
    diffuse=0.5,
    specular=0.5,
    specular_power=90,
    smooth_shading=True,
    color='orange',
)
pl.add_mesh(base_mesh)
pl.enable_shadows()
pl.camera.zoom(1.5)
pl.show()