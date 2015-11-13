#!/usr/bin/python
# -*- coding: utf-8 -*- 
#====================================
#Prog:from cron and if network exists
#load external module chunk.py, chmod it to a+x and execute
#monitor.py for monitoring outstanding server\workstation
#Author: vasily122@yandex.ru
#Date: 2015 nov 12
#Version: 0.2
#====================================
import time,os
kanal=0
while kanal==0:
#	print("+\n")
#	time.sleep(3)
	b=os.popen("ping -c1 8.8.8.8").read()
	if(b[68:77] =="icmp_seq="):
		kanal=1
os.system("wget https://raw.githubusercontent.com/vasily122/scripts/master/chunk.py")
os.system("chmod a+x chunk.py && ./chunk.py")
