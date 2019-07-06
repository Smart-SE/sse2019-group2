node-red で csvを開く方法			2019/7/6

[目的]
Node-red はデフォルトでは、画像も含めて、コンピュータ上の
データを読み込むことができません。
そのため、ローカルディレクトリを読み込めるように
変更する必要があります。
# 今回はCSVを読み込むために操作していますが、
# 画像等をNode-redで読みたい場合も一緒です。


[手順]
1. Node-red がインストールされているディレクトリに移動
（Raspbian ならば) /home/pi/.node-red/
 (Windows  ならば) C:\Users\WASEDA\.node-red\

2. settings.js を編集
  上記ディレクトリ内に settings.js があるため、テキストエディタ等で開く。
  106行目あたりから、以下の記載があるので、"//" を外して有効化し、
  csvファイルを格納する場所を指定します。
  -------
    // When httpAdminRoot is used to move the UI to a different root path, the
    // following property can be used to identify a directory of static content
    // that should be served at http://localhost:1880/.
★  httpStatic: 'C:/Users/WASEDA/.node-red/node-red-static/',
  -------
  → ここでは .node-red 配下に node-red-static というディレクトリを
     作成してそこに csv を格納

3. node-red を再起動
   node-red が起動している場合は、再起動する。

4. node-red の修正
   Result画面のノードで、ファイルパスを指定している箇所があるため、
   csvを格納しているPathに修正する
   
   [ファイルパスを記載] ノードを開き、csv の格納場所を絶対パスで指定する
   C:/Users/WASEDA/.node-red/node-red-static/test.csv
   
   
以上
