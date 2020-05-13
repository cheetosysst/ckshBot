# ckshBot 臺北市成功高中公告爬蟲

## 目的
由於網路中心不會直接跟我們通知學校要停電、學網要維護、他不小心踩掉伺服器電源…等訊息，所以想說要用爬蟲直接在有新公告時通知社團網管。

## 說明
### 結構
```bash
botSchool
├── main.py				# 主要檔，使用時以 python3 執行
├── README.md			# 沒有人會認真讀的東西
└── school				# 這個套件裡面包含大部分會用到的工具類別
    ├── __init__.py		# 不是很重要的東西
    ├── school.py		# 取得 html
    └── soup.py 		# 處裡 html
```
### 用法
目前處在開發階段， main.py 的用法之後會有很多變動，使用前請多看幾眼 readme.md。
```bash
# 相依安裝
pip3 install bs4

# 執行
python3 main.py
```
執行後會看到一個叫做 data.json 的新檔案
這個程式目前只做的到提供資料格式範本做為開發參考

## 同性質專案
### [cksh-post](https://github.com/simba-fs/cksh-post)
32 屆網管 simba-fs 開發的類似專案，使用 node.js。

## 注意事項
- .gitignore 檔案來自 GitHub 範例
- 現階段執行時須先刪除 data.json，才能夠正常執行
- 預計會進行幾個禮拜的長時間測試，但測試成功的前提是網路中心有發文
