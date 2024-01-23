# -*- encoding: utf-8 -*-
'''
@File    :   SubtitleRemove.py
@Time    :   2024/01/22 22:54:23
@Author  :   Kiumb 
@Description : 将mkv视频剔除内封字幕，并将剔除之后的视频保存到SubtitleRemove文件夹中

ffmpeg 指令  ffmpeg -i a.mkv  -vcodec copy -acodec copy -sn 1-no-subs.mkv
-vcodec 视频编码  直接copy 
-acodec 音频编码  直接copy
-sn     去除字幕

文件树结构
|
---- Season 1
|       |----- S01E01.mkv
|       ------- ......  
|--- Season 2
|       |----- S02E02.mkv
|       ------ .......
.....
'''

import os 
import subprocess


main_dir      = '.\\'
secondary_dir_list = [f'Season {i+1}' for i in range(9)]
output_dir    = 'SubtitleRemove'

for secondary in secondary_dir_list:   
    current_dir = os.path.join(main_dir,secondary)
    result_path = os.path.join(current_dir,output_dir)
    if not os.path.exists(result_path):
        os.makedirs(result_path)
    # print(current_dir+'     '+result_path)
    for vedio in os.listdir(current_dir):
        if vedio.endswith('.mkv'):
            result_vedio_path = os.path.join(result_path,vedio)
            current_vedio_path = os.path.join(current_dir,vedio)
            cmd = ['ffmpeg','-i',current_vedio_path,'-vcodec','copy','-acodec','copy','-sn',result_vedio_path]
            # print(result_vedio_path+'     '+current_vedio_path)
            subprocess.call(cmd)

