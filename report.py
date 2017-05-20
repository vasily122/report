#!/usr/bin/python3
# -*- coding: utf-8 -*- 
#====================================
# report.py
# starts in crontab: @reboot /home/toma/DO/./report.py & 
#if network exists, then load module ~/DO/./monitor.py
# USE  Python3 !
# launch with & !
#Author: vasily122@yandex.ru
#Date: 2017 may 20
#Version: 3.2
#====================================
import time,os
kanal=0
while kanal==0:
        b=os.popen("ping -c1 8.8.8.8").read()
        if(b[68:77] == "icmp_req=" ):
# === TODO depends from version of ping? ===== 
#	b=os.popen("ping -c1 8.8.8.8|grep icmp_seq= ").read()
#	if(b[23:32] =="icmp_seq="):	
                kanal=1
                os.system("""python3 ~/DO/./monitor.py""")
                break
        else:
                print("sleep...")
                time.sleep(60)
#		time.sleep(600)
