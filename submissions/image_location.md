* **队伍名称***：白夜追凶
* **队长姓名***：白夜



# 项目信息

## 简要介绍

本项目着重于抓取到目标目录中所有的的带有地理位置标记的图片，并以可视化的方式来展现。

## 项目目标

- 可针对任意目录进行遍历
- 可解析图片的exif信息
- 可从exif信息中提取到相应的拍摄设备信息，定位坐标
- 可根据不同的拍摄时间模拟行进轨迹
- 可通过相关第三方API获得坐标大概地理位置名称
- 以卡片方式在地图上展示单个结果，并辅助以标注源文件夹信息、图片概要、地理位置、拍摄设备等
- 地图背景可选夜间风格

## 项目意义

- 日常生活中，我们不免得会将一些带有地理位置的图像上传至网路，而存在暴露个人位置及行程的风险。而本项目则可以辅助于检测相关风险。

- 个人对于自身历史相册的分析处理工具

- 可以作为一款社工辅助工具


## 项目创新

- 可扩展成一个 `github Action` 用于对项目中所带图片的检测

## 项目效果

👯一次女装图集的分析结果

<video controls="controls">
    <source type="video/mp4" src="https://raw.githubusercontent.com/singsoul/image_location/master/exif-finder/media/%E9%A1%B9%E7%9B%AE%E4%BB%8B%E7%BB%8D.mp4"></source>
    <p>Your browser does not support the video element.</p >
</video>




图集项目地址: [https://github.com/komeiji-satori/Dress](https://github.com/komeiji-satori/Dress)

![media/demo.jpg](https://raw.githubusercontent.com/singsoul/image_location/master/exif-finder/media/demo.jpg)





## 结果案例:

```json
[

    {
        "new_path": "images/34.jpg",
        "path":"xxxx2.jpg",
        "date": "2016-06-21 23:10:27",
        "gps": [
            34.78708,
            113.63151497222222
        ],
        "alt": [
            0,
            "海平面"
        ],
        "soft": "gemini-user 6.0 MRA58K V7.3.10.0.MAACNDD release-keys",
        "model": "MI 5",
        "make": "Xiaomi",
        "address": "河南省郑州市金水区南阳新村街道第九人民医院家属院"
    },
    {
        "new_path": "images/0.jpg",
        "path":"xxxx1.jpg",
        "date": "2016-07-20 12:21:15",
        "gps": [
            47.362586972222225,
            123.91117858333334
        ],
        "alt": [
            0,
            "海平面"
        ],
        "soft": "Adobe Photoshop CC 2018 (Windows)",
        "model": "m2 note",
        "make": "Meizu",
        "address": "黑龙江省齐齐哈尔市梅里斯达斡尔族区梅里斯乡浏园"
    }
 
]

```


***代码仓库地址***: https://github.com/singsoul/image_location


# 联系方式 

***邮箱***：824300438@qq.com