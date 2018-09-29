#!/usr/bin/python3
# -*- coding: utf-8 -*-
#====================================
#report.py - core of remote monitoring
#USAGE:
#      crontab -e
#      @reboot /home/toma/DO/./report.py &
# NOTE: install Python3,launch with & in background!
# Author: vasily122@yandex.ru
# Date: 2018 september 29 (revised)
# Version: 3.6
#====================================
import time,os
kanal=0
#before mobile network starts, lets wait 5 min before 1 test...
time.sleep(300)
while kanal==0:
# if network exists, then starts module ~/DO/./monitor.py
        b=os.popen("ping -c1 8.8.8.8|grep icmp_seq= ").read()
        if(b[23:32] =="icmp_seq="):
                kanal=1 #network exists
                os.system("""python3 ~/DO/./monitor.py""")
                break
        else:
                time.sleep(100)
os.system("""(echo "report done"; date)>>monitor.log""")
