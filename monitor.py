
#!/usr/bin/python3
# -*- coding: utf-8 -*- 
#====================================
#monitor.py is for remote monitoring server\workstation
#starts on @reboot or in time - set in crontab
#delate previous module
#if network exists, load new external module task_<HOSTNAME>.py,
#makes it executible (chmod a+x) and run
#Author: vasily122@yandex.ru
#Date: 2016 oct 12
#Version: 2.2
#====================================
import os
os.system("rm task_s50.py")
os.system("wget https://raw.githubusercontent.com/vasily122/scripts/master/task_s50.py")
os.system("chmod a+x task_s50.py")
os.system("python task_s50.py")
