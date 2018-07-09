import os
import datetime
import pyinotify
import logging
import subprocess

class MyEventHandler(pyinotify.ProcessEvent):
    logging.basicConfig(level=logging.INFO,filename='/var/log/monitor.log')
    #自定义写入那个文件，可以自己修改
    logging.info("Starting monitor...")
     
    def process_IN_CREATE(self, event):
        print ('13')
        subprocess.getstatusoutput('sh restart.sh')
    def process_IN_DELETE(self, event):
        print ('16')
        subprocess.getstatusoutput('sh restart.sh')
    def process_IN_MODIFY(self, event):
        print ('19')
        subprocess.getstatusoutput('sh restart.sh')
def main():
    # watch manager
    wm = pyinotify.WatchManager()
    wm.add_watch('/home/ysh/mysite', pyinotify.ALL_EVENTS, rec=True)
    #/tmp是可以自己修改的监控的目录
    # event handler
    eh = MyEventHandler()
 
    # notifier
    notifier = pyinotify.Notifier(wm, eh)
    notifier.loop()
 
if __name__ == '__main__':
    main()
