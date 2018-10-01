# report
Main purpose of this project is to research and develop
monitoring scripts for some servers, that run BOINC or
for maintain old notebook of my parents

We uses now Xubuntu 16.04 LTS + 4G-modem for Skype whith me and family.
3G-4G usually has dynamic IP ang specific continuous connecting process,
so - communications are via emails only.
NOTE: some ISP and mobile operators are protecting from spam,
so -unmark your emails, moved to spam folder 

Also tested in Ubuntu 17.04,17.10,18.04, Debian 8,9
TODO:
sudo apt-get install exim4 mailutils
sudo dpkg-reconfigure exim4-config

Usually to start monitoring i need 3 files:
1.report.py - core start script, installed in /home/...path.../
It starts once from @reboot in crontab, needs no changes,

USAGE:
  crontab -e
      @reboot  python3 /home/...path.../report.py
      
If network exists - call /home/...path.../ monitor.py  
if not- sleeps and do cycle until network appears. (may depend on ping version)
This file uses ONLY for manual mobile 3G/4G connection, which starts in 2-3-5 min or manually

2.monitor.py - may be called or started without report.py 

USAGE(if networking is persistant):
   crontab -e
     (once on reboot)
     @reboot  python /home/...path.../monitor.py
     or
     0 * * * * python /home/...path.../monitor.py
     (hourly)

monitor.py shoud be tuned - i need to change string 'filename' 
of additional command file (name depends on hostname):
task_<HOSTNAME>.py (from REPOSITORY "report" !!!)
Command file task_<HOSTNAME>.py will download from repository and execute

3.If necessary I can put additional commands to file task_{host}.py in this repository
and get additional reports by mail (different commans for different hosts)
or let them empty
task_<HOSTNAME>.py
  
TODO report.py and monitor.py should be tested both on python3 or python2
