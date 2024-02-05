PythonでCGを作りたい人のためのPyVista入門
=========================================
.. todo::

   日食で光の表現をする。

小山哲央(`@tkoyama010 <https://twitter.com/tkoyama010>`_)です。
今回は私が開発に参加している3次元可視化ツール `PyVista <https://pyvista.github.io/pyvista-docs-dev-ja/>`_ について紹介します。
PyVistaは科学技術計算の3次元可視化のために開発されたツールですが、CGを作成する機能があります。
そこで今回はPythonが好きでCGを作ってみたい人に向けてPyVistaでCGを作成する方法を本記事で紹介します。

インストール
------------

本記事の動作確認に使用したPython、PyVistaのバージョンは以下のとおりです。
PyVistaは2024年1月現在、Python3.8以上をサポートしています。

* Python 3.11.2
* PyVista 0.43.1

PyVistaは `pip` コマンドでインストールすることができます。

.. code-block:: bash

    $ pip install pyvista

インストール後、Pythonで以下のコードを実行して図のようなウィンドウが表示されることを確認してください。

.. pyvista-plot::
    :include-source: True
    :context:

    >>> import pyvista as pv
    >>> mesh = pv.Sphere()
    >>> mesh.plot()

これがPyVistaのHello Worldです。
ウィンドウの表示は環境により多少異なる場合があります。
球が表示されたらインストール成功です。

地球儀を作ろう
--------------

3次元コンピュータグラフィックスでは3Dモデル表面に質感を与えるためにテクスチャマッピングという手法が使用されます。
そこで、先程の3Dモデルにテクスチャを追加してみましょう。
テクスチャは自分自身で準備した画像を指定することもできますが、今回はPyVistaで提供されているテクスチャの素材を使用することにしましょう。
PyVistaでは入門用のデータがパッケージに同封されており、以下のように取得することができます。
`Texture` オブジェクトの `plot()` メソッドを使用することで地球のテクスチャが表示されます。

.. pyvista-plot::

    from pyvista import examples

    texture = examples.load_globe_texture()
    texture.plot()

ロードしたテクスチャでテクスチャマッピングを行いましょう。
テクスチャマッピングの際にはイメージの空間参照を `active_texture_coordinates` に定義する必要があります。

.. todo::

   説明をもう少し詳しく

.. pyvista-plot::

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

ご覧の通り、地球儀が作成できていることがわかります。

太陽の光を表現しよう
--------------------

前節ではテクスチャマッピングをすることで地球儀を作成しました。
しかし、もう少しリアリティを演出したいですね。
そこでこの節では地球儀に背景を設定しライトニングを行うことで太陽の光を表現します。
PyVistaのLightオブジェクトを使用してレンダリング用のバーチャルライトを設定します。

.. pyvista-plot::

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

.. ファイルからモデルを読み込む
.. ----------------------------

他の惑星も作ろう
----------------

.. pyvista-plot::

    import pyvista as pv
    from pyvista import examples
    mesh = examples.planets.load_moon()
    texture = examples.planets.download_moon_surface(texture=True)
    pl = pv.Plotter()
    image_path = examples.planets.download_stars_sky_background(
        load=False
    )
    pl.add_background_image(image_path)
    _ = pl.add_mesh(mesh, texture=texture)
    pl.show()


まとめ
------

以上がPyVistaを使用したCGの作り方になります。
PyVistaのAPIはMatplotlibに影響を受けているため、
PythonやMatplotlibを使用している人には扱いやすいと思います。

.. レンダリング
.. ------------

.. .. pyvista-plot::
..
..     from itertools import product
..     import pyvista as pv
..     from pyvista import examples
..
..     cubemap = examples.download_sky_box_cube_map()
..     colors = ['red', 'teal', 'black', 'orange', 'silver']
..
..     p = pv.Plotter()
..     p.set_environment_texture(cubemap)
..
..     for i, j in product(range(5), range(6)):
..         sphere = pv.Sphere(radius=0.5, center=(0.0, 4 - i, j))
..         p.add_mesh(sphere, color=colors[i], pbr=True, metallic=i / 4, roughness=j / 5)
..
..     p.view_vector((-1, 0, 0), (0, 1, 0))
..     p.show()


.. .. pyvista-plot::
..
..     import numpy as np
..
..     import pyvista as pv
..     from pyvista import examples
..
..     cow = examples.download_cow()
..     cow.rotate_x(90, inplace=True)
..     plotter = pv.Plotter(lighting='none', window_size=(1000, 1000))
..     plotter.add_mesh(cow, color='white')
..     floor = pv.Plane(center=(cow.center[0], cow.center[1], cow.bounds[-2]), i_size=30, j_size=25)
..     plotter.add_mesh(floor, color='green')
..
..     UFO = pv.Light(position=(0, 0, 10), focal_point=(0, 0, 0), color='white')
..     UFO.positional = True
..     UFO.cone_angle = 40
..     UFO.exponent = 10
..     UFO.intensity = 3
..     UFO.show_actor()
..     plotter.add_light(UFO)
..
..     # enable shadows to better demonstrate lighting
..     plotter.enable_shadows()
..
..     plotter.camera_position = [(28, 30, 22), (0.77, 0, -0.44), (0, 0, 1)]
..     plotter.show()
..
.. .. pyvista-plot::
..
..     import numpy as np
..
..     import pyvista
..     from pyvista import examples
..
..     mesh = examples.download_dragon()
..     mesh.rotate_x(90, inplace=True)
..     mesh.rotate_z(120, inplace=True)
..
..     light1 = pyvista.Light(
..         position=(0, 0.2, 1.0),
..         focal_point=(0, 0, 0),
..         color=[1.0, 1.0, 0.9843, 1.0],  # Color temp. 5400 K
..         intensity=0.3,
..     )
..
..     light2 = pyvista.Light(
..         position=(0, 1.0, 1.0),
..         focal_point=(0, 0, 0),
..         color=[1.0, 0.83921, 0.6666, 1.0],  # Color temp. 2850 K
..         intensity=1,
..     )
..
..     # Add a thin box below the mesh
..     bounds = mesh.bounds
..     rnge = (bounds[1] - bounds[0], bounds[3] - bounds[2], bounds[5] - bounds[4])
..
..     expand = 1.0
..     height = rnge[2] * 0.05
..     center = np.array(mesh.center)
..     center -= [0, 0, mesh.center[2] - bounds[4] + height / 2]
..
..     width = rnge[0] * (1 + expand)
..     length = rnge[1] * (1 + expand)
..     base_mesh = pyvista.Cube(center, width, length, height)
..
..     # rotate base and mesh to get a better view
..     base_mesh.rotate_z(30, inplace=True)
..     mesh.rotate_z(30, inplace=True)
..
..     # create the plotter with custom lighting
..     pl = pyvista.Plotter(lighting=None, window_size=(800, 800))
..     pl.add_light(light1)
..     pl.add_light(light2)
..     pl.add_mesh(
..         mesh,
..         ambient=0.2,
..         diffuse=0.5,
..         specular=0.5,
..         specular_power=90,
..         smooth_shading=True,
..         color='orange',
..     )
..     pl.add_mesh(base_mesh)
..     pl.enable_shadows()
..     pl.camera.zoom(1.5)
..     pl.show()
