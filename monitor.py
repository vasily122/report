#!/usr/bin/python
# -*- coding: utf-8 -*- 
#====================================
#Prog starts on @reboot in crontab
#if network exists then load external module chunk.py, chmod it to a+x and execute
# NEW: in some period downloads new chank.py during work - like bot 
#monitor.py is for remote monitoring server\workstation
#Author: vasily122@yandex.ru
#Date: 2016 may 07
#Version: 2.0.1
#====================================
import os
#remove old chunk.py, if exist
os.system("rm s50_task.py")
# to download new command file, make it executable and if ok - starts it
os.system("wget https://raw.githubusercontent.com/vasily122/scripts/master/s50_task.py")
os.system("chmod a+x s50_task.py && ./s5_task.py")
