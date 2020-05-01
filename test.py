from pytube import YouTube, Playlist
import os
import subprocess

import moviepy.editor as mp
import re


def download_video(addr):
    '''링크의 동영상을 mp3 형식으로 mp3 폴더에 다운로드합니다

    1. 해당 동영상을 mp4 형식으로 먼저 다운로드 합니다. 재생목록일 경우 1, 단일 동영상일 경우 2 입력
    2. 동영상 링크를 입력합니다. 축약주소, 모바일주소, 웹주소 모두 가능합니다.
    3. pytube 라이브러리로 mp3디렉토리에 mp4 파일로 먼저 다운로드받습니다.
    4. 로컬에 설치되어 있는 ffmpeg로 mp3로 인코딩합니다.
    5. mp4파일을 삭제합니다.
    '''
    try:
        yt = YouTube(addr).streams.filter(mime_type="audio/mp4").first()
    except:
        print('올바른 형식으로 입력해주십시오')
        return

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
    try:
        p_list = Playlist(addr)
    # 'list' 문자열을 찾지못하면 에러
    except KeyError:
        print('올바른 주소값을 입력해주십시오')
        return

    p_list.download_all('./mp3')
    print('mp4 파일 다운로드를 완료하였습니다.')
    index = 0
    list_len = len(str(len(p_list)))

    for link in p_list.parse_links():
        index += 1
        index_str = len(str(index))
        if index_str<list_len:
            index = '0'*(list_len-index_str)+str(index)
        else:
            index = str(index)

        m_addr = 'youtube.com'+link
        yt = YouTube(m_addr).streams.filter(mime_type="audio/mp4").first()
        parent_dir = './mp3'
        default_filename = index+yt.default_filename 
        new_filename = os.path.splitext(default_filename)[0]+'.mp3'
        print(f'새로운 파일의 이름은 {new_filename}입니다.')
        
        subprocess.call(['ffmpeg', '-i',
        os.path.join(parent_dir, default_filename),
        '-b:a',
        '192K',
        '-vn',
        os.path.join(parent_dir, new_filename)
        ])
        index = int(index) 
        print('mp3 파일 다운로드를 완료하였습니다. mp4 파일을 삭제합니다.')
        os.remove(os.path.join(parent_dir, default_filename))
    

choose_num = input("재생목록이면 1번 단일 비디오면 2번 : ")
addr = input("주소를 입력하세요 : ")
print('** 플레이리스트나 영상이 비공개상태거나 비어있다면 정상적으로 작동하지 않을 수 있습니다.')

if choose_num=='1':
    download_videos(addr)
elif choose_num=='2':
    download_video(addr)
else:
    print('1번과 2번중에 선택해주십시오')




 
