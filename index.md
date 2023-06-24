# PythonでCGを作りたい人のためのPyVista入門

小山哲央([@tkoyama010](https://twitter.com/tkoyama010))です。
今回は私が開発に参加している3次元可視化ツールPyVistaについて紹介します。
PyVistaは科学技術計算の3次元可視化のために開発されたツールですが、CGを作成する機能があります。
そこで今回はPythonが好きでCGを作ってみたい人に向けてPyVistaでCGを作成する方法を本記事で紹介します。

## PyVistaとは

## インストール

本記事の動作確認に使用したPython、PyVistaのバージョンは以下のとおりです。
PyVistaは2023年6月現在、Python3.8以上をサポートしています。

- Python 3.11.2
- PyVista v0.39.0

PyVistaは `pip` コマンドでインストールすることができます。

```bash
$ pip install pyvista
```

インストール後、Pythonで以下のコードを実行して図のようなウィンドウが表示されることを確認してください。

```python
import pyvista as pv

m = pv.Cube()
m.plot()
```

```{figure} images/hello-world.png
:alt: PyVistaのHello World
:width: 400px
PyVistaのHello World
```

ウィンドウの表示は環境により多少異なる場合があります。
立方体が表示されたらインストール成功です。

## テクスチャマッピング

前節で立方体を描画しましたが、このままでは少し味気ないですね。
3次元コンピュータグラフィックスでは3Dモデル表面に質感を与えるためにテクスチャマッピングという手法が使用されます。
そこで、作成した3Dモデルにテクスチャを追加してみましょう。
テクスチャは自分自身で準備した画像を指定することもできますが、今回はPyVistaで提供されているテクスチャの素材を使用することにしましょう。
PyVistaでは入門用のデータがパッケージに同封されており、以下のように取得することができます。

```python
from pyvista import examples

tex = examples.download_puppy_texture()
tex.plot()
```

`Texture` オブジェクトの `plot()` メソッドを使用することで以下のような子犬のテクスチャが表示されます。

```{figure} images/read_texture.png
:alt: テクスチャの描画
:width: 400px
テクスチャの描画
```

ロードしたテクスチャでテクスチャマッピングを行いましょう。
テクスチャマッピングの際にはイメージの空間参照を `texture_map_to_plane` メソッドで定義する必要があります。

```python
m.texture_map_to_plane(inplace=True)
m.plot(texture=tex)
```

## ライティング

## まとめ
