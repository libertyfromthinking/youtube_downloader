# Youtube mp3 Downloader
우분투 환경에서 ffmpeg와 파이썬을 이용해 유튜브 동영상을 로컬에 mp3 파일로 받습니다

## 설치방법(우분투 18.04 기준)
가상환경을 설치합니다
```sh
$ python3 -m virtualenv .venv
```

가상환경을 활성화합니다
```sh
$ source .venv/bin/activate
```

git 저장소를 clone 합니다
```sh
$ git clone https://github.com/libertyfromthinking/youtube_downloader.git 
```

프로젝트 디렉토리로 이동 후 pip를 업데이트 합니다
```sh
$ cd django_korean_anagram
$ pip install -upgrade pip
```

requirements.txt 파일로 패키지들을 설치합니다
```sh
$ pip install -r requirements.txt
```

ffmpeg를 설치합니다
```sh
$ sudo apt install ffmpeg
```

실행 후 다운받으려는 동영상의 주소를 입력합니다
```sh
$ python3 test.py
```



