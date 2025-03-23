# sbs_tab_converter
使用前请先安装最新版FFmpeg，安装地址[FFmpeg](https://ffmpeg.org/download.html)
## 用途
将3D视频转换为目标格式，并保存在原目录下
## 参数说明
-f 待转换文件所在位置
-s 转换前文件的格式，可选的值为["sbsl", "sbsr", "sbs2l", "sbs2r", "abl", "abr", "ab2l", "ab2r"]
-t 转换后文件的目标格式，可选的值为["sbsl", "sbsr", "sbs2l", "sbs2r", "abl", "abr", "ab2l", "ab2r"]
### 例：
```bash
python sbs_tab_converter.py -f test.m2ts -s sbsl -t sbs2l
```