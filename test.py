from pytube import YouTube, Playlist
import os
import subprocess

import moviepy.editor as mp
import re

# def download_video(addr):
#     yt = YouTube(addr).streams.filter(mime_type="audio/mp4").first()
#     tgt_folder = './mp3'
#     yt.download(tgt_folder)
#     for file in [n for n in os.listdir(tgt_folder) if re.search('mp4',n)]:
#         full_path = os.path.join(tgt_folder, file)
#         output_path = os.path.join(tgt_folder, os.path.splitext(file)[0] + '.mp3')
#         clip = mp.AudioFileClip(full_path, bitrate='192k').subclip(10,) # disable if do not want any clipping
#         clip.write_audiofile(output_path)
#         os.remove(full_path)

def download_video(addr):
    yt = YouTube(addr).streams.filter(mime_type="audio/mp4").first()
    parent_dir = './mp3'
    yt.download(parent_dir)

    print('mp4 파일 다운로드를 완료하였습니다.')
    default_filename = yt.default_filename 
    new_filename = os.path.splitext(default_filename)[0]+'.mp3'
    print(f'새로운 파일의 이름은 {new_filename}입니다.')
    subprocess.call(['ffmpeg', '-i',
        os.path.join(parent_dir, default_filename),
        '-b:a',
        '192K',
        '-vn',
        os.path.join(parent_dir, new_filename)
    ])
    print('mp3 파일 다운로드를 완료하였습니다. mp4 파일을 삭제합니다.')
    os.remove(os.path.join(parent_dir, default_filename))

def download_videos(addr):
    p_list = Playlist(addr)
    p_list.download_all('./mp3')
    print('mp4 파일 다운로드를 완료하였습니다.')
    index = 0
    for link in p_list.parse_links():
        index += 1
        m_addr = 'youtube.com'+link
        yt = YouTube(m_addr).streams.filter(mime_type="audio/mp4").first()
        parent_dir = './mp3'
        default_filename = str(index)+yt.default_filename 
        new_filename = os.path.splitext(default_filename)[0]+'.mp3'
        print(f'새로운 파일의 이름은 {new_filename}입니다.')
        
        subprocess.call(['ffmpeg', '-i',
        os.path.join(parent_dir, default_filename),
        '-b:a',
        '192K',
        '-vn',
        os.path.join(parent_dir, new_filename)
        ])
        
        print('mp3 파일 다운로드를 완료하였습니다. mp4 파일을 삭제합니다.')
        os.remove(os.path.join(parent_dir, default_filename))
    

choose_num = input("재생목록이면 1번 단일 비디오면 2번 : ")
addr = input("주소를 입력하세요 : ")

if choose_num=='1':
    download_videos(addr)
else:
    download_video(addr)




 
