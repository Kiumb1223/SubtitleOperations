# -*- encoding: utf-8 -*-
'''
@File    :   SubtitleMerge_enc.py
@Time    :   2024/01/27 14:32:05
@Author  :   Kiumb 
@Description :   在使用ffmpeg合并字幕过程中，会遇到 Invalid UTF-8 in decoded subtitles text; maybe missing -sub_charenc option 
                 究其原因是 该字幕的编码为GB2312，而ffmpeg合并时读取字幕文件是按照UTF-8进行读取的，所以会出现中文乱码的情况
                 解决方案则是 将该字幕编码格式另存为UTF-8，再进行下一步的合并

                 更新了ffmpeg合并字幕的指令 
                 ffmpeg -i 1.ass -i 1.mkv -c copy 2.mkv

                 同时合并之后，会删掉原本的视频和字幕文件（主要是我的存储太小了，保存不了两份视频）

                 
'''

import os 
import re
import shutil
import subprocess

def match_vedio_subtitle(vedio,subtitle):
    '''
    @Description : 匹配视频以及字幕 
                   适配 S01.E01 以及S01E01的情况，但统一返回S01E01的格式名字
    @Parameter   : vedio    - 视频名字
    @Parameter   : subtitle - 字幕名字
    @Return      : 匹配成功则返回 修正之后的字符；否则返回None
    '''
    pattern  = r'(S\d+)\.?(E\d+)'  
    # re.match是字符串的开始处匹配的
    # re.search会扫描整个字符串
    match1   = re.search(pattern,vedio)
    match2   = re.search(pattern,subtitle)
    # 需要额外处理  一个是S01.E01  另一个是S01E01 的特殊情况
    str1     =  re.sub(pattern,r'\1\2',match1.group())   
    str2     =  re.sub(pattern,r'\1\2',match2.group())   
    if match1 and match2 and str1 == str2:
        return str1 
    else:
        return None

current_dir = '.\\'
temporary_output_dir = os.path.join(current_dir,'merged')


if not os.path.exists(temporary_output_dir):
    os.mkdir(temporary_output_dir)

for vedio in os.listdir(current_dir):
    if vedio.endswith('.mkv'):

        for subtitle in os.listdir(current_dir):
            if (subtitle.endswith('.ass') or subtitle.endswith('.srt')):                
                rename = match_vedio_subtitle(vedio,subtitle)
                if rename : # 匹配字幕和视频文件
                    
                    preview_vedio_path    = os.path.join(current_dir,vedio)
                    preview_subtitle_path = os.path.join(current_dir,subtitle)

                    try:
                        # 变换编码格式
                        with open(preview_subtitle_path,'r',encoding='GB18030') as f:
                            content = f.read()
                        with open(preview_subtitle_path,'w',encoding='UTF-8')   as f:
                            f.write(content)
                    except UnicodeDecodeError:
                        pass
                    
                    rename_vedio_path     = os.path.join(current_dir,rename+'.mkv')
                    rename_subtitle_path  = os.path.join(current_dir,rename+f".{subtitle.split('.')[-1]}")
                    
                    try:
                        os.rename(preview_vedio_path,rename_vedio_path)
                        os.rename(preview_subtitle_path,rename_subtitle_path)
                    except:
                        pass

                    cmd = ['ffmpeg','-i',rename_vedio_path,'-i',rename_subtitle_path,'-c','copy',os.path.join(temporary_output_dir,rename+'.mkv')]

                    subprocess.call(cmd)

                    # 删除 源视频和源字幕文件
                    os.remove(rename_vedio_path)
                    os.remove(rename_subtitle_path)

# 完成所有字幕压制之后，需要把temporary_output_dir中的视频搬移到current_dir中去
for vedio  in os.listdir(temporary_output_dir):
    source       = os.path.join(temporary_output_dir,vedio)
    destination  = os.path.join(current_dir,vedio)
    shutil.move(source,destination)

os.rmdir(temporary_output_dir)