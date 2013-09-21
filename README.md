# Web文件分享

![](https://github.com/blahgeek/personal-file-sharing-center/raw/master/img/screenshot.png)

类似SimpleHTTPServer的web文件分享页面，但是：

- 可以配置很多个文件夹（类似Dropbox的分享）
- 更好的UI
- 支持上传（可选）
- 支持下载所有文件（ZIP）

使用：

使用`web.py`写的，直接运行`python index.py [port]`运行网页服务器。

之后，为了编辑分享的文件夹列表，使用了`sqliteboy`编辑，运行`python sqliteboy.py main.db [PORT]`，
在web页面上插入要分享的文件夹的名字、路径和是否可以上传。

