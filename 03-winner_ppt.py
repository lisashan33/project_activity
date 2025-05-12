from PIL import Image, ImageDraw, ImageFont
import pandas as pd
import os

from pathlib import Path

# 載入資料與圖片
# 修改識別身份
# 修改檔案路徑位置
file = pd.read_csv("./input/test_file.csv")

pictures = "./input/winner_ppt/bg.jpg"

# 字型設定
# 修改字體檔案位置
font_path = "/System/Library/Fonts/Supplemental/PingFang.ttc"
font_name = ImageFont.truetype(font_path, size=1200, index=1) # size=120，為字體大小，依需求調整
font_group = ImageFont.truetype(font_path, size=600, index=1) # size=60，為字體大小，依需求調整

# 輸出資料夾位置/輸出檔名
output_dir = "./output/winner_ppt"
os.makedirs(output_dir, exist_ok=True)
output_failed_file_name = "undone.csv"

# 顏色設定，依需求調整
black_color = "#000000"

# 置中處理
def center(name , group , font_name , font_group):
    img_width , img_high = pic.size
    text_name = draw.textbbox((0, 0), name, font=font_name)
    text_group = draw.textbbox((0, 0), group, font=font_group)
    name_x = (img_width - (text_name[2] - text_name[0])) // 2
    group_x = (img_width - (text_group[2] - text_group[0])) // 2
    name_y = (img_high - (text_name[3] - text_name[1])) // 2
    group_y = (img_high - (text_group[3] - text_group[1])) // 2
    name_position = draw.text((name_x, name_y+600), name, fill=black_color, font=font_name) # y座標可以再做調整
    group_position = draw.text((group_x,group_y-420), group, fill=black_color, font=font_group) # y座標可以再做調整

    return name_position , group_position

count = 0
for idx , (i, row) in enumerate(file.iterrows(),start=1):

    # [""]內為表格欄位名稱，依需求調整
    name = row["name"]
    group = row["group"]
    class_= row["class"]

    pic = Image.open(pictures).convert("RGBA")
    draw = ImageDraw.Draw(pic)

    if class_ == "得獎者" :
        name_position , group_position = center(name , group , font_name , font_group)
    else:
        continue

    output_path = os.path.join(output_dir, f"{idx+1}_{class_}_{name}.png")
    pic.save(output_path)
    count += 1

print(f"輸出完畢，預計輸出 {len(file)} 張圖片 | 實際輸出 {count} 張圖片")