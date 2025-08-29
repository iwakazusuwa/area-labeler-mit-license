import cv2
import csv
import random

# 画像ファイル名、出力ファイル名 
IMAGE_PATH = "car.png"
OUTPUT_CSV = "xy_points.csv"

# ファイル読み込み
points_df = pd.read_csv(OUTPUT_CSV)
img = cv2.imread(IMAGE_PATH)
if img is None:
    raise FileNotFoundError(f"画像が読み込めません: {IMAGE_PATH}")

# 色の用意（エリア数に合わせて自動生成）

random.seed(42)
area_names = points_df["name"].unique()
colors = {}
for area in area_names:
    colors[area] = [random.randint(50, 255) for _ in range(3)]

# エリアごとにポリゴンを描く関数
def draw_area(img, polygon_points, color, name, thickness=2):
    pts = np.array(polygon_points, np.int32)
    pts = pts.reshape((-1, 1, 2))
    # ポリゴン塗りつぶし（半透明）
    overlay = img.copy()
    cv2.fillPoly(overlay, [pts], color)
    alpha = 0.4
    cv2.addWeighted(overlay, alpha, img, 1 - alpha, 0, img)
    # ポリゴン輪郭
    cv2.polylines(img, [pts], isClosed=True, color=color, thickness=thickness)
    # エリア名の表示（ポリゴン重心に）
    M = cv2.moments(pts)
    if M["m00"] != 0:
        cx = int(M["m10"] / M["m00"])
        cy = int(M["m01"] / M["m00"])
        cv2.putText(img, name, (cx - 30, cy), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 0), 2, cv2.LINE_AA)
        cv2.putText(img, name, (cx - 30, cy), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 1, cv2.LINE_AA)

# エリアごとに描画
for area, group in points_df.groupby("name"):
    polygon_points = group[["x", "y"]].values.tolist()
    draw_area(img, polygon_points, colors[area], area)

# 保存
cv2.imwrite("a_labeled_areas.png", img)
print("✅ エリア描画済み画像を 'labeled_areas.png' に保存しました。")
