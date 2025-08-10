# Image Area Labeler
画像上で自由に点を打ち、複数のポリゴンエリアを定義・名前付けしてCSVに保存できるPythonツールです。

## 概要
- OpenCVを使ったGUIで、画像に対して多角形エリアを作成

- Tkinterのポップアップでエリア名を入力可能

- 定義したエリアの頂点座標をCSVで保存

- 後続処理のためのエリア範囲描画サンプルコード付き

## ファイル構成例

project_root/

├── area_labeler.py         # エリア定義ツールのコード<Br>
├── draw_areas.py           # エリアを色付きで描画するコード<Br>
├── car.png                 # 元画像<Br>
├── xy_points.csv           # エリア座標のCSV（入力データ）<Br>
├── labeled_areas.png       # エリア描画後の出力画像<Br>
├── README.md<Br>
├── LICENSE<Br>

## 必要な環境・依存パッケージ
- Python 3.x

- OpenCV (opencv-python)

- NumPy

- Tkinter（Python標準GUIライブラリ。通常は標準で含まれます）


pip install opencv-python numpy

## 使い方
1. area_labeler.py を実行

2. 画像上で左クリックで点を追加、右クリックで直前の点を削除

3. スペースキーでエリア確定＆名前入力

4. Enterキーで全エリア保存して終了

5. ESCキーでキャンセル


python area_labeler.py


# draw_areas.py について
draw_areas.py は、xy_points.csv に保存されたエリアの頂点情報を読み込み、
元画像上に色付きポリゴンとしてエリア範囲を描画し、結果を画像ファイル（labeled_areas.png）に保存するサンプルコードです。

エリアの可視化や確認にお役立てください。

python draw_areas.py


area_labeler.py を使って画像上で点を打ち、多角形エリアを作成し、
その頂点座標が xy_points.csv に保存されます。

# ライセンス
MIT License（詳細はLICENSEファイルを参照）


