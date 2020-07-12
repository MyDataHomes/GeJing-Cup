## 队伍信息

* **队伍名称***：加载中
* **队长姓名***：宋后宇


## 项目信息

项目的简要介绍：

> github_backups / github 备份： 用于备份github仓库的源码，采用多线程下载到本地磁盘

你们构建这一项目的动机和目标：

> 公司需要定期备份 github 仓库，由于项目数量比较多，因此采用 JxBrowers 登录 github 抓取项目数据，然后批量下载到公司服务器保存。

你们的工作将会对MyDataHomes项目带来什么：

> 增加一个小小的案例，说不定也有需要备份github源码的小伙伴会用到...

你们计划如何将该项目整合进MyDataHomes：

> 可以写一个py版的整合到 MyDataHomes

项目运行环境：

> jdk8、git

运行项目

`具体运行流程可查看博客: ` https://shaines.cn/blog/detail/1282338441662246912

**1.** clone 项目 

```
git clone https://github.com/HouYuSource/java_spider.git
```

**2. 使用idea打开项目**

把 shaines-jxbrowser-6.23.1-min.jar 添加到资源库中

**3. 运行GithubSpider#Main**

登录：程序自动打开github登录界面，输入密码登录

获取仓库：程序自动跳转到仓库地址，进行准备批量下载

控制台输入：控制输出下载信息

**4. 查看下载文件**

> 备份文件默认保存在运行项目目录下:$/temp/github_backups
> 提示：由于 github 在国外，因此网络方面可能不是很好，如果运行起来下载文件比较慢或者打开页面都比较慢的话，那只能从优化自己的网络，提高体验了。。。

* **代码仓库地址***: https://github.com/HouYuSource/java_spider.git

## 联系方式


* **邮箱***：for.houyu@qq.com


