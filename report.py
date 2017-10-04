#!/usr/bin/python3
# -*- coding: utf-8 -*-
#====================================
# report.py
# starts in crontab: @reboot /home/toma/DO/./report.py &
# if network exists, then load module ~/DO/./monitor.py
# USE  Python3 
# launch with & 
# Author: vasily122@yandex.ru
# Date: 2017 oct 04
# Version: 3.5
#====================================
import time,os
kanal=0
#lets wait 5 min before 1 test...
time.sleep(300)
while kanal==0:
# === depends from version of ping => for ubuntu 12.04 LTS
# === Also works with cable ethrnet
#        b=os.popen("ping -c1 8.8.8.8|grep icmp_seq= ").read()
#        if(b[68:77] == "icmp_req=" ):

# === depends from version of ping => iputils-s20161105 on ubuntu 16.04,17.04
# === works with Megafon
        b=os.popen("ping -c1 8.8.8.8|grep icmp_seq= ").read()
        if(b[23:32] =="icmp_seq="):
                kanal=1
                os.system("""python3 ~/DO/./monitor.py""")
                break
        else:
                time.sleep(100)
os.system("""(echo "report done"; date)>>monitor.log""")
