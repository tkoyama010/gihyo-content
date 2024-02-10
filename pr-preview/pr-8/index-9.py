import pyvista as pv
from pyvista import examples

mesh = examples.download_st_helens().warp_by_scalar()
p = pv.Plotter()
p.add_mesh(mesh, lighting=False)
p.camera.zoom(1.5)
p.show(auto_close=False)
path = p.generate_orbital_path(n_points=36, shift=mesh.length)
p.open_gif("orbit.gif")
p.orbit_on_path(path, write_frames=True)
p.close()