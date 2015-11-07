#!/usr/bin/python
# -*- coding: utf-8 -*- 
#====================================
#Prog: external uploaded command module 
#Author: vasily122@yandex.ru
#Date: 2015 nov 7
# Version: 0.1
#====================================
import os
os.system("""(uname -a && date && df) | mail -s "Activity report" vasily122@yandex.ru""")
