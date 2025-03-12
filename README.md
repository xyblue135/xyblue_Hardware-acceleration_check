# xyblue_Hardware-acceleration_check
用来检测系统目前支持的硬件加速，如qsv，cuda，VAAPI ，OpenCL等
# 使用须知
需要有一定硬件编码解码基础和py基础，且对ffmpeg有了解

# 如何使用
首先确保你的电脑中安装了ffmpeg，因为此脚本是通过ffmpeg的各种操作来验证相关的硬件加速能否正常使用，你甚至可以自己编译一个ffmpeg，然后使用下述命令可以查看出当前系统上支持的硬件加速方法
```
ffmpeg -hwaccels
```
但有一点需要说明，木桶效应→ffmpeg显示的如qsv，不一定支持，比如直接迁移硬盘到另外一台无核显的主机上。
# 准备素材
准备一个mp4素材
命名为test_video.mp4，将以此为底进行转码测试
推荐用录屏软件就可以了。

# py开始
后者提供了更为详细的输出，前者则更为简洁直观
python xyblue_Hardware-acceleration_check.py
python xyblue_Hardware-acceleration_check_detail.py
![image](https://github.com/user-attachments/assets/dde3b130-baa9-40cd-b5d5-f511fd980b50)
![image](https://github.com/user-attachments/assets/0c7ceb2c-1859-4f9b-8899-1d15de8009d2)

# 跨平台
因为是基于ffmpeg去做的，所以理论上跨平台

