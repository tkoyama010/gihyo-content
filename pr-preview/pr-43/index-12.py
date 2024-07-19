import pyvista as pv
p = pv.Plotter()

def create_mesh(value):
    res = int(value)
    sphere = pv.Sphere(phi_resolution=res, theta_resolution=res)
    p.add_mesh(sphere, name='sphere', show_edges=True)
    return


p.add_slider_widget(create_mesh, [5, 100], title='Resolution')
p.show()