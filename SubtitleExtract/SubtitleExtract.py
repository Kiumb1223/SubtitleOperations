# -*- encoding: utf-8 -*-
'''
@File    :   SubtitleExtract.py
@Time    :   2024/01/22 18:57:48
@Author  :   Kiumb 
@Description :   遍历当前目录下的所有mkv视频文件，提取内封字幕到Subtitles文件夹中去

需要先把视频按照S01E01的格式进行重命名，再进行提取字幕

提取字幕指令：  ffmpeg  -i 1.mkv -map 0:s:0 1.srt
'''

import os 
import re 
import subprocess

current_dir = '.\\'
output_dir  = os.path.join(current_dir,'Subtitles')
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

vedio_path = [] # 记录视频文件的路径
ass_path   = [] # 记录保存字幕文件的路径

# 对视频重命名
for vedio in os.listdir(current_dir):
    if vedio.endswith('.mkv'):
        pattern = r'S\d+(E\d+)+'
        match = re.search(pattern,vedio)
        if match:
            # 重命名
            preview_vedio_path = os.path.join(current_dir,vedio)
            rename_vedio_path  = os.path.join(current_dir,f"{match.group()}.mkv")
            os.rename(preview_vedio_path,rename_vedio_path)

            vedio_path.append(rename_vedio_path)
            ass_path.appent(os.path.join(output_dir,f"{match.group()}.ass"))

for idx in range(len(vedio_path)):
    cmd = ['ffmpeg','-i',vedio_path[idx],'-map','0:s:0',ass_path[idx]]
    subprocess.call(cmd)