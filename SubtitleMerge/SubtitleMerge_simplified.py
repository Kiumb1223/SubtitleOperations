# -*- encoding: utf-8 -*-
'''
@File    :   SubtitleMerge_simplified.py
@Time    :   2024/01/23 18:18:08
@Author  :   Kiumb 
@Description :   将Subtitles文件夹中的字幕压制到视频中,保存到Merged文件夹中

文件树结构 
|----- mkv视频     # vedios_dir
|------Subtitles
        |-----  ass字幕

视频和字幕文件名字相同

Debug info :
    cmd = ['ffmpeg', '-i', '.\\S08E25.mkv', '-vf', 'subtitles=.\\Subtitles\\S08E25.ass', '.\\Merged\\S08E25.mkv']
    subprocess 总是会运行报错
    
    Solutions: 把字幕文件搬移到vedios_dir，然后调用，之后删除该字幕文件
    但是  ffmpeg -i S08E01.mkv -vf subtitles='.\\Subtitles\\S08E01.ass' .\\Merged\\1.mkv 是能成功在命令行运行的
'''
# import os 
# import re
# import subprocess


# # vedios_dir   = '.\\'   
# # subtitle_dir = os.path.join(vedios_dir,'Subtitles') 
# # output_dir = os.path.join(vedios_dir,'Merged')
# # if not os.path.exists(output_dir):
# #     os.makedirs(output_dir)
# # for vedio in os.listdir(vedios_dir):
# #     if vedio.endswith('.mkv') or vedio.endswith('.mp4'):
# #         vedio_path  = os.path.join(vedios_dir,vedio)
# #         ass_path    = os.path.join(subtitle_dir,vedio.replace('.mkv','.ass'))
# #         output_path = os.path.join(output_dir,vedio)
# #         # print(ass_path)
# #         cmd = ['ffmpeg','-i',vedio_path,'-vf',f"subtitles={ass_path}",output_path]
# #         print(cmd)
# #         subprocess.call(cmd)

##  debug info
import os 
import shutil
import subprocess


vedios_dir   = '.\\'   
subtitle_dir = os.path.join(vedios_dir,'Subtitles') 
output_dir = os.path.join(vedios_dir,'Merged')
if not os.path.exists(output_dir):
    os.makedirs(output_dir)
for vedio in os.listdir(vedios_dir):
    if vedio.endswith('.mkv') or vedio.endswith('.mp4'):
        vedio_path  = os.path.join(vedios_dir,vedio)
        ass_path    = os.path.join(subtitle_dir,vedio.replace('.mkv','.ass'))

        # 搬移字幕
        # ass_move_path = os.path.join(vedios_dir,vedio.replace('.mkv','.ass'))
        ass_move_path = vedio.replace('.mkv','.ass')
        # shutil.move(ass_path,ass_move_path)   类似于剪切操作
        shutil.copyfile(ass_path,ass_move_path)
        output_path = os.path.join(output_dir,vedio)
        cmd = ['ffmpeg','-i',vedio_path,'-vf',f"subtitles='{ass_move_path}'",output_path]
        print(cmd)
        subprocess.call(cmd)
        # 删除搬移之后的字幕
        os.remove(ass_move_path)
