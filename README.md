# ckshBot 臺北市成功高中公告爬蟲
本來名字跟 repo 名一樣，但後來想改但不想丟失 git 的紀錄就算了…

## 目的
由於網路中心不會直接跟我們通知學校要停電、學網要維護、他不小心踩掉伺服器電源…等訊息，所以想說要用爬蟲直接在有新公告時通知社團網管。

## 說明
### 結構
```
botSchool
├── main.py 主要檔，使用時以 python3 執行
├── README.md 沒有人會認真讀的東西
└── school 這個套件裡面包含大部分會用到的工具類別
    ├── __init__.py
    ├── school.py 取得 html
    └── soup.py 處裡 html
```
### 用法
目前處在開發階段， main.py 的用法之後會有很多變動，使用前請多看幾眼 readme.md。
```bash
# 相依安裝
pip3 install bs4

# 執行
python3 main.py
```

## 同性質專案
### [cksh-post](https://github.com/simba-fs/cksh-post)
32 屆網管 simba-fs 開發的類似專案，使用 node.js。

## 注意事項
- .gitignore 檔案來自 GitHub 範例
