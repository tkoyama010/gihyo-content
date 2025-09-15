import pyvista as pv
import numpy as np
from pyvista import examples

texture = examples.load_globe_texture()

sphere = pv.Sphere(
    radius=1, theta_resolution=120, phi_resolution=120, start_theta=270.001, end_theta=270
)

sphere.active_texture_coordinates = np.zeros((sphere.points.shape[0], 2))
for i in range(sphere.points.shape[0]):
    sphere.active_texture_coordinates[i] = [
        0.5 + np.arctan2(-sphere.points[i, 0], sphere.points[i, 1]) / (2 * np.pi),
        0.5 + np.arcsin(sphere.points[i, 2]) / np.pi,
    ]
sphere.plot(texture=texture)