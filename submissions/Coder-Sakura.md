## 队伍信息

---

* 队伍名称：Coder-Sakura
* 队长姓名：张育豪（Coder-Sakura）
* 项目地址：[PixiC](https://github.com/Coder-Sakura/PixiC) v2.1.0
* 项目Wiki及教程：[Wiki](https://github.com/Coder-Sakura/PixiC/wiki)、[Blog](http://00102400.xyz/blog/2020/06/24/pixic-bu-shu/)



## 项目信息

---

### PixiC是什么？

​		PixiC是一个以[Pixiv](https://www.pixiv.net/)插画交流虚拟社区进行开发的爬虫项目，旨在简单配置之后，敲下回车键，可以下载关注用户及收藏的作品（数据）。

​		PixiC主要功能是绕过Pixiv的Google V3验证，下载Chrome浏览器上登录的Pixiv账号的关注画师与收藏的作品（包括单图多图动图），同时PixiC支持下载数据入库、开启`API`功能、收藏数筛选下载等功能。

​		PixiC采用多进程+爬虫模块实现多种功能，支持自定义拓展；爬虫模块内使用多线程进行数据获取、过滤、处理、存储。

​		目前PixiC的功能模块有三个，BM模块（下载收藏），CW模块（下载关注画师作品）及API模块。其中BM（bookmark.py）就是根据原型爬虫CW（crawler.py）二次开发拓展出来的。

​		通过配置文件，用户可自定义爬虫模块的启用与其他设置。

​		配置项包括但不限于：各个功能模块的开关启用，爬虫模块轮询周期时长设置，API信息，作品下载最低收藏数，数据库模块开关的启用，数据库连接信息，下载目录等等。



## 联系方式

* 邮箱：1508015265@qq.com
