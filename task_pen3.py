#!/usr/bin/python3
# -*- coding: utf-8 -*- 
#2021feb01
#2021apr26 - 2021may04 - processor fan died, repaired by Maks

import os
#os.system("""(sync; date; ps ax; uptime)| mail -s "pen3 milkyway" vasily122@yandex.ru""")

os.system("""rm index.shtml""")
os.system("""rm index.html""")
os.system("""wget -O index.html opennet.ru/index.shtml""")
os.system("""(cat index.html) | mail -s "Pentium3 news digest 0.3" vasily122@yandex.ru""")

#os.system("""(date; ls -R /var/lib/boinc-client; cat /var/lib/boinc-client/gui_rpc_auth.cfg)| mail -s "pen3 boinc" vasily122@yandex.ru""")
#os.system("""(sync; date;crontab -l;cat ~/DO/monitor.py;ls  ~/DO/;cat /etc/issue; )| mail -s "Pen3 serv files" vasily122@yandex.ru""")
#os.system("""(sync; uptime; ps ax; cat /var/lib/boinc-client/stderrdae.txt; date; cat /var/lib/boinc-client/stdoutdae.txt; date; cat /var/lib/boinc-client/time_stats_log)| mail -s "pen3 milky errors" vasily122@yandex.ru""")
#os.system("""(date; cat .bash_history)| mail -s "Pen3 history" vasily122@yandex.ru""")
#os.system("""(date;ls) |mail -s "Pen3 html test 0.1" vasily122@yandex.ru""")
#os.system("""wget opennet.ru""")
#os.system("""mail -s "Pen3 test 0.16 wget" vasily122@yandex.ru < index.shtml""")
#os.system("""(date;ls) | mail -s "Pen3 test 0.13" vasily122@yandex.ru""")
#os.system("""catx --dump opennet.ru""")
#os.system("""rm index.html""")
#os.system("""(sync; date; uptime; ps ax) | mail -s "PentiumIII" vasily122@yandex.ru""")
#os.system("""(sync; date; uptime; ps ax; crontab -l; cat ~/DO/monitor.py; cat ~/task_pen3.py) | mail -s "Pen3 " vasily122@yandex.ru""")
#os.system("""(date;crontab -l;cat ~/DO/monitor.py)| mail -s "pen3" vasily122@yandex.ru""")
#os.system("""wget https://raw.githubusercontent.com/vasily122/report/master/monitor.py""")
#os.system("""ls -la|mail -s "pen3 get monitor" vasily122@yandex.ru""")
#os.system("""(date;python3 --version;uptime)|mail -s "pen3 python versions" vasily122@yandex.ru""")
