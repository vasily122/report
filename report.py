#!/usr/bin/python
# -*- coding: utf-8 -*- 
#====================================
#Prog:from cron and if network exists
#run report.py to monitoring outstanding server\workstation
#chmod a+x report.py
#crontab -e : @reboot /home/arina122/DO/./report.py
#Author: vasily122@yandex.ru
#Date: 2015 nov 16
#Version: 0.3
#====================================
import time,os
kanal=0
while kanal==0:
	time.sleep(300)
	b=os.popen("ping -c1 8.8.8.8|grep icmp_seq= ").read()
	if(b[23:32] =="icmp_seq="):
		kanal=1
os.system("""(date && df) | mail -s "Activity report" vasily122@yandex.ru""")
