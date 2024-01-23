# -*- encoding: utf-8 -*-
'''
@File    :   SubtitleMerge.py
@Time    :   2023/11/12 20:30:29
@Author  :   Kiumb 
@Description :  给当前目录下的所有mkv或mp3视频文件添加字幕，并输出到merged文件夹中
                匹配字幕并给视频与字幕进行重命名
'''
import os 
import re
import subprocess


current_dir = '.\\'
output_dir = os.path.join(current_dir,'merged')
if not os.path.exists(output_dir):
    os.makedirs(output_dir)
# 遍历current_dir文件夹中的mkv、mp4文件
vedios_path = []
ass_path    = []
output_path = []
for vedio in os.listdir(current_dir):
    if vedio.endswith('.mkv') or vedio.endswith('.mp4'):
        # 匹配ass文件
        # 匹配规则为  vedio的前缀 + 乱七八糟字符 + .ass
        prefix_vedio =vedio.split('\\')[-1].rsplit('.',1)[0]
        # 匹配视频中的S数字E数字，重命名
        pattern = r'S\d+(E\d+)+'
        match = re.search(pattern,vedio)
        if match: # 定位正确的视频名字
            for ass in os.listdir(current_dir):
                if ass.startswith(prefix_vedio) and ass.endswith('.ass'):
                    # print(match.group())
                    preview_vedio_path = os.path.join(current_dir,vedio)
                    rename_vedio_path  = os.path.join(current_dir,f"{match.group()}.mkv")
                    preview_ass_path = os.path.join(current_dir,ass)
                    rename_ass_path  = f"{match.group()}.ass"
                    os.rename(preview_vedio_path,rename_vedio_path)
                    os.rename(preview_ass_path,rename_ass_path)
                    vedios_path.append(rename_vedio_path)
                    ass_path.append(rename_ass_path)
                    output_path.append(os.path.join(output_dir,f'{match.group()}.mkv'))


# # vedios_path 与 ass_path 的长度相同
for idx in range(len(vedios_path)):
    cmd = ['ffmpeg','-i',vedios_path[idx],'-vf',f"subtitles='{ass_path[idx]}'",output_path[idx]]
    subprocess.call(cmd)
