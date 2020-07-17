# 队伍信息

***队伍名称***：日常咸鱼队

***队长姓名***：星辰


# 项目信息


<p align="center">
<img src="https://github.com/aoii103/Sharingan/blob/master/medias/main.gif?raw=true" />
    <h1 align="center" >Sharingan</h1>
    <p align="center">我们将尽可能得从社交媒体中寻找您的基本可见足迹</p>
        <p align="center">
    <a href="https://app.codacy.com/manual/aoii103/Sharingan?utm_source=github.com&utm_medium=referral&utm_content=aoii103/Sharingan&utm_campaign=Badge_Grade_Dashboard"><img src="https://api.codacy.com/project/badge/Grade/f00d1d69a99346038d14df4bec303034"/></a>
    <a target="_blank" href="https://www.python.org/downloads/" title="Python version"><img src="https://img.shields.io/badge/python-%3E=_3.8-green.svg"></a>
    <a target="_blank" href="LICENSE" title="License: MIT"><img src="https://img.shields.io/badge/License-MIT-blue.svg"></a>
</p>

## 项目意义

曾有项目用于针对单个账号来搜集是否在各个站点注册过。

但对于社工人员来说，这只是第一步，下一步即针对搜索结果进行进一步数据搜集。

而本项目则是解决该痛点，通过简单的规则添加即可做到对目标页基础信息的采集

你所需要掌握的仅仅是基本的`python3`功底及`css`选择器知识。

## 项目进程

已在第一时间开源，并在持续完善站点规则器中。

1. 目前已支持近 `500` 多个站点的账户存在性判断、标题截取。

2. 获取有人会问这东西不是上一个特性只要一个 `for` 循环就能搞定么。确实，但我的想法没这么简单

3. 现在正每天花时间完善规则代码，使其能够抓取更多站点

4. 但站点默认数据结构如下，当然后续也会增加重要字段

    - title 网页标题
    - name 个人昵称
    - sign 可能存在的个性签名
    - age 可能存在的年龄
    - gender 可能存在的行吧
    - avatar 使用的头像b64
    - locations 地理位置
    - websites 站点
    - extra 其他结构信息

5. 结果导出默认为json，正在开发html报告导出功能

6. 后续会上传到 pypi 实现模块化



## 案例用法

```sh

cd sharingan

python3 worker.py --name=blue

```

![](https://github.com/aoii103/Sharingan/blob/master/medias/use.gif?raw=true)

## 添加新站点

我有曾考虑过使用 `json` 作为站点的配置文件，但后来还是把它写在了 `extract.py`中

我们需要做的是在 `class Extractor` 下添加如下方法，其中 `upload` 方法中存放对应站点的基础配置

可选配置详见 [`models.py`](https://github.com/aoii103/Sharingan/blob/master/sharingan/models.py#L25)


```python

    @staticmethod
    def __example() -> Generator:
        """
            1. <-- yield your config first
            2. --> then got your datas back 
            3. <-- finally, yield the extracted data back
        """
        T = yield from upload(
            **{
                "url": "http://xxxx", 
            }
        )

        T.name = T.html.pq('title').text()
        ...

        yield T

```

## 单项测试

偶尔我们在编写添加新站点后需要进行测试

就可以用到如下代码，例如我们要测试 `twitter`

```bash
python3 worker.py --singel=twitter --name=larry  
```

## 通过 sherlock 创建站点

首先我们运行如下代码

```bash
python3 common.py
```

然后它将创建一个叫`templates.py`的python脚本


```python
    @staticmethod
    def site_2Dimensions():
        T = yield from upload(url='''https://2Dimensions.com/a/{}''',)

        T.title = T.html.pq('title').text()
        yield T
        
    @staticmethod
    def site_3dnews():
        T = yield from upload(url='''http://forum.3dnews.ru/member.php?username={}''',error_type='text',error_msg='''Пользователь не зарегистрирован и не имеет профиля для просмотра.''',)

        T.title = T.html.pq('title').text()
        yield T

    ...
```

我们将其中的代码替换到 `extract.py`的相应位置即可


## TODO

- HTML格式化输出



***代码仓库地址***: https://github.com/aoii103/Sharingan

# 联系方式

***邮箱***：ak47__98k@163.com
