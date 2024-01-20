PythonでCGを作りたい人のためのPyVista入門
=========================================

小山哲央(`@tkoyama010 <https://twitter.com/tkoyama010>`_)です。
今回は私が開発に参加している3次元可視化ツール `PyVista <https://pyvista.github.io/pyvista-docs-dev-ja/>`_ について紹介します。
PyVistaは科学技術計算の3次元可視化のために開発されたツールですが、CGを作成する機能があります。
そこで今回はPythonが好きでCGを作ってみたい人に向けてPyVistaでCGを作成する方法を本記事で紹介します。

インストールをしてみよう
------------------------

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

    >>> from pyvista import examples
    >>> mesh = examples.download_dragon()
    >>> mesh.plot()

ウィンドウの表示は環境により多少異なる場合があります。
ドラゴンが表示されたらインストール成功です。

テクスチャマッピングをしてみよう
--------------------------------

立方体を描画しましたが、このままでは少し味気ないですね。
3次元コンピュータグラフィックスでは3Dモデル表面に質感を与えるためにテクスチャマッピングという手法が使用されます。
そこで、作成した3Dモデルにテクスチャを追加してみましょう。
テクスチャは自分自身で準備した画像を指定することもできますが、今回はPyVistaで提供されているテクスチャの素材を使用することにしましょう。
PyVistaでは入門用のデータがパッケージに同封されており、以下のように取得することができます。

`Texture` オブジェクトの `plot()` メソッドを使用することで以下のような子犬のテクスチャが表示されます。

.. pyvista-plot::

    from pyvista import examples

    tex = examples.download_puppy_texture()
    tex.plot()

ロードしたテクスチャでテクスチャマッピングを行いましょう。
テクスチャマッピングの際にはイメージの空間参照を `texture_map_to_sphere` メソッドで定義する必要があります。

.. pyvista-plot::

    import pyvista as pv
    from pyvista import examples

    mesh = pv.Sphere()
    tex = examples.download_masonry_texture()

    mesh.texture_map_to_sphere(inplace=True)
    mesh.plot(texture=tex)

ライティングをしてみよう
------------------------

テクスチャマッピングをしたことで3Dモデルの質感を表現することができました。

.. pyvista-plot::

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

シェーディングをしてみよう
--------------------------

.. pyvista-plot::

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

カメラを操作してみよう
----------------------

レンダリングをしてみよう
------------------------

モデリングをしてみよう
----------------------

ファイルからモデルを読み込んでみよう
------------------------------------

複数のモデルを描画してみよう
----------------------------

まとめ
------

