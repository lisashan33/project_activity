from PIL import Image, ImageDraw, ImageFont
import pandas as pd
import os

from pathlib import Path

# 載入資料與圖片
# 修改識別身份
# 修改檔案路徑位置
file = pd.read_csv("./input/test_file.csv")

pictures = {
    "觀禮人員": Image.open("./input/identification_card/person.png").convert("RGBA"),
    "貴賓": Image.open("./input/identification_card/visit.png").convert("RGBA"),
    "媒體": Image.open("./input/identification_card/media.png").convert("RGBA"),
    "得獎者": Image.open("./input/identification_card/winner.png").convert("RGBA")
}

# 字型設定
# 修改字體檔案位置
font_path = "/System/Library/Fonts/Supplemental/PingFang.ttc"
font_name = ImageFont.truetype(font_path, size=96, index=1) # size=96，為字體大小，依需求調整
font_seat = ImageFont.truetype(font_path, size=36, index=1) # size=36，為字體大小，依需求調整

# 輸出資料夾位置/輸出檔名
output_dir = "./output/identification_card"
os.makedirs(output_dir, exist_ok=True)
output_failed_file_name = "undone.csv"

# 相關參數設定
seat_position = (36, 405) # 座位寫入圖片的座標，依需求調整
white_color = "#FFFFFF"
black_color = "#000000"

count = 0
for i, row in file.iterrows():

    # [""]內為表格欄位名稱，依需求調整
    name = row["name"]
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

    # 通常得獎者需顯示名字，並置中處理
    # 如果不需要則把這段刪除
    if class_ == "得獎者":
        img_width = pic.size[0]
        text_name = draw.textbbox((0, 0), name, font=font_name)
        name_x = (img_width - (text_name[2] - text_name[0])) // 2
        draw.text((name_x, 200), name, fill=white_color, font=font_name)

    # 所有人都印座位
    draw.text(seat_position, seat, fill=black_color, font=font_seat)

    output_path = os.path.join(output_dir, f"{seat}_{name}.png")
    pic.save(output_path)
    count += 1

print(f"輸出完畢，預計輸出 {len(file)} 張圖片 | 實際輸出 {count} 張圖片")