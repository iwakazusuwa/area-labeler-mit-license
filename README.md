# ea-labeler-mit-license
- 画像上で自由に点を打ち、複数のポリゴンエリアを定義・名前付けしてCSVに保存できるPythonツールです。
- 元画像上に色付きポリゴンとしてエリア範囲を描画し結果を画像ファイル（labeled_areas.png）に保存するPythonツールです。

## 概要
- OpenCVを使ったGUIで、画像に対して多角形エリアを作成
- Tkinterのポップアップでエリア名を入力可能
- 定義したエリアの頂点座標をCSVで保存
- 後続処理のためのエリア範囲描画コードあり

## ファイル構成例

```
project_root/
├── area_labeler.py         # エリア定義ツールのコード
├── draw_areas.py           # エリアを色付きで描画するコード
├── car.png                 # 元画像（1380×840）
├── xy_points.csv           # エリア座標のCSV（入力データ）
├── labeled_areas.png       # エリア描画後の出力画像
├── README.md
└── LICENSE
```
サンプル画像（car.png など）は含めていません。任意の画像ファイルをご用意ください。

## 必要な環境・依存パッケージ
- Python 3.x
- OpenCV (opencv-python)
- NumPy
- Tkinter（Python標準GUIライブラリ。通常は標準で含まれます）


pip install opencv-python numpy

## 使い方
このスクリプトは、コマンドライン操作なしで、ファイルをダブルクリックするだけで実行できます。

### area_labeler.py について
1. area_labeler.py をダブルクリック
2. 画像上で左クリックで点を追加、右クリックで直前の点を削除
3. スペースキーでエリア確定＆名前入力
4. Enterキーで全エリア保存して終了
5. ESCキーでキャンセル


### draw_areas.py について
1. draw_areas.py をダブルクリック


## License
MIT License（詳細はLICENSEファイルを参照）



#### 作成者：iwakazusuwa(Swatchp)


