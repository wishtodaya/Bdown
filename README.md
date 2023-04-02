#Bdown
>Bilibili Video Downloader 是一个简单的 Python 脚本，用于下载 Bilibili 网站上的音频和视频，并将它们合并成一个 MP4 文件。请注意，根据 Bilibili 的服务条款，用户可能没有下载和分发其内容的许可。在使用此代码之前，请确保了解并遵守 Bilibili 的相关政策和法规。

##1.环境准备
确保您已安装以下依赖项：

Python 3.6 或更高版本
requests 库
ffmpeg 库
ffmpeg 命令行工具
###python库
可以通过以下命令安装所需的库：
```
pip install requests
pip install ffmpeg-python
```
###ffmpeg 命令行工具
ffmpeg 是一个非常强大且流行的跨平台开源多媒体处理工具，它提供了处理音频、视频和图像的各种功能，包括转码、剪辑、合并和过滤等。
要使用 ffmpeg 命令行工具，首先需要从其官方网站下载并安装：https://ffmpeg.org/download.html
##2.使用方法
在脚本中，将 url 变量更改为您希望下载的 Bilibili 视频的 URL。

打开命令行或终端，并导航到包含 bdown.py 文件的目录。
运行以下命令以启动下载和合并过程：
```
python bdown.py
```
脚本将下载音频和视频文件，然后将它们合并成一个 MP4 文件。合并后的文件将保存在当前用户桌面上的 bilibili\concat 文件夹中。

