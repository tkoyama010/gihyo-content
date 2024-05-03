PythonでCGを作りたい人のためのPyVista入門
=========================================

小山哲央(`@tkoyama010 <https://twitter.com/tkoyama010>`_)です．
今回は私が開発に参加している3次元可視化ツール `PyVista <https://pyvista.github.io/pyvista-docs-dev-ja/>`_ について紹介します．

PyVistaとは
-----------

PyVistaは，3次元可視化のためのPythonライブラリです．
このライブラリは，VTK（Visualization Toolkit）をラップしており，VTKの機能をPythonで簡単に利用できるようにしています．
PyVistaは，VTKの機能を継承しているため，高度な3次元可視化を行うことができます．
また，PyVistaは，VTKの機能を簡単に利用できるようにしただけでなく，Pythonの特性を活かして，VTKの機能をより使いやすくしています．
PyVistaは科学技術計算の3次元可視化のために開発されたツールですが，CGを作成する機能があります．
そこで今回はPythonが好きでCGを作ってみたい人に向けてPyVistaでCGを作成する方法を本記事で紹介します．

インストール
------------

本記事の動作確認に使用したPython，PyVistaのバージョンは以下のとおりです．
PyVistaは2024年5月現在，Python3.8以上をサポートしています．

* Python 3.11.6
* PyVista 0.43.6

PyVistaは `pip` コマンドでインストールすることができます．

.. code-block:: bash

    $ pip install pyvista

インストール後，Pythonで以下のコードを実行して図のようなウィンドウが表示されることを確認してください．

.. pyvista-plot::
    :include-source: True
    :context:

    import pyvista as pv
    mesh = pv.Sphere()
    mesh.plot()

これがPyVistaのHello Worldです．
ウィンドウの表示は環境により多少異なる場合があります．
球が表示されたらインストール成功です．

地球を作ってみる
----------------

3次元コンピュータグラフィックスでは3Dモデル表面に質感を与えるためにテクスチャマッピングという手法が使用されます．
そこで，先程の3Dモデルにテクスチャを追加してみましょう．
テクスチャは自分自身で準備した画像を指定することもできますが，今回はPyVistaで提供されているテクスチャの素材を使用することにしましょう．
PyVistaではデモンストレーション用のデータがパッケージに同封されており，以下のように取得することができます．
`Texture` オブジェクトの `plot()` メソッドを使用することで地球のテクスチャが表示されます．

.. pyvista-plot::

    from pyvista import examples

    texture = examples.load_globe_texture()
    texture.plot()

ロードしたテクスチャでテクスチャマッピングを行いましょう．
テクスチャマッピングの際にはイメージの空間参照を `active_texture_coordinates` に定義する必要があります．
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

Pythonではテクスチャマッピングに使用する式を比較的簡単に記述することができます．
自分が考えた式を実装してマッピングしてみるのも面白いかもしれません．
テクスチャマッピングの式を考えるのが難しい場合は，
PyVistaの `examples` モジュールにあるテクスチャマッピング済みのデータセットを使用することをおすすめします．
以下のコードは地球のデータセットをロードして表示するコードです．

地球の横に月を追加してみる
--------------------------

次に地球の隣に月を追加してみましょう．
PyVistaには月のデータセットが準備されているので，地球と並べて表示してみましょう．
月のデータセットは `pyvista.examples.planets.load_moon` 関数で取得することができます．
PyVistaでは複数オブジェクトを描画することも可能です．
複数のオブジェクトを配置する際には `Plotter` オブジェクトを使用します．
これは， `Matplotlib` の `Figure` オブジェクトに似ています．
以下のコードを実行して地球と月が表示されたら実行成功です．

.. pyvista-plot::

    import pyvista as pv
    from pyvista import examples

    pl = pv.Plotter()
    mesh = examples.planets.load_moon()
    texture = examples.planets.download_moon_surface(texture=True)
    _ = pl.add_mesh(mesh, texture=texture)
    pl.show()


背景を黒にしてみる
------------------

次に背景を夜空にしてみましょう．
次に背景に夜空の星を追加してみましょう．
宇宙空間に浮かぶ地球を表現することができました．
以下のコードを実行して宇宙空間に浮かぶ地球と月が表示されたら実行成功です．

.. pyvista-plot::

    import pyvista as pv
    from pyvista import examples
    mesh = examples.planets.load_moon()
    texture = examples.planets.download_moon_surface(texture=True)
    pl = pv.Plotter()
    pl.background_color = 'k'
    _ = pl.add_mesh(mesh, texture=texture)
    pl.show()

カメラを操作してみる
--------------------

pyvista.Camera クラスは， vtk.vtkCamera クラスに追加機能とPython APIを追加します．
pyvista.vtkCamera オブジェクトには，ほとんどの場合に適切に機能するデフォルトのライトセットが付属していますが，多くの場合，より実践的なカメラへのアプローチが必要です．
pyvista.Camera クラスは， vtk.vtkCamera クラスに追加機能とPython APIを追加します． pyvista.vtkCamera オブジェクトには，ほとんどの場合に適切に機能するデフォルトのライトセットが付属していますが，多くの場合，より実践的なカメラへのアプローチが必要です．

日食のような影を作ってみる
--------------------------
.. todo::

   日食で光の表現をする．

指向性ライトを使用すると，複雑なライティングシナリオを作成できます．
たとえば，ライトをアクター(この場合は球体)の真上に配置して，その真下にシャドウを作成できます．
次の例では，位置ライトを使用して，ライトの円錐角度と指数値を制御し，球体の下に日食のようなシャドウを作成します．

.. pyvista-plot::

    import pyvista as pv

    plotter = pv.Plotter(lighting=None, window_size=(800, 800))

    light = pv.Light(position=(0, 0, 3), show_actor=True, positional=True,
                     cone_angle=30, exponent=20, intensity=1.5)
    plotter.add_light(light)

    sphere = pv.Sphere(radius=0.3, center=(0, 0, 1))
    plotter.add_mesh(sphere, ambient=0.2, diffuse=0.5, specular=0.8,
                     specular_power=30, smooth_shading=True,
                     color='dodgerblue')

    grid = pv.Plane(i_size=4, j_size=4)
    plotter.add_mesh(grid, ambient=0, diffuse=0.5, specular=0.8, color='white')

    plotter.enable_shadows()
    plotter.set_background('darkgrey')
    plotter.show()


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

pyvista.Light インスタンスには，ヘッドライト，カメラライト，シーンライトの3つのタイプがあります．
ヘッドライトは常にカメラの軸に沿って輝き，カメラライトはカメラに対して固定位置を持ち，シーンライトはシーンに対して配置されるため，カメラの周りを移動してもシーンのライティングには影響しません．

照明をカスタムしてみる
----------------------

pyvista.Plotter クラスには，既定の照明システム用に次の3つのオプションがあります．

* ヘッドライトと4つのカメラライトで構成されたライトキット
* カメラの周囲に配置された3つのライトを含む照明システム，
* 照明なし．

メッシュのカラーにエンコードされた深度情報がない場合，正確に表示するには適切なライティング設定が最も重要になります．

ルーシーエンジェルデータセットをカスタム照明でプロットします．
"flame" で光をつくります
シーンライトを作成します．

.. pyvista-plot::

    from pyvista import examples
    import pyvista as pv
    dataset = examples.download_lucy()
    flame_light = pv.Light(
        color=[0.886, 0.345, 0.133],
        position=[550, 140, 950],
        intensity=1.5,
        positional=True,
        cone_angle=90,
        attenuation_values=(0.001, 0.005, 0),
    )
    scene_light = pv.Light(intensity=0.2)

    pl = pv.Plotter(lighting=None)
    _ = pl.add_mesh(dataset, smooth_shading=True)
    pl.add_light(flame_light)
    pl.add_light(scene_light)
    pl.background_color = 'k'
    pl.show()

月を地球の周りに回転させてみる
------------------------------

シーンを周回します．
軌道を描くには，まずシーンを表示し，プロッターを .show(auto_close=False) で開いたままにしておく必要があります．
また， pv.Plotter(off_screen=True) を設定する必要があるかもしれません．

.. pyvista-plot::

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

物理ベースレンダリングをしてみる
--------------------------------

VTK9は物理ベースレンダリング(PBR)を導入しており，その機能をPyVistaで公開しています．詳細については blog about PBR をお読みください．
PBRは pyvista.PolyData に対してのみサポートされており， add_mesh の pbr キーワード引数を介して起動できます．また， metallic および roughness 引数を使用してさらに制御できます．
この機能を，彫像の高品質メッシュを金属のようにレンダリングすることで示しましょう．

.. pyvista-plot::

    from itertools import product

    import pyvista as pv
    from pyvista import examples

    # Load the statue mesh
    mesh = examples.download_nefertiti()
    mesh.rotate_x(-90.0, inplace=True)  # rotate to orient with the skybox

    # Download skybox
    cubemap = examples.download_sky_box_cube_map()

    p = pv.Plotter()
    p.add_actor(cubemap.to_skybox())
    p.set_environment_texture(cubemap)  # For reflecting the environment off the mesh
    p.add_mesh(mesh, color='linen', pbr=True, metallic=0.8, roughness=0.1, diffuse=1)

    # Define a nice camera perspective
    cpos = [(-313.40, 66.09, 1000.61), (0.0, 0.0, 0.0), (0.018, 0.99, -0.06)]

    p.show(cpos=cpos)

Minecraftのような洞窟を作成してみる
-----------------------------------

.. todo::
    フィルタの説明をする．

ここでは， pyvista.core.utilities.features.sample_function() を使用して領域上のPerlinノイズをサンプリングし，ランダムな地表を生成します．
Minecraftなどのビデオゲームでは，Perlinノイズを使用して地表を作成します．ここでは，Minecraftの "洞窟" に似たボクセル化メッシュを作成します．
"freq" の値を自由に変更して， "洞窟" の形を変えることができます．
たとえば，周波数を低くすると，洞穴が大きく拡張します．
一方，任意の方向の周波数を高くすると，洞穴はより "静脈のように" 見え，開きにくくなります．

しきい値を変更して，開いている地形または閉じている地形の割合を増減します

.. pyvista-plot::

    import pyvista as pv
    freq = (1, 1, 1)
    noise = pv.perlin_noise(1, freq, (0, 0, 0))
    grid = pv.sample_function(noise, [0, 3.0, -0, 1.0, 0, 1.0], dim=(120, 40, 40))
    out = grid.threshold(0.02)
    mn, mx = [out['scalars'].min(), out['scalars'].max()]
    clim = (mn, mx * 1.8)

    out.plot(
        cmap='gist_earth_r',
        background='white',
        show_scalar_bar=False,
        lighting=True,
        clim=clim,
        show_edges=False,
    )

インタラクティブにパラメータを修正してみる
------------------------------------------

.. todo::
    毎回パラメータを修正してPythonを実行すのは面倒であることを伝える．

スライダウィジェットは，
pyvista.Plotter.add_slider_widget() メソッドおよび pyvista.Plotter.clear_slider_widgets() メソッドによって，
それぞれ有効および無効にすることができます．
これは，ほぼすべてのものに使用できる値を制御できるため，最も用途の広いウィジェットの1つです．

.. pyvista-plot::

    import pyvista as pv
    p = pv.Plotter()

    def create_mesh(value):
        res = int(value)
        sphere = pv.Sphere(phi_resolution=res, theta_resolution=res)
        p.add_mesh(sphere, name='sphere', show_edges=True)
        return


    p.add_slider_widget(create_mesh, [5, 100], title='Resolution')
    p.show()

外部のファイルからデータを読み込んでみる
----------------------------------------

glTFファイルをPyVistaのプロッティングシーンに直接インポートできます．
glTFフォーマットの詳細については， https://www.khronos.org/gltf/ を参照してください．
まず，サンプルをダウンロードします．
なお，ここではハイダイナミックレンジのテクスチャを使用していますが，
これはglTFファイルが一般的に物理ベースのレンダリングを含んでおり，VTK v9がハイダイナミックレンジのテクスチャをサポートしているためです．
プロッタを設定し，環境テクスチャを有効にします． これは，ダメージを受けたヘルメットの例のように，物理ベースのレンダリングが可能なメッシュに有効です．

.. pyvista-plot::

    import pyvista
    from pyvista import examples

    helmet_file = examples.gltf.download_damaged_helmet()
    texture = examples.download_dikhololo_night()

    pl = pyvista.Plotter()
    pl.import_gltf(helmet_file)
    pl.set_environment_texture(texture)
    pl.camera.zoom(1.7)
    pl.show()

ALIEN MONSTERSのピクセルアート
------------------------------

ここでは， pyvista.Box() を使って， ピクセルアート を作ります．
ピクセル文字列 ソース と ライセンス ．

.. pyvista-plot::

    import pyvista as pv
    from pyvista.demos import logo
    alien_str = """
        %         %
          %     %
        % % % % % %
      % %   % %   % %
    % % % % % % % % % %
    %   % % % % % %   %
    %   %         %   %
    %   % %     % %   %
          %     %
        %         %
    """


    alien = []
    for line in alien_str.splitlines()[1:]:  # skip first linebreak
        if not line:
            continue
        if len(line) < 20:
            line += (20 - len(line)) * ' '
        alien.append([line[i : i + 2] == '% ' for i in range(0, len(line), 2)])

    def draw_pixels(plotter, pixels, center, color):
        bounds = [
            center[0] - 1.0,
            center[0] + 1.0,
            center[1] - 1.0,
            center[1] + 1.0,
            -10.0,
            +10.0,
        ]
        for rows in pixels:
            for pixel in rows:
                if pixel:
                    box = pv.Box(bounds=bounds)
                    plotter.add_mesh(box, color=color)
                bounds[0] += 2.0
                bounds[1] += 2.0
            bounds[0] = center[0] - 1.0
            bounds[1] = center[0] + 1.0
            bounds[2] += -2.0
            bounds[3] += -2.0
        return plotter

    # Display MONSTERS
    p = pv.Plotter()
    p = draw_pixels(p, alien, [-22.0, 22.0], "green")
    p = draw_pixels(p, alien, [0.0, 22.0], "green")
    p = draw_pixels(p, alien, [22.0, 22.0], "green")
    p = draw_pixels(p, alien, [-22.0, 0.0], "blue")
    p = draw_pixels(p, alien, [0.0, 0.0], "blue")
    p = draw_pixels(p, alien, [22.0, 0.0], "blue")
    p = draw_pixels(p, alien, [-22.0, -22.0], "red")
    p = draw_pixels(p, alien, [0.0, -22.0], "red")
    p = draw_pixels(p, alien, [22.0, -22.0], "red")

    text = logo.text_3d("ALIEN MONSTERS", depth=10.0)
    text.points = text.points * 4.0
    text.translate([-20.0, 24.0, 0.0], inplace=True)

    p.add_mesh(text, color="yellow")
    p.show(cpos="xy")

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
