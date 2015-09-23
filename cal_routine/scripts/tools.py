#!/usr/bin/env python

import rospy
import urllib
import json

from lxml import etree

from calendar import timegm
from dateutil import parser
from dateutil import tz
from datetime import datetime
from datetime import timedelta

from threading import Thread



global target_time

PKG = 'cal_routine'

file_name_default= '../data/data_r.xml'





class Cal:

    def __init__(self,update_wait=60, file_name=None):
        self.tz_utc = tz.gettz('UTC')
        if file_name is not None:
            self.uri = file_name
        else:
            self.uri = file_name_default
        self.update_wait = update_wait
        global target_time
        target_time = datetime.now()
        target_time = target_time.replace( second=target_time.second+10 )
        self.update_worker = Thread(target=self.waiting_run)
        
    def start_worker(self):
        self.update_worker.start()
        
            
    def waiting_run(self):
        
        global target_time
        # make sure we can be killed here
        while not rospy.is_shutdown():
            #if exist next event
            if target_time:
                while datetime.now() < target_time and not rospy.is_shutdown():
                    print 'update'
                    #task.name='tour'
                    publish_next_task('tour')
                    rospy.sleep(1)
                    
                publish_task()
                target_time = None
             
    def run(self):
        print 'run'
        
        
    def recurring_day(self,rec_type_str):
        #if (events[i].find("event_pid").text): # Recurring event modified 
            #print "event_pid"
        rec_type_str=rec_type_str.split('#')
        rec_type=rec_type_str[0].split('_')
        print rec_type
        ok_today=False
        if rec_type[0]=='day':
            ok_today=True
        elif rec_type[0]=='week':
            
            today_d=datetime.today().weekday()
            day_n=rec_type[4].split(',')
            
            for i in range(len(day_n)):
                
                if day_n[i]==str(today_d):
                    ok_today=True
                    print ok_today
                    
        elif rec_type[0]=='month':
            print 'month'
        return ok_today
        
    def update_cal(self):
        doc = etree.parse(self.uri)
        #print etree.tostring(doc,pretty_print=True ,xml_declaration=True, encoding="utf-8")
        
        events=doc.findall("event")
        for i in range(len(events)):
            
            start_str=events[i].find("start_date").text
            start_t=datetime.strptime(start_str, '%Y-%m-%d %H:%M')
            end_str=events[i].find("end_date").text
            end_t=datetime.strptime(end_str, '%Y-%m-%d %H:%M')
            now = datetime.now()
            
            if now > end_t: # Past event 
                continue
            today_t= now.replace(hour=23, minute=59, second=0, microsecond=0)
            if today_t < start_t: # After today event 
                continue
            
            if events[i].find("rec_type").text: # Recurring event
                rec_type_str=events[i].find("rec_type").text
                if self.recurring_day(rec_type_str):
                    print 'recurring'
                else:
                    print 'not recurring'
                    continue
                
            #Today event
            
            print start_t
            

        
if __name__ == '__main__':
    print 'tools'
    pass

