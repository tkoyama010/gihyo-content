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

インストール後、PyVistaの以下のコードを実行して球体のウィンドウが表示されることを確認してください。

```python
import pyvsita as pv

m = pv.Sphere()
m.plot()
```

```{figure} images/hello-world.png
:alt: PyVistaのHello World
:width: 400px
PyVistaのHello World
```

ウィンドウの表示は環境により多少異なる場合があります。
ウィンドウが表示されたらインストール成功です。

## データの読み込みと表示

## メッシュ操作

## PyVistaの活用事例

## まとめ
