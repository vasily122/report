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
#Date: 2017 may 20
#Version: 2.2
#====================================
import os
os.system("rm task_besl.py")
os.system("wget https://raw.githubusercontent.com/vasily122/scripts/master/task_besl.py")
os.system("chmod a+x task_besl.py")
os.system("python task_besl.py")
