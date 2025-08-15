# area-labeler-mit-license

画像上で自由に点を打ち、複数のポリゴンエリアを定義・名前付けして CSV に保存できる Python ツールです。  
元画像上に色付きポリゴンとしてエリア範囲を描画し、結果を画像ファイル（`labeled_areas.png`）に保存する機能も備えています。

---

## 概要

- OpenCV を使った GUI で、画像に対して多角形エリアを作成
- Tkinter のポップアップでエリア名を入力可能
- 定義したエリアの頂点座標を CSV で保存
- 後続処理のためのエリア範囲描画コードあり

---

## 特徴

- 画像上で直感的にエリアを定義・編集可能
- エリア定義を CSV 形式で保存し、他のツールやプログラムで利用可能
- エリア範囲を画像上に色付きで描画し、視覚的に確認可能

---

## フォルダ構成
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

---

## 使い方

1. `area_labeler.py` を実行し、画像上でエリアを定義
2. エリア名を入力し、座標を CSV に保存
3. `draw_areas.py` を実行し、エリア範囲を画像上に描画

```bash
python area_labeler.py
python draw_areas.py
```

#今後の展望
- エリア定義の精度向上
- GUI の改善
- 他の画像形式への対応

献方法
プロジェクトへの貢献は以下の方法で歓迎します：
- バグ報告や機能追加の提案は Issues で
- コード改善や新機能追加は Pull Request で
- ドキュメント改善や翻訳も歓迎


# License
MIT License（詳細はLICENSEファイルを参照）



#### 作成者：iwakazusuwa(Swatchp)


