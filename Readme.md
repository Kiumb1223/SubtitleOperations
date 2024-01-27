# SubtitleOperation

<div align = 'center' font = 'bold'>
    <b>
   		 <a href='./Readme.md'>简体中文</a> | <a href='./Readme_en.md'>English</a>
    </b>
</div>

## Trivial Knowledge about Subtitle

> Reference:[失传技术研究所小讲堂 篇二十二：一文看懂视频外挂字幕 内嵌字幕 内封字幕的区别](https://post.smzdm.com/p/a07mwv7z/)

1. **外挂字幕**：视频本身没有字幕，字幕以字幕文件形式独立地挂在视频外面，需要软件支持。通常正规的播放器都可以挂在各种字幕。外挂字幕的格式也有很多，记录了视频的相关必要信息，字幕字体，起始时间，位置等信息都可以被解读。
2. **内封字幕**：把字幕封在视频内部的一种形式。字幕本身就在于视频中，不需要额外的外挂。播放器在播放的时候会自动挂载内封字幕。mkv格式视频 = mp4格式视频+自带字幕（内封字幕）**播放器在播放的时候会自动挂在内封字幕，当然也可以关掉它去找自己喜欢的字幕**
3. **内嵌字幕**：类似于把字幕焊在视频上，扣都扣不下来。

## Introduction

1. 该项目的应用场景有限，但是实现的思路极其简单。基本上就是利用`ffmpeg`的指令，然后设定输入文件和输出文件的路径，最后运行即可。

2. 运行该项目的时候，务必需要确认`ffmpeg`已经安装，且已经添加到环境变量中去（这样子即可使用`subprocess.call(cmd)`来调用设定的cmd）。

      :point_right:[download link of ffmpeg](https://www.ffmpeg.org/) or :point_right: [git仓库](./ffmpeg-6.1-full_build.7z)
## Updates
1. 在`SubtitleMerge`中添加了`SubtitleMerge_enc.py`文件，并同时更新其可执行文件。
   
   该文件旨在解决当字幕编码格式为`GB18030`时，压制视频字幕乱码的问题；解决方案为将字幕文件的编码格式转化为`UTF-8`。
## SubtitleExtract

> 从mkv视频中提取内封字幕

* ffmpeg指令：`ffmpeg  -i 1.mkv -map 0:s:0 1.srt`
* 将`SubtitleExtract.py`放置在视频文件夹下，直接运行即可;提取出来的字幕会保存在新建`Subtitles`文件夹中

## SubtitleFormatConvert

> 将srt格式字幕转化为ass格式字幕

* ffmpeg指令：`ffmpeg -i 1.srt 1.ass`
* 将`SubtitleFormatConvert.py`放置在字幕文件夹下，直接运行即可；提取出来的字幕会保存在新建`AssSubtitle`文件夹下

## SubtitleMerge

> 将ass字幕文件压制到视频中去

* ffmpeg指令：` ffmpeg -i 1.mkv -vf subtitles='1.ass' my.mkv`
* 可以将打包好的app直接放置在视频文件夹下，直接运行即可；合并的视频保存在新建`Merged`文件夹下

注：`SubtitleMerge.py`和`SubtitleMerge_simplified.py`的核心区别在于对于字幕文件的处理不同

## SubtitleRemove

> 将mkv视频中的内封字幕去除

* ffmpeg指令：`ffmpeg -i 1.mkv  -vcodec copy -acodec copy -sn 1-no-subs.mkv`
* 将`SubtitleRemove.py`放置在视频文件夹下，直接运行即可；剔除字幕后的视频保存在新建`SubtitleRemove`文件夹下

## SubtitleofMyLittlePony

> MLP的1-9季的中英字幕

- 中文字幕（缺少第四季）：[winddramon/Tidal-Fansub: Chinese Fansub for MLP by Team Tidal (github.com)](https://github.com/winddramon/Tidal-Fansub)
- 英文字幕：[Friendship is magic:heart:](./SubtitleofMLP)

## Reference

1. [Imyukehan/SubtitleMergeMKV: 将ass字幕并入mkv (github.com)](https://github.com/Imyukehan/SubtitleMergeMKV)

