#!/usr/bin/python3
# -*- coding: utf-8 -*- 
#====================================
# Prog: external uploaded command module 
# Author: vasily122@yandex.ru
# Date: 2017 may 24
# Version: 0.4
#====================================
import os
os.system(""" date >> /home/toma/DO/log.txt """)
os.system("""(date; df)| mail -s "Samsung r530" vasily122@yandex.ru """)
