#!/usr/bin/python
# -*- coding: utf-8 -*- 
#====================================
#Prog starts on @reboot in crontab
#if network exists then load external module monitor.py
#Author: vasily122@yandex.ru
#Date: 2016 july 28
#Version: 3.1
#====================================
import time,os
kanal=0
while kanal==0:
	b=os.popen("ping -c1 8.8.8.8").read()
	if(b[68:77] == "icmp_req=" ):
#	b=os.popen("ping -c1 8.8.8.8|grep icmp_seq= ").read()
#	if(b[23:32] =="icmp_seq="):	
		kanal=1
		break
	else:
		time.sleep(300)
os.system("""python /home/toma/DO/./monitor.py""")
