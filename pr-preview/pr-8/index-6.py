import pyvista
from pyvista import examples

light = pyvista.Light()
light.set_direction_angle(30, -20)

pl = pyvista.Plotter(lighting="none")
cubemap = examples.download_cubemap_space_16k()
_ = pl.add_actor(cubemap.to_skybox())
pl.set_environment_texture(cubemap, True)
pl.add_light(light)
mesh = examples.planets.load_earth()
texture = examples.load_globe_texture()
pl.add_mesh(mesh, texture=texture, smooth_shading=True)
# mercury.translate((0.0, 0.0, 0.0), inplace=True)
pl.show()