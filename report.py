#!/usr/bin/python
# -*- coding: utf-8 -*- 
#====================================
#Prog:from cron and if network exists
#run report.py to remote monitoring server\workstation
#report.py converted to monitor.py+sort.sh
#note: chmod a+x report.py
#crontab -e : @reboot ~/DO/./report.py
#Author: vasily122@yandex.ru
#Date: 2015 dec 8
#Version: 1.3
#====================================
import time,os
chanel=0
while chanel==0:
	time.sleep(300)  #every 5 minutes until network appear 
	b=os.popen("ping -c1 8.8.8.8|grep icmp_seq= ").read()
	if(b[23:32] =="icmp_seq="):
		chanel=1
os.system("""(date && df) | mail -s "Activity report" vasily122@yandex.ru""")

#DONE next idea is to split report.py to: monitor.py (resident) and chunk.py (download every time,changeble)
