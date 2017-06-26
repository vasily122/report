#!/usr/bin/python3
# -*- coding: utf-8 -*- 
#====================================
#monitor.py is for remote monitoring server\workstation
#launch with & !
#starts on @reboot or in time - set in crontab
#delete previous module
#if network exists, load new external module task_<HOSTNAME>.py,
#makes it executible (chmod a+x) and run
#Author: vasily122@yandex.ru
#Date: 2017 june 26
#Version: 3.0
#====================================
import os
filename="task_s50.py"
os.system("rm "+filename)
os.system("wget https://raw.githubusercontent.com/vasily122/scripts/master/"+filename)
os.system("chmod a+x "+filename)
os.system("python3 "+filename)
print("monitor.py done")
#os.system("./"+filename)
