# MineCraft private server install 
  - Ubuntu 24.10 LTS
  - Rasberrypi 5 8GB
  - 참고 사이트
      - https://pimylifeup.com/ubuntu-minecraft-server-java/

# 1. step
```
sudo apt update
sudo apt upgrade
```
# 2. JAVA Install
```
sudo apt install openjdk-21-jre-headless
```

# 3. MineCraft Server File dir
```
sudo mkdir /home/((user))/minecraft
cd /home/((user))/minecraft
```

# 4. copy link latest version
  - visit below link 
  - https://www.minecraft.net/en-us/download/server
  - copy link download
```
sudo wget (copy link)
```

# 5. You can use the ls command to view the contents of your directory, which should contain the “server.jar” file.
```
ls
server.jar
```
# 6. Run Java Server
```
sudo java -Xms1024M -Xmx2048M -jar ./server.jar nogui
```
```
 To launch the server, we need to enter a Java command that specifies a few settings and references the server jar file.

-Xms allows you to specify the initial size of the memory allocation pool. The number is in bytes unless followed by a letter. K or k for kilobytes. M or m for megabytes.
-Xmx allows you to specify the maximum size of the memory allocation pool. The number is in bytes unless followed by a letter. K or k for kilobytes. M or m for megabytes.
-jar is followed by the jar file that you wish to run.
nogui we set this option as we do not need any GUI (Graphical User Interface) as we’re running the server from the terminal.
```

# 7. As soon as you start the server, it will stop as you will need to agree to a EULA to proceed.
```
[10:08:07] [ServerMain/INFO]: Building unoptimized datafixer
[10:08:09] [ServerMain/ERROR]: Failed to load properties from file: server.properties
[10:08:09] [ServerMain/WARN]: Failed to load eula.txt
[10:08:09] [ServerMain/INFO]: You need to agree to the EULA in order to run the server. Go to eula.txt for more info
```
```
sudo vim eula.txt
```
```
eula=TRUE
```
```
sudo java -Xms1024M -Xmx2048M -jar ./server.jar nogui
```
# 8. If you are running UFW on your Ubuntu machine you will want to allow port “25565” before connecting to the Minecraft Java Edition server.
```
sudo apt install ufw
sudo ufw enable
sudo ufw allow 25565
sudo ufw status
```
# 9. Set up an online participation session
```
sudo vim server.properties
online-mode = True -> online-mode = false
```


    
