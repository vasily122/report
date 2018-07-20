#!/usr/bin/python3
# -*- coding: utf-8 -*- 
import os
os.system("""(date; df; tail ~/monitor.log; sync) | mail -s "Samsung_R530 is online" vasily122@yandex.ru""")
