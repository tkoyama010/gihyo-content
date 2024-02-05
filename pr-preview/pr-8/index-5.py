import pyvista
from pyvista import examples

# Light of the Sun.
light = pyvista.Light()
light.set_direction_angle(30, -20)

# Load planets
mercury = examples.planets.load_mercury(radius=2439.0)
mercury_texture = examples.planets.download_mercury_surface(texture=True)
venus = examples.planets.load_venus(radius=6052.0)
venus_texture = examples.planets.download_venus_surface(texture=True)
earth = examples.planets.load_earth(radius=6378.1)
earth_texture = examples.load_globe_texture()
mars = examples.planets.load_mars(radius=3397.2)
mars_texture = examples.planets.download_mars_surface(texture=True)
jupiter = examples.planets.load_jupiter(radius=71492.0)
jupiter_texture = examples.planets.download_jupiter_surface(texture=True)
saturn = examples.planets.load_saturn(radius=60268.0)
saturn_texture = examples.planets.download_saturn_surface(texture=True)
# Saturn's rings range from 7000.0 km to 80000.0 km from the surface of the planet
inner = 60268.0 + 7000.0
outer = 60268.0 + 80000.0
saturn_rings = examples.planets.load_saturn_rings(inner=inner, outer=outer, c_res=50)
saturn_rings_texture = examples.planets.download_saturn_rings(texture=True)
uranus = examples.planets.load_uranus(radius=25559.0)
uranus_texture = examples.planets.download_uranus_surface(texture=True)
neptune = examples.planets.load_neptune(radius=24764.0)
neptune_texture = examples.planets.download_neptune_surface(texture=True)
pluto = examples.planets.load_pluto(radius=1151.0)
pluto_texture = examples.planets.download_pluto_surface(texture=True)

# Move planets to a nice position for the plotter. These numbers are not
# grounded in reality and are for demonstration purposes only.
mercury.translate((0.0, 0.0, 0.0), inplace=True)
venus.translate((-15000.0, 0.0, 0.0), inplace=True)
earth.translate((-30000.0, 0.0, 0.0), inplace=True)
mars.translate((-45000.0, 0.0, 0.0), inplace=True)
jupiter.translate((-150000.0, 0.0, 0.0), inplace=True)
saturn.translate((-400000.0, 0.0, 0.0), inplace=True)
saturn_rings.translate((-400000.0, 0.0, 0.0), inplace=True)
uranus.translate((-600000.0, 0.0, 0.0), inplace=True)
neptune.translate((-700000.0, 0.0, 0.0), inplace=True)

# Add planets to Plotter.
pl = pyvista.Plotter(lighting="none")
cubemap = examples.download_cubemap_space_16k()
_ = pl.add_actor(cubemap.to_skybox())
pl.set_environment_texture(cubemap, True)
pl.add_light(light)
pl.add_mesh(mercury, texture=mercury_texture, smooth_shading=True)
pl.add_mesh(venus, texture=venus_texture, smooth_shading=True)
pl.add_mesh(earth, texture=earth_texture, smooth_shading=True)
pl.add_mesh(mars, texture=mars_texture, smooth_shading=True)
pl.add_mesh(jupiter, texture=jupiter_texture, smooth_shading=True)
pl.add_mesh(saturn, texture=saturn_texture, smooth_shading=True)
pl.add_mesh(saturn_rings, texture=saturn_rings_texture, smooth_shading=True)
pl.add_mesh(uranus, texture=uranus_texture, smooth_shading=True)
pl.add_mesh(neptune, texture=neptune_texture, smooth_shading=True)
pl.add_mesh(pluto, texture=pluto_texture, smooth_shading=True)
pl.show()