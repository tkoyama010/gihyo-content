import numpy as np

import pyvista as pv
from pyvista import examples

cow = examples.download_cow()
cow.rotate_x(90, inplace=True)
plotter = pv.Plotter(lighting='none', window_size=(1000, 1000))
plotter.add_mesh(cow, color='white')
floor = pv.Plane(center=(cow.center[0], cow.center[1], cow.bounds[-2]), i_size=30, j_size=25)
plotter.add_mesh(floor, color='green')

UFO = pv.Light(position=(0, 0, 10), focal_point=(0, 0, 0), color='white')
UFO.positional = True
UFO.cone_angle = 40
UFO.exponent = 10
UFO.intensity = 3
UFO.show_actor()
plotter.add_light(UFO)

# enable shadows to better demonstrate lighting
plotter.enable_shadows()

plotter.camera_position = [(28, 30, 22), (0.77, 0, -0.44), (0, 0, 1)]
plotter.show()