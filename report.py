#!/usr/bin/python3
# -*- coding: utf-8 -*-
#====================================
#report.py - core of remote monitoring
#USAGE:
#      crontab -e
#      @reboot /home/toma/DO/./report.py &
# NOTE: install Python3,launch with & in background!
# Author: vasily122@yandex.ru
# Date: 2018 october 05
# Version: 3.7
#====================================
import time,os
kanal=0

#before mobile network starts, lets wait 5 min before 1 test - need time to start
time.sleep(300)
while kanal==0:

#version with eth0
#	b=os.popen("ping -c1 8.8.8.8").read()
#	if(b[68:77] == "icmp_req=" ):

#version with mobile provider Megafon
        b=os.popen("ping -c1 8.8.8.8|grep icmp_seq= ").read()
        if(b[23:32] =="icmp_seq="):

# if network exists, then starts module ~/DO/./monitor.py                
                kanal=1
                os.system("""python3 ~/DO/./monitor.py""")
                break
        else:
                time.sleep(100)
os.system("""(echo "report done"; date)>>monitor.log""")
