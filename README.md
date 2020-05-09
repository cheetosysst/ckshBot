# ckshBot 臺北市成功高中公告爬蟲
本來名字跟 repo 名一樣，但後來想改但不想丟失 git 的紀錄就算了…

## 目的
網路中心不會直接跟我們通知學校要停電、學網要維護、他不小心踩掉伺服器電源…等訊息，所以想說要用爬蟲直接在有新公告時通知社團網管。

## 說明
### 結構
```
├── main.py 主要檔，使用時以 python3 執行
├── README.md 沒有人會認真讀的東西
└── school 這個套件裡面包含大部分會用到的工具類別
    ├── __init__.py
    ├── school.py 取得 html
    └── soup.py 處裡 html
```
### 用法
(有待補齊)

## 同性質專案
### [cksh-post](https://github.com/simba-fs/cksh-post)
32 屆網管 simba-fs 開發的類似專案，使用node.js。
