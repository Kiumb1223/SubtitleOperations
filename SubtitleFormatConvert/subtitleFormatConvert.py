# -*- encoding: utf-8 -*-
'''
@File    :   subtitleFormatConvert.py
@Time    :   2024/01/22 20:43:33
@Author  :   Kiumb 
@Description :   将srt格式的字幕文件转化为ass格式文件，同时根据需要将ass名字命名一下

ffmpeg命令 ffmpeg -i 1.srt 1.ass 

srt 命名格式  季数x集数
'''

import os 
import subprocess

current_dir = '.\\'
output_dir  = os.path.join(current_dir,'AssSubtitle')
if not os.path.exists(output_dir):
    os.makedirs(output_dir)
for srt in os.listdir(current_dir):
    if srt.endswith('.srt'):
        temp = srt.split('.')[0].split('x')    # ['08','01']
        ass_name = f'S{temp[0]}E{temp[1]}.ass'
        ass_path = os.path.join(output_dir,ass_name)
        cmd = ['ffmpeg','-i',srt,ass_path]
        subprocess.call(cmd)