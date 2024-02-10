PythonでCGを作りたい人のためのPyVista入門
=========================================
.. todo::

   日食で光の表現をする．

小山哲央(`@tkoyama010 <https://twitter.com/tkoyama010>`_)です．
今回は私が開発に参加している3次元可視化ツール `PyVista <https://pyvista.github.io/pyvista-docs-dev-ja/>`_ について紹介します．
PyVistaは科学技術計算の3次元可視化のために開発されたツールですが，CGを作成する機能があります．
そこで今回はPythonが好きでCGを作ってみたい人に向けてPyVistaでCGを作成する方法を本記事で紹介します．

インストール
------------

本記事の動作確認に使用したPython，PyVistaのバージョンは以下のとおりです．
PyVistaは2024年2月現在，Python3.8以上をサポートしています．

* Python 3.11.2
* PyVista 0.43.1

PyVistaは `pip` コマンドでインストールすることができます．

.. code-block:: bash

    $ pip install pyvista

インストール後，Pythonで以下のコードを実行して図のようなウィンドウが表示されることを確認してください．

.. pyvista-plot::
    :include-source: True
    :context:

    >>> import pyvista as pv
    >>> mesh = pv.Sphere()
    >>> mesh.plot()

これがPyVistaのHello Worldです．
ウィンドウの表示は環境により多少異なる場合があります．
球が表示されたらインストール成功です．

地球を作ってみる
----------------

3次元コンピュータグラフィックスでは3Dモデル表面に質感を与えるためにテクスチャマッピングという手法が使用されます．
そこで，先程の3Dモデルにテクスチャを追加してみましょう．
テクスチャは自分自身で準備した画像を指定することもできますが，今回はPyVistaで提供されているテクスチャの素材を使用することにしましょう．
PyVistaでは入門用のデータがパッケージに同封されており，以下のように取得することができます．
`Texture` オブジェクトの `plot()` メソッドを使用することで地球のテクスチャが表示されます．

.. pyvista-plot::

    from pyvista import examples

    texture = examples.load_globe_texture()
    texture.plot()

ロードしたテクスチャでテクスチャマッピングを行いましょう．
テクスチャマッピングの際にはイメージの空間参照を `active_texture_coordinates` に定義する必要があります．

.. todo::

   説明をもう少し詳しく

以下のコードを実行して地球が表示されたら実行成功です．

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

地球の横に月を追加してみる
--------------------------

次に地球の隣に月を追加してみましょう．
PyVistaには月のデータセットが準備されているので，地球と並べて表示してみましょう．
月のデータセットは `pyvista.examples.planets.load_moon` 関数で取得することができます．
PyVistaでは複数オブジェクトを描画することも可能です．
複数のオブジェクトを配置する際には `Plotter` オブジェクトを使用します．
これは， `Matplotlib` の `Figure` オブジェクトのようなものです．

.. pyvista-plot::

    import pyvista as pv
    from pyvista import examples

    pl = pv.Plotter()
    mesh = examples.planets.load_moon()
    texture = examples.planets.download_moon_surface(texture=True)
    _ = pl.add_mesh(mesh, texture=texture)
    pl.show()

背景に夜空の星を追加してみる
----------------------------

次に背景を星空にしてみましょう．
次に背景に夜空の星を追加してみましょう．
宇宙空間に浮かぶ地球を表現することができました．
以下のコードを実行して宇宙空間に浮かぶ地球と月が表示されたら実行成功です．

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

太陽の光を表現してみる
----------------------

前節ではテクスチャマッピングをすることで地球儀を作成しました．
しかし，もう少しリアリティを演出したいですね．
そこでこの節では地球儀に背景を設定しライトニングを行うことで太陽の光を表現します．
PyVistaのLightオブジェクトを使用してレンダリング用のバーチャルライトを設定します．

.. pyvista-plot::

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

カメラを操作してみる
--------------------

まとめ
------

今回はPyVistaを使用したCGの作り方を説明してきました．
PyVistaのAPIはMatplotlibに影響を受けているため，
PythonやMatplotlibを使用している人には扱いやすいと思います．
Matplotlibは2Dプロットに特化しているため，
3Dの描画に難がありましたが．
PyVistaを使用することでそれが容易になりました．

.. ## プロフィール
..
.. ```{figure} images/profile.jpg
.. :alt: アイコン
.. :width: 100px
.. :align: left
.. ```
..
.. [@tkoyam010](https://twitter.com/tkoyama010)というハンドル名で活動。
.. 都内のIT企業で数値シミュレーションソフトの開発と受託解析を行うシステムエンジニアとして働く。
..
.. 可視化ライブラリ [PyVista](https://pyvista.github.io/pyvista-docs-dev-ja/) のメンテナ兼ドキュメント翻訳者。
.. SciPy 2023 チュートリアル座長。
..
.. 著書に『[Pythonによる有限要素法 実装ノート](https://www.amazon.co.jp/dp/B09SPMYZN4)』がある。
..
.. Facebook：[tetsuo.koyama.94](https://www.facebook.com/tetsuo.koyama.94)
..
.. Twitter：[@tkoyama010](https://twitter.com/tkoyama010)
..
.. GitHub：[tkoyama010](https://github.com/tkoyama010/)
