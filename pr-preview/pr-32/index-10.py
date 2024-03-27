from itertools import product

import pyvista as pv
from pyvista import examples

# Load the statue mesh
mesh = examples.download_nefertiti()
mesh.rotate_x(-90.0, inplace=True)  # rotate to orient with the skybox

# Download skybox
cubemap = examples.download_sky_box_cube_map()

p = pv.Plotter()
p.add_actor(cubemap.to_skybox())
p.set_environment_texture(cubemap)  # For reflecting the environment off the mesh
p.add_mesh(mesh, color='linen', pbr=True, metallic=0.8, roughness=0.1, diffuse=1)

# Define a nice camera perspective
cpos = [(-313.40, 66.09, 1000.61), (0.0, 0.0, 0.0), (0.018, 0.99, -0.06)]

p.show(cpos=cpos)