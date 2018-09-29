#!/usr/bin/python3
# -*- coding: utf-8 -*- 
#====================================
#monitor.py -remote monitoring linux server\workstation script in python3
#USAGE:
#      crontab -e
#      0 * * * * python3 /home/...path.../monitor.py
#Author: vasily122@yandex.ru
#Date: 2018 september 29
#Version: 3.3
#====================================
import os
#set filename for proper server: task_<HOSTNAME>.py
filename="task_tower.py"
#at the beginning delete previous module
os.system("rm "+filename)
#load new external module  (network must exist)
os.system("wget https://raw.githubusercontent.com/vasily122/report/master/"+filename)
#make it executible and run
os.system("chmod a+x "+filename)
os.system("python3 "+filename)
os.system("""(echo "monitor done"; date) >> monitor.log""")
