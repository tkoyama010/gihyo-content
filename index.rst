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

    >>> import pyvista as pv
    >>> mesh = pv.Sphere()
    >>> mesh.plot()

これがPyVistaのHello Worldです。
ウィンドウの表示は環境により多少異なる場合があります。
球が表示されたらインストール成功です。
