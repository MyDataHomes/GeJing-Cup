## 队伍信息

* **队伍名称***：MDG
* **队长姓名***：[胡琦](https://segmentfault.com/blog/huqi)


## 项目信息

---
 * 项目的简要介绍    
微信数据“爬取”，借助[uiautomator2](https://github.com/openatx/uiautomator2#stop-an-app)加Android真机实现。

 * 我们构建这一项目的动机和目标    
 自从微信暂停网页版，感觉获取微信的数据不太容易，希望借此机会能和各位大佬请教相关的技术问题，能学到解决问题的思路。我们的目标是从腾讯手中“拿回”自己的数据(PS:可能和游戏直播一样我们没有使用权，莫非创作权归……)，最终目标是做人人都能用的个人微信数据获取工具及基于微信数据开发的应用。

 * 我们的工作将会对MyDataHomes项目带来什么
 带来什么，目前来看应该还是未知数，现阶段应该是算我们从MyDataHomes索取和学习，希望通过我们自身的努力争取早日作出贡献！

 * 我们计划如何将该项目整合进MyDataHomes
暂无。正处于萌芽阶段，目前做的估计也有人做过了，走别人的路，让自己有路可走，管它呢！

* 关于项目的其他

### WeChat Crawlers
Just some crawlers for WeChat by [Appium](https://github.com/appium/appium).    
一次小小的尝试，借助跨平台自动化测试工具[Appium](https://github.com/appium/appium),实现微信相关的数据爬取，结合数据及数据分析实践朋友圈云词生成等应用。    
本仓库使用**windows**环境搭配**Android真机**来实现抓取特定**APP**如(微信)的数据，所以您可能需要安装**Python 3.7+**、**Java 8**、**Node.js 10+**已及**Android SDK**等必要环境或依赖，由于笔者工作需要使用**React Native**开发**APP**，所以已安装上述环境环境或依赖，此处不做过多的介绍。

### 效果
可查看**example**目录下文件，**wc_moment_list.txt**和**wc_moment_list_wordcloud.txt**分别为爬取的源数据和处理过后的数据，**result-XX.jpg**为输出的词云结果。**wc_moment_list_wordcloud_bak.txt**的生成是因为我发现源数据中存在一些无意义的数据，导致结果不准确，修正数据之后修改**needManual**配置，重新运行生成新的结果同时不存了上一次的结果。

|                  moments                                  |                    juejin                  |baidu                                     |
| ----------------------------------- | ------------------------------------------ |--------------- |
| ![moments](https://cdn.jsdelivr.net/gh/hu-qi/wechat-crawlers/example/result-1594507948130.jpg)    | ![juejin](https://cdn.jsdelivr.net/gh/hu-qi/wechat-crawlers/example/result-1594507943103.jpg)        |![baidu](https://cdn.jsdelivr.net/gh/hu-qi/wechat-crawlers/example/result-1594507938241.jpg)                   |


### 配置说明
```
[APPINFO]
platformName = 'Android'             # 平台
deviceName = '621da8320804'          # 设备名称，通过adb devices获取
appPackage = 'com.tencent.mm'        # APP包名
appActivity = '.ui.LauncherUI'       # APP入口
[WECHAT]
wechatUser = '******'                # 微信账号(最好手机号)
wechatPWd = '**********'             # 微信密码
wechatWho = 'Hugi66'                 # 目标用户微信账号
[WORDCLOUD]
needManual=                          # 是否需要人工修改源数据
stopwords=stopwords                  # 停词文件默认采用stopwords.txt
wordsCount=180                       # 显示词的数量，默认180
inputImg=juejin                      # 单张模板图片，默认juejin.jpg
fontFamily=simhei.ttf                # 字体，默认simhei.ttf
MODE=single                          # 生成模式，单张或全部，默认single，可选all
```

### wc_moments.py
朋友圈数据抓取。先借助[https://github.com/openatx/weditor](https://github.com/openatx/weditor)开启一个可在浏览器端访问**APP**内部节点的服务，通过获取节点、编辑atx脚本等为**APP**的一些自动化脚本做准备,再使用[uiautomator2](https://github.com/openatx/uiautomator2)来执行具体的流程并获取、储存数据。

### wc_wordcloud.py
词云生成。本项目中默认处理上一步获取的朋友圈数据，根据词频等生成关键词，也可单独使用。默认背景图片存放在**res/images**目录，单独使用时需新建**data**目录并存放**wc_moment_list.txt**，可指定背景图片或全部生成。

### TODO

- [√] 抓取朋友圈数据    
- [√] 生成关键词词云    
- [ ] 滑动拼图验证码    

### 公众号-胡琦

![huqi](https://www.fashaoge.com/img/weixinCode.jpg)



* **代码仓库地址***: [https://github.com/hu-qi/wechat-crawlers](https://github.com/hu-qi/wechat-crawlers)



## 联系方式

* **邮箱***：<huqi@gpdi.com>
* 电话号码：OOYpcR
* 微信号：Hugi66
