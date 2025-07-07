
# IoT Stack 을 활용하여 설치

- curl -fsSL https://raw.githubusercontent.com/SensorsIot/IOTstack/master/install.sh | bash
- cd ~/IOTstack
- sudo ./menu.sh 실행하여, 메뉴로 선택 docker-compose.yml 생성 
  - 이후 메뉴에 따라 설치 [메뉴설치](<a href target=_blank > iostack_run.md </a>) 
- docker-compose.yml 수정
  - ${VOL_PATH}/photo_volume:/Photo 

## 문제 발생시, 설치 완료 불가능
### python 3.11 외부 설정 문제
<pre>
EXTERNALLY-MANAGED 이슈 나오면서, 설치가 안되는 경우가 있음. 아래처럼 변경하였음 (3.11은 버전에 따라 변경될 수 있음)
sudo mv /usr/lib/python3.11/EXTERNALLY-MANAGED /usr/lib/python3.11/EXTERNALLY-MANAGED_OLD
</pre>

### 도커버전 문제 

![image](https://github.com/user-attachments/assets/34ba078a-3234-4194-9fb0-62cf26b57493)


- 삭제순서
  - sudo docker ps -a 로 컨테이너 이름 확보
  - sudo docker rm {컨테이너 이름} 
  - sudo docker images; sudo dcoker rmi {image이름}
