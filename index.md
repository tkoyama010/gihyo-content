# SciPy 2022 カンファレンスレポート

小山哲央です。
アメリカで開催されたSciPy2022に参加してきたので、現地の様子をこのレポートで伝えたいと思います。

## SciPyについて

[SciPy2022](https://www.scipy2022.scipy.org/)は科学技術計算やデータの可視化を専門としたPythonのユーザーや開発者が結集し、知見を共有することを目的とした国際カンファレンスです。
SciPyと聞くと[PythonライブラリのSciPy](https://github.com/scipy/scipy)を連想される方が多いと思います。
しかし、実態は科学技術計算やデータの可視化に関するPythonライブラリのコミュニティが多数参加するカンファレンスです。
そのため、科学に関する[PyCon](https://us.pycon.org/2022/)であると表現したほうが適当です。

以下は SciPy 2022 の開催概要です。
参加者数の情報はカンファレンス初日の主催者発表を基にしています。

```{list-table}

* - URL
  - [https://www.scipy2022.scipy.org/](https://www.scipy2022.scipy.org/)
* - 日程
  - - チュートリアル: 2022年7月11日(月)、12日(火)
    - カンファレンス: 2022年7月12日(火)〜15日(金)
    - スプリント: 2022年7月16日(土)、17日(日)
* - 場所
  - アメリカ合衆国、オースティン
* - 会場
  - [At&T Hotel & Conference Center](https://meetattexas.com/)
* - 参加者数
  - - カンファレンス現地参加 565人
    - カンファレンスオンライン参加 190人
    - スプリント現地参加 250人
* - 主催
  - [Enthought, Inc.](https://www.enthought.com/)
```

## 参加目的

筆者は普段OSS活動の一環として[PyVista](https://pyvista.github.io/pyvista-docs-dev-ja/)というプロジェクトに参加しています。
このプロジェクトはPythonのデータ可視化ライブラリで近年最も注目されているものの1つです。
以下の画像はPyVistaの使用例の一部です。
今回、ライブラリの広報とコミュニテイの交流を目的としてこのカンファレンスに参加してきました。

```{figure} images/pyvista_examples.png
:alt: PyVistaの例
:width: 400px
PyVistaの例
```

ここでは、PyVistaの説明をします。
[Visualization Toolkit（VTK）](https://vtk.org/)という3Dコンピュータグラフィックス・画像処理・可視化のための、自由に利用可能なオープンソースソフトウェアがあります。
1993年から開発が行われており3Dコンピュータグラフィックス・画像処理・可視化の分野でユーザーが必要なことがほぼ全て実現できます。
世界中にユーザーと開発者がおりさらにロスアラモス国立研究所やサンディア国立研究所の研究者も協力しています。
メンテナンスは[Kitware Inc.](https://www.kitware.com/)が行っています。
他にもVTKをベースとした[ParaView](https://www.paraview.org/)というGUIソフトを公開しています。
スーパーコンピュータの計算の可視化はParaViewで行われることが多いです。
以上のようにVTKは世界的に使用されるライブラリですがPython APIはPythonicではありません。

そこで、VTKのAPIをimportしてNumPyやMatplotlibのようにAPIを呼び出せるようにすることを目指してvtkiプロジェクトが[Alex Kaszynski](https://github.com/akaszynski)氏により立ち上げられました。
その後、[Bane Sullivan](https://banesullivan.com/)氏による積極的な貢献があり、Pythonicな可視化ライブラリPyVistaとしてPyPIにリリースされました。

現在は筆者も含め開発チームは10名で構成されています。
また、100名以上のcontributorとGitHubで1.4k以上のStarを獲得した成功プロジェクトになっています。

## チュートリアル

PyVistaコミュニティとして、チュートリアルを行うことになったのは、筆者が2021年に[こちらの GitHub Discussion](https://github.com/pyvista/pyvista/discussions/1513) で提案したのがきっかけでした。
チュートリアルには、[JupyterLab](https://jupyter.org/)の環境を[MyBinder](https://mybinder.org/)というサービスで提供することになりました。
MyBinderはGitHub 上のJupyter Notebooks をクラウドで実行することのできるサービスです。

チュートリアルの準備は半年近く前からしていましたが他の2人が忙しくほぼ私1人でやっていました。
私が日本を出るくらいの段階で他の2人が動き出した感じです。
ただし、最終的な成果物への貢献は他の2人の貢献が大きいです。
行きの飛行機に乗るまでSlackで活発に議論しました。
最終的に筆者が作成した部分はほぼ書き換わることになりましたが、たたき台となる情報を集めることはできたのでそこはよかったかなと思います。
それについては2人も感謝してもらえました。

チュートリアル前日にはじめて前出のAlex氏とBane氏と顔合わせをしました。
3人でホテルのラウンジで最後の追い込みの作業をしました。
2人ともとても優秀で作業が早く、人気のライブラリを生み出す人はこういう人達なのかと感動しました。

当日は前日まで資料を作っていたため寝坊し、チュートリアル開始の30分前に起床し焦りましたが、幸いチュートリアルには開始ギリギリに到着しました。
これは会場とホテルが一体だったのが良かったです。
資料は完成していましたが、説明用の原稿はゼロで即興でやることになりました。

チュートリアルは4時間で内容は以下の通りです。
Slackのチュートリアルチャンネルの参加者は30名でした。

1. はじめに (Alex氏)
1. 基本的な使い方 (Alex氏)
1. メッシュとは? (Bane氏)
1. プロットオプションとアニメーション (Bane氏)
1. フィルタ (Bane氏)
1. PyVistaの活用 (筆者)
1. PyVistaとVTK (Bane氏)
1. PyVistaとSphinx (Alex氏)
1. PyVistaのウィジェット (筆者)
1. PyVistaとQT (Alex氏)

チュートリアル後には参加者からPyVistaで自分が欲しいプロットをどのように実現するかについての相談もあり、ライブラリの有用性を伝えることができたと感じました。

筆者は英語での抽象的な説明が難しかったためより実践的で説明がしやすいセクションを担当しました。
それでも英語の即興での発表は大変でした。
ただ、チームでやっているため他のメンバーの言い回しを流用したりして自分の英語力を補うことができたのでそこはよかったと思います。
当然かもしれませんが、英語非ネイティブが英語圏でチュートリアルをやるには英語ネイティブの協力が必要不可欠だと実感しました。

```{figure} images/tutorial.gif
:alt: 筆者が担当したチュートリアルの一部
:width: 400px
筆者が担当したチュートリアルの一部
```

このイベントのチュートリアルしか筆者は知りませんが、どのチュートリアルもJupyterLabを使っています。
ただ、JupyterLabだけを使ったチュートリアルはNotebookが長くなりすぎて分かりづらいとBane氏が苦言していました。
そのため、今回は説明資料に[Sphinx](https://www.sphinx-doc.org/ja/master/)を使い、デモとエクササイズはJupyterLabを使うことにしました。
説明が書かれているSphinxの資料と、デモ用のJupyterLabが分割していることで、チュートリアルの構成が参加者にわかりやすくなりました。

担当セクション以外の時間は参加者のサポートをしていました。
その際に後ろから見ていましたがみんな集中して聴いてくれていたのでうれしかったです。
参加者が質問をしてくれて話が広がったり、詳しい人が説明を補足してくれたりしてくれてトークとは違う楽しさがありました。
説明はSphinxにすべてまとめてありましたしJupyterLabはみんなMyBinderを使っていたので特にサポートが必要な人はいませんでした。
筆者は2020年からオンラインでSciPyのチュートリアルに参加していましたが、クラウドの環境でチュートリアルを受ける人が年々増えていると感じます。
ちなみに、1人だけWSLで実行をしたいという人がいて相談にのりました。

チュートリアル終了後、PyVistaコミュニティで打ち上げをしました。
普段OSSの活動をしている姿しか知らないので、各自ビジネスは何をやっているのかの話題で盛り上がりました。
ちなみにPyVistaプロジェクトとして[NumFOCUS](https://numfocus.org/)に申し込むことがこの集まりで決まりました。
チュートリアルはPyVistaの新規ユーザー獲得につながるとの判断で[pyvista-tutorial](https://github.com/pyvista/pyvista-tutorial)リポジトリをメンテナンスしていくことにしました。

## 会場の雰囲気

こちらがカンファレンス中の会場の様子です。
丸テーブルに座って食事などをとりながらのんびりとトークを聴いていました。

```{figure} images/room.jpg
:alt: 会場の様子
:width: 400px
会場の様子
```

会場の前にはブースがありそれぞれの組織が宣伝のためのブースを出していました。

```{figure} images/booth.jpg
:alt: ブースの様子
:width: 400px
ブースの様子
```

[Anaconda](https://www.anaconda.com/)が帽子を配っていましたので1つもらいました。

```{figure} images/hat.jpg
:alt: Anacondaの帽子
:width: 400px
Anacondaの帽子
```

PyConより企業の影響が強いという印象を受けましたが、一般的な学会よりは自由な雰囲気です。
参加者には毎回参加しているコミュニティのコアメンバーもいれば今年初参加の人もいます。
ただ、参加者はフレンドリーに議論をしているため両者の垣根は感じません。
筆者とレセプション会場までUberで相乗りした参加者は「自由な雰囲気が好きで何回も参加している」と言っていました。
Ph.D.を取得している人が多いため、ポスドクのキャリア形成のセッションも開かれていました。

また、[SciPy](https://github.com/scipy/scipy)リポジトリのスター数がもうすぐ10kにとどきそうなのでみんなでスターを押そうと呼びかけていました。
カンファレンス終了時にめでたく10kに到達しました。
またカンファレンス最終日に[Backstreet Boys](https://ja.wikipedia.org/wiki/%E3%83%90%E3%83%83%E3%82%AF%E3%82%B9%E3%83%88%E3%83%AA%E3%83%BC%E3%83%88%E3%83%BB%E3%83%9C%E3%83%BC%E3%82%A4%E3%82%BA)のパロディバンドが”I Want It That Way”の[替え歌を歌っていました](https://www.youtube.com/watch?v=yhwXDaaq09s)。
会場は大盛り上がりでした。

## キーノート

キーノートは日本での「基調講演」に当たるものです。
カンファレンス3日間の間に1日1公演、計3回行われました。

初日の ["Software and Services to Fully Realize the Impact of AI, Machine Learning, Automation, and Community Engagement in Science"](https://www.youtube.com/watch?v=D0S6blFPOCg) は機械学習やAIにPythonがどのように活用されているかの公演でした。
この発表は公演者がそれぞれの開発者にインタビューをしていく形式でした。
話す人が各スライドで変わるので最後まで楽しんで聴くことができ、とてもいい発表方法だと思いました。

```{figure} images/keynote.jpg
:alt: キーノートのインタビューの様子
:width: 400px
キーノートのインタビューの様子
```

## トークセッション

カンファレンス中、筆者は可視化とコミュニティ活動に興味があったのでそのセッションを中心にトークをみていきました。
今年は可視化のセッションが昨年よりも多かったため見応えがありました。
カンファレンスのスケジュールは[こちら](https://www.scipy2022.scipy.org/update-conference-schedule)から確認できます。

トークセッションの中では特に ["Scientific Python: From GitHub to TikTok"](https://youtu.be/jYGxHV7INs4) が印象に残りました。
[Scientific Pythonプロジェクト](https://scientific-python.org/)は、科学系のPythonコミュニティを成長させることを目的としているとのことです。
NumPyやSciPyなど各ライブラリごとのコミュニティはこれまでありましたが、科学系のPythonエコシステム全体でコミュニティを作ることに新しさを感じました。
[YouTube](https://www.youtube.com/c/ScientificPython-org)や[TikTok](https://www.tiktok.com/@scientific.python)を使ってOSSへのコントリビューションの敷居を下げる活動もしているそうです。

```{figure} images/talk.png
:alt: Scientific Pythonプロジェクトの説明
:width: 400px
Scientific Pythonプロジェクトの説明
```

## BoFセッション

BoFはBirds of a Featherの略で、司会が短いプレゼンテーションを行い、大部分の時間は出席者全員で議論を行うセッションです。
トークに比べ参加者の幅広い意見を募ることができます。
SciPyはコミュニティの活性化に重点をおいているため、BoFのセッションが多く設けられています。

個人的には "Python Data Visualization, 2022" が一番楽しめました。
Pythonの可視化ライブラリは数が多いのでこのような横断的なセッションは貴重です。
ここでは、主に以下のような内容が議論されていました。

1. Pythonの可視化ライブラリが乱立しているためどれでプロットすればいいかわからない。
1. PyVistaが注目されている。
1. 可視化ライブラリの開発は趣味で行っているメンバーが多い。
   NumFOCUSなどのスポンサーシップを利用する必要がある。

最終日には "SciPy 2023 planning BoF" に参加しました。
これはSciPy2022のフィードバックとSciPy2023に向けての意見を募るセッションです。
以下のような意見が出ていました。

1. 名前が書かれた名札が配られていたため自己紹介の際に便利だった。
1. スプリントを初日にすれば参加率が上がるのではないか。
1. PyConではスペイン語でのトークセッションがある。英語以外のセッションが必要ではないか。

筆者は以下の2点について発言・質問しました。
1. スプリントを初日にすると、チュートリアルやトークの準備の時間となってしまい望ましくない結果になる。
1. 同じ内容を毎年チュートリアルでやることに問題はないか。

2つ目の質問については「採択されれば特に問題はない」とのことでした。
機会があれば今回のチュートリアルをアップデートして再度行いたいと考えています。

## ポスターセッション

ポスターセッションは各プロジェクトをポスターで紹介するセッションです。
セッション中は先程の会場にポスターが貼られ発表者がその前に立っています。
トークに比べ発表から得られる情報は限られますが、興味のあるプロジェクトについて対面で議論することができます。

こちらのポスターはインタラクティブな Web アプリやダッシュボードを作成できる[Panel](https://panel.holoviz.org/index.html)というライブラリを使って、JupyterNotebookのプロトタイプからWebアプリケーションを作る内容です。
筆者も普段プロトタイプをJupyterNotebookで作っているため、プロダクトとしてWebアプリケーションにする工程をまとめたこのポスターには興味を持ちました。

```{figure} images/poster.jpg
:alt: ポスターセッションの様子
:width: 400px
ポスターセッションの様子
```

## ライトニングトーク

4日間のカンファレンス中は毎日夕方にライトニングトークが行われます。
ライトニングトークは5分以内でプレゼンテーションを行うセッションです。
1つの発表が短いためより多くの参加者が自分の発表を行うことができます。

今回のカンファレンスでは天文学のトークが多数あったため、筆者も[惑星を3DCGで作成をする](https://github.com/pyvista/pyvista/pull/2994)という内容で申し込んでみました。
しかし、ライトニングトーク枠の3倍以上の希望者がおりトークはできませんでした。
SciPyでは、初参加・ライトニングトーク未経験が優先されます。
徹夜をして作ったので残念でした。

他には次のセクションで出てくるJorge Martínez氏が天体力学のライトニングトークをしていました。

```{figure} images/lightning-talk.png
:alt: ライトニングトークをするJorge Martínez氏
:width: 400px
ライトニングトークをするJorge Martínez氏
```

## スプリント

最後の2日間はスプリントが行われました。
スプリントは自分の興味のあるOSSプロジェクトに対して、コードのテスト、バグの修正、新機能の追加、ドキュメントの改善など、様々な貢献を行うセッションです。
また、OSSの著者やメンテナーと一緒に作業をする機会を設けることで、OSS初心者に貢献の機会を提供することも大きな目的です。

筆者はPyVistaのスプリントに参加しました。
Alex氏は帰宅する必要があったのでスプリントはオンライン参加、Bane氏も用事があるとのことで帰宅しました。
そのため、PyVistaのスプリントリーダーは筆者がやることになりました。
チャットには[GitHubDiscussion](https://github.com/pyvista/pyvista/discussions/2995)を使いました。
最終的に4名の方に参加してもらえました。

1人目は[Kelly Meehan](https://www.linkedin.com/in/kellysiobhanmeehan/)氏です。
[アメリカ合衆国森林局](https://www.fs.usda.gov/)の所属で調査の際の可視化にPyVistaを使いたいと考えているそうです。
2人目は[Roberto Pastor Muela](https://github.com/RobPasMue)氏です。
Alex氏がリーダーをしている[PyAnsys](https://github.com/pyansys)のメンバーです。
PyAnsysの結果の可視化にPyVistaを使用しているとのことでした。
3人目はカンファレンス中に仲良くなった[Charith Gunasekara](https://www.linkedin.com/in/charithgunasekara/)氏です。
PyVistaへのコントリビューションをしてみたいと話してくれたので参加してもらいました。
3人にはPyVistaプロジェクトでは最初のコントリビュートとして[docstringのExampleを追加する](https://github.com/pyvista/pyvista/issues/1629)というissueを用意しているのでそれに取り組んでもらいました。
この課題は直接ライブラリに影響を与えず、PyVistaの勉強にもなるため大変いい内容だと思っています。

4人目の[Jorge Martínez](https://github.com/jorgepiloto)氏はライトニングトークで作成した資料を、スプリント中にカンファレンス参加者がいるSlackで共有したところ反応してくれました。
彼もPyAnsysのメンバーです。
[Juan Luis Cano Rodríguez](https://github.com/astrojuanlu)氏とPythonの天体力学ライブラリ[poliastro](https://github.com/poliastro/poliastro)を開発しており、[惑星の可視化にPyVistaを使用したい](https://github.com/poliastro/poliastro/issues/1525)とのことでした。
[PyVista](https://github.com/pyvista/pyvista)と[poliastro](https://github.com/poliastro/poliastro)がそれぞれどこまで実装を担当するかについてスプリントで有益な議論ができました。

他には[Alt Text Sprints](https://hackmd.io/bfhftUCiTRqx2S8CTGUt6g?view)というワークショップがあり面白い試みだと思いました。
画像リンクにAlt Textを追加してOSSプロジェクトへのアクセスを改善することを目的にした活動です。

## 最後に

チュートリアル・カンファレンス・スプリント全日参加することができて満足しました。
普段、GitHub上でやり取りしている開発者と直接コミニケーションを取ることができたのは自分にとって大きな収穫でした。
NumFOCUSへの申請を決めたり、他のライブラリの開発者とコラボレーションについて議論するのはやはり対面が一番効果的なようです。
ここでは紹介しませんでしたが、カンファレンス以外でもNASAのツアーに行くなど充実した旅行になりました。
アメリカ渡航などの詳しい話は[こちらのPodcast](https://podcast.terapyon.net/episodes/0072.html)で話しています。
ぜひお聴きください。

```{figure} images/friends.jpg
:alt: 左から Charith Gunasekara氏, Bhupendra Raut氏 と筆者
:width: 400px
左から Charith Gunasekara氏, Bhupendra Raut氏 と筆者
```

ちなみに来年からSciPyの主催は Enthought, Inc. から[NFOCUS](https://numfocus.org/)移るとのことです。
今後も科学分野のPythonユーザーとしてSciPyに注目していきたいと思います。

## プロフィール

```{figure} images/profile.jpg
:alt: アイコン
:width: 100px
:align: left
```

[@tkoyam010](https://twitter.com/tkoyama010)というハンドル名で活動。
都内のIT企業で数値シミュレーションソフトの開発と受託解析を行うシステムエンジニアとして働く。

可視化ライブラリ [PyVista](https://pyvista.github.io/pyvista-docs-dev-ja/) のメンテナ兼ドキュメント翻訳者。
SciPy Japan 2020 座長。

著書に『[Pythonによる有限要素法 実装ノート](https://www.amazon.co.jp/dp/B09SPMYZN4)』がある。

Facebook：[tetsuo.koyama.94](https://www.facebook.com/tetsuo.koyama.94)

Twitter：[@tkoyama010](https://twitter.com/tkoyama010)

GitHub：[tkoyama010](https://github.com/tkoyama010/)
