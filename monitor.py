#!/usr/bin/python
# -*- coding: utf-8 -*- 
#====================================
#Prog starts on @reboot in crontab and if network exists then
#load external module chunk.py, chmod it to a+x and execute
#monitor.py is for remote monitoring server\workstation
#Author: vasily122@yandex.ru
#Date: 2016 jan 19
#Version: 0.4
#====================================
import time,os
chanel=0
while chanel==0:
	b=os.popen("ping 8.8.8.8 -c1 |grep icmp_seq=").read()
	if(b[23:32] =="icmp_seq="):
		chanel=1
	time.sleep(100)
# remove old chunk.py, if exist
os.system("rm chunk.py")
# to download new command file, make it executable and if ok- snart it
os.system("wget https://raw.githubusercontent.com/vasily122/scripts/master/chunk.py")
os.system("chmod a+x chunk.py && ./chunk.py")
