from PIL import Image, ImageDraw, ImageFont
import pandas as pd
import os

from pathlib import Path

# 載入資料與圖片
# 修改識別身份
# 修改檔案路徑位置
file = pd.read_csv("./input/test_file.csv")

pictures = {
    "觀禮人員": Image.open("./input/seat_stickers/person.png").convert("RGBA"),
    "貴賓": Image.open("./input/seat_stickers/visit.png").convert("RGBA"),
    "媒體": Image.open("./input/seat_stickers/media.png").convert("RGBA"),
    "得獎者": Image.open("./input/seat_stickers/winner.png").convert("RGBA")
}

# 字型設定
# 修改字體檔案位置
font_path = "/System/Library/Fonts/Supplemental/PingFang.ttc"
font_name = ImageFont.truetype(font_path, size=120, index=1) # size=120，為字體大小，依需求調整
font_group = ImageFont.truetype(font_path, size=60, index=1) # size=60，為字體大小，依需求調整
font_seat = ImageFont.truetype(font_path, size=100, index=1) # size=100，為字體大小，依需求調整

# 輸出資料夾位置/輸出檔名
output_dir = "./output/seat_stickers"
os.makedirs(output_dir, exist_ok=True)
output_failed_file_name = "undone.csv"

# 相關參數設定
seat_position = (500, 80) # 座位寫入圖片的座標，依需求調整

# 顏色設定，依需求調整
color_name_group = "#FCE6E2" 
color_visit = "#AF2E26"
color_winner = "#D87093"
color_person = "#9370DB"
color_media = "#444444"

# 置中處理
def center(name , group , font_name , font_group):
    img_width = pic.size[0]
    text_name = draw.textbbox((0, 0), name, font=font_name)
    text_group = draw.textbbox((0, 0), group, font=font_group)
    name_x = (img_width - (text_name[2] - text_name[0])) // 2
    group_x = (img_width - (text_group[2] - text_group[0])) // 2
    name_position = draw.text((name_x, 385), name, fill=color_name_group, font=font_name)
    group_position = draw.text((group_x,305), group, fill=color_name_group, font=font_group)

    return name_position , group_position

count = 0
for i, row in file.iterrows():

    # [""]內為表格欄位名稱，依需求調整
    name = row["name"]
    group = row["group"]
    class_= row["class"]
    seat = row["seat"]

    if class_ not in pictures:
        print(f"第 {count+1} 筆 {name} 無參與身份！")

        # 將未正常輸出的圖片另存一份檢視
        df_undone = file.iloc[[i]]
        path = Path(f"{output_dir}/{output_failed_file_name}")
        if path.exists():
            df_undone.to_csv(path, index=False, header=False, encoding='utf-8-sig', mode="a") 
        else:
            df_undone.to_csv(path, index=False, header=True, encoding='utf-8-sig', mode="a")
        continue

    pic = pictures[class_].copy()
    draw = ImageDraw.Draw(pic)

    if class_ == "觀禮人員":
        draw.text(seat_position, seat, fill=color_person, font=font_seat)
    
    elif class_ == "媒體":
        draw.text(seat_position, seat, fill=color_media, font=font_seat)
    
    elif class_ == "貴賓":
        draw.text(seat_position, seat, fill=color_visit, font=font_seat)
        name_position , group_position = center(name , group , font_name , font_group)
    
    else:
        draw.text(seat_position, seat, fill=color_winner, font=font_seat)
        name_position , group_position = center(name , group , font_name , font_group)


    output_path = os.path.join(output_dir, f"{class_}_{seat}_{name}.png")
    pic.save(output_path)
    count += 1

print(f"輸出完畢，預計輸出 {len(file)} 張圖片 | 實際輸出 {count} 張圖片")