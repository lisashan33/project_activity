# 專案活動 視覺物產出工作資源區

本專案方便企劃人員**大量輸出制式版的視覺物**，如識別證、座位貼紙、得獎者 PPT 等。需準備好資料 CSV 與背景圖片，即可自動生成對應視覺內容。

## 📄 輸入資料格式（CSV）

請先將資料轉為 `.csv` 格式，範例如下：

| name   | class    | seat  | group  |
|--------|----------|-------|--------|
| 王小明  | 得獎者    | A1-7  | 台北   |
| 陳大華  | 觀禮人員  | B10-4 | 親友   |
| 李璇    | 貴賓     | B1-7  | VIP    |
| OOO    | 媒體     | C19-3 | 媒體保留 |

---

## 📁 資料夾與檔案架構

```
.
├── scripts/
│   ├── 01-identification\_card.py    # 生成識別證
│   ├── 02-seat\_stickers.py          # 生成座位貼紙
│   └── 03-winner\_ppt.py             # 生成得獎者PPT
└── input/
├── test\_file.csv                    # 輸入的CSV檔案
├── identification\_card/             # 識別證背景圖片
│   ├── person.png                    # 觀禮人員
│   ├── visit.png                     # 貴賓
│   ├── media.png                     # 媒體
│   └── winner.png                    # 得獎者
├── seat\_stickers/                   # 座位貼背景圖片
│   ├── person.png                    # 觀禮人員      
│   ├── visit.png                     # 貴賓
│   ├── media.png                     # 媒體
│   └── winner.png                    # 得獎者
└── winner\_ppt/                      # 得獎者 PPT 背景
└── bg.jpg                            # 背景圖片

````

---

## 🚀 執行方式

### 安裝套件

請於 Terminal 執行以下指令安裝必要套件：

```bash
pip install Pillow pandas
````

### 程式參數設定

根據需求調整以下參數（於各 script 中）：

* `file`: 輸入 CSV 路徑
* `pictures`: 背景圖片資料夾路徑
* `font_path`: 字體檔案路徑
* `output_dir`: 輸出目錄

可調整內容包含：

* 字體大小與顏色
* 文字寫入位置座標

---

## ❗ 注意事項

* 執行後若有圖片生成失敗，可於 `./output/undone.csv` 中查看失敗紀錄並進行補救。
