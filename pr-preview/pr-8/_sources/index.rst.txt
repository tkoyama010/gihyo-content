PythonでCGを作りたい人のためのPyVista入門
=========================================

小山哲央([@tkoyama010](https://twitter.com/tkoyama010))です。
今回は私が開発に参加している3次元可視化ツール[PyVista](https://pyvista.github.io/pyvista-docs-dev-ja/)について紹介します。
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
テクスチャマッピングの際にはイメージの空間参照を `texture_map_to_plane` メソッドで定義する必要があります。

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

シェーディングをしてみよう
--------------------------

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

