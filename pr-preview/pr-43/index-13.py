import pyvista
from pyvista import examples

helmet_file = examples.gltf.download_damaged_helmet()
texture = examples.download_dikhololo_night()

pl = pyvista.Plotter()
pl.import_gltf(helmet_file)
pl.set_environment_texture(texture)
pl.camera.zoom(1.7)
pl.show()