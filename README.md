# RaspberryPi-Timelapse
The project is a tutorial on how to build and implement a long time lapse recording based on a Raspberry Pi.

![Setup](setup.JPG)

## Components

- Raspberry Pi Zero WH V1
- 5MP RPIZ OV5647 Camera Module
- Weatherproof IP66 CCTV Camera Housing
- FFC/FPC/FPV Cable and Connectors
- UFL SMD Solder Connector
- UFL Antenna
- 3D printed Parts

## Software

Raspberry Pi OS Lite V5.15


##Steps 

1. Connect all wires and put the camera in the outdoor housing
2. Install the OS
3. Connect the Raspi to a monitor and enable SSH with the command: 
```
pi@IP:~$ sudo raspi-config
```
4. Connect with your device via SSH to the Raspi
5. Clone the repo and move the Python-Script in the home directory
6. Edit the parameters of timelapse.py
7. Create the images-folder:
```
pi@IP:~$ mkdir images
```
9. Move the service-files in the following directory, or create them, and copy the content:
```
pi@IP:~$ cd /lib/systemd/system

pi@IP:~$ sudo nano timelapse.service
pi@IP:~$ sudo nano timelapse.timer
```
8. Enable and start the services
```
pi@IP:~$ systemctl start timelapse.service
pi@IP:~$ systemctl enable timelapse.service

pi@IP:~$ systemctl start timelapse.timer
pi@IP:~$ systemctl enable timelapse.timer
```
9. You can copy the files to your remote machine:
10. ```
remote:~$ rsync -r -t pi@IP:/home/pi/images/  /Users/remote/Desktop/images
```


