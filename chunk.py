#!/usr/bin/python
# -*- coding: utf-8 -*- 
#====================================
# Prog: external uploaded command module 
# Author: vasily122@yandex.ru
# Date: 2016 jan 19
# Version: 0.3
#====================================
import os
os.system("""(date ; ls -la /var/lib/boinc-client) | mail -s "Activity report" vasily122@yandex.ru""")
