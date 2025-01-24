
# Self Cloud Machine for hosting cloud software service (in-house own, private cloud) 
- Self cloud machine is for in-house self hosting which supports connecting big data, instelligent software service
- It supports Home-scale(in-house) cloud system which based on RaspberryPi5 and Ubuntu OS system
- Web page : http://ssncloud.iptime.org:8888

## RaspberryPi 5 with NVMe booting, it has enough booting speed
- High speed, quite enough performance for personal and family cloud system
- Also name is SSDPi Ver.2.0 (as of 2024.3) on the web page which is same hardware and software


## How to Install system (설치방법)
1. NVMe 에 RaspberryPi5용 Ubuntu OS 설치
2. 하드웨어 조립, NVMe 에 Ubuntu OS 이미지 다운로드 되어 있어야 함 (1번 과정 실행) 
3. 네트워크 연결 및 클라우드 설정
4. Docker 서비스 실행 (apps 디렉토리에 추가 내용 참조)
### Important
- nextcloud Docker image error
- should use image: nextcloud:28.0.9 in docker_compose.yml (as of 2024.8.31)


## Hardware Assembly(하드웨어 조립, 사진포함)
- Hardware assembly, https://github.com/jeonghoonkang/selfcloud/blob/main/installation/hw_install.md


# Software Installation
- RaspberryPi Imager로 Ubuntu OS 설치
- Ubuntu OS 이미지 다운로드를 위한 USB to NVMe 어댑터 필요


## Requirements
## Installation Ubuntu
## Structure of self cloud system
## Application (응용SW)
### motion
- 움직임 감지 카메라
- https://github.com/jeonghoonkang/BerePi/tree/master/apps/camera/motion
