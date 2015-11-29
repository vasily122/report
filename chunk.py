#!/usr/bin/python
# -*- coding: utf-8 -*- 
#====================================
#Prog: external uploaded command module 
#Author: vasily122@yandex.ru
#Date: 2015 nov 29
# Version: 0.2
#====================================
import os
os.system("""(date && uptime && df && netstat -t) | mail -s "Activity report by chunk" vasily122@yandex.ru""")
