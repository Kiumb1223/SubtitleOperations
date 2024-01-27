# SubtitleOperation

<div align = 'center' font = 'bold'>
    <b>
            <a href='./Readme.md'>简体中文</a> | <a href='./Readme_en.md'>English</a>
    </b>
</div>

## Trivial Knowledge about Subtitle

> Reference:[失传技术研究所小讲堂 篇二十二：一文看懂视频外挂字幕 内嵌字幕 内封字幕的区别](https://post.smzdm.com/p/a07mwv7z/)

1. **Softcoded Subtitles**: There are subtitles that not are not part of the video itself and are independently attached as subtitle files, requiring software support. Most standard players can support various subtitle formats. These subtitles come in many formats , containing essential video information , subtitle fonts, start times, positions,etc.
2. **Embeded Subtitles**: This refers to subtitles that are encapsulated within the video file. The subtitles are inherently part of the video, eliminating the need for external files.Players automatically load these subtitles during playback. For example, an MKVformat video is essentially an MP4format video with embedded subtitles.**Players automatically load these subtitles, but they can also be turned off in favor preferred ones**
3. **Hardcoded Subtitles**: Similiar to embedding subtitles onto the video, these are permanently affixed and cannot be removed.

## Introduction

1. The application scenarios of this project are limited, but the implementation approach is extremely simple. It primarily utilizes the `ffmpeg` command and sets the inputs file and output file paths, and then execute it.

1. When running this project, it is crucial to ensure that `ffmpeg` is installed and added to the environment variables(this allows the use of `subprocess.call(cmd)` to invoke the set command).

   :point_right:[download link of ffmpeg](https://www.ffmpeg.org/) or :point_right: [download Link in the git repository ](./ffmpeg-6.1-full_build.7z)

## Updates
1. Added the `SubtitleMerge_enc.py` file to `SubtitleMerge`, and updated its executable files simulaneously.

   This file aims to address the issue of grabled video subtitles when the subtitle encoding format is `GB18030`;the solution involves converting the subtitle tile encoding format to `UTF-8`
## SubtitleExtract

> Extracting Embedded Subtitles from MKV Videos

* ffmpeg Command：`ffmpeg  -i 1.mkv -map 0:s:0 1.srt`
* Place `SubtitleExtract.py ` in the video folder and run it directly; the extracted subtitles will be saved in the newly created `Subtitles` folder

## SubtitleFormatConvert

> 将srt格式字幕转化为ass格式字幕
>
> Convert SRT Format Subtitles to ASS Format

* ffmpeg Command：`ffmpeg -i 1.srt 1.ass`
* Place `SubtitleFormatConver.py` in the subtitles folder and run it directly; the converted subtitles will be saved in the newly created `AssSubtitle` folder

## SubtitleMerge

> Embedding ASS Subtitle Files into Videos 

* ffmpeg Command：` ffmpeg -i 1.mkv -vf subtitles='1.ass' my.mkv`
* The packedaged app can be placed directly in the video folder and run; the merged video will be saved in the newly created `Merged` folder

**Note**:The core difference between `SubtitleMerge.py` and `SubtitleMerge_simplified.py` lies in the different handing of subtitle files.

## SubtitleRemove

> 将mkv视频中的内封字幕去除
>
> Removing Embeded Subtitles from MKV Videos

* ffmpeg Command：`ffmpeg -i 1.mkv  -vcodec copy -acodec copy -sn 1-no-subs.mkv`
* Place `SubtitleRemove.py` in the video folder and run it directly; the video with subtitles removed will be saved in the newly created `SubtitleRemove` folder

## SubtitleofMyLittlePony

> Chinese and English Subtitle for Season 1-9 of My Little Pony 

- **Chinese Subtitle(missing Season 4)**：[winddramon/Tidal-Fansub: Chinese Fansub for MLP by Team Tidal (github.com)](https://github.com/winddramon/Tidal-Fansub)
- **English Subtitle**:[Friendship is magic:heart:](./SubtitleofMLP)

## Reference

1. [Imyukehan/SubtitleMergeMKV: 将ass字幕并入mkv (github.com)](https://github.com/Imyukehan/SubtitleMergeMKV)

