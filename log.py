#!/usr/bin/env python3  
# Om uitvoerbaar te maken : sudo chmod +x log.py via terminal !!
# Starten in background : python log.py &
# in crontab -e "@reboot python log.py &
import RPi.GPIO as GPIO
import time
import datetime
#import MySQLdb as mdb

GPIO.setmode(GPIO.BCM)
time_now = datetime.datetime.now()  
prev_minute = time_now.minute - (time_now.minute % 5)  
heden_minuut = time_now.replace(minute=prev_minute, second=0, microsecond=0)
next_minute=heden_minuut+datetime.timedelta(minutes=5)  # every 5 minutes

GPIO.setup(22, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)  
start=0
teller=0
status22=0
vtijd=0
watt=0

def puls(channel):
    global start
    global teller
    global vtijd	
    global watt
    stop=time.time()
    vtijd=stop-start
    start=time.time()
    if vtijd > 1 and vtijd < 250:
       teller = teller+1
       watt=3600/vtijd
       print ("Tijd: %.4f Teller: %d Watt: %d " %(vtijd,teller,watt))
    else:
       watt=0
       vtijd=0

def insertDB(vtijd, teller, watt): #pulstijd, counts, watt
  try:
    con = mdb.connect('ipadres', 'user', 'password', 'dbase');
    cursor = con.cursor()
    sql = "INSERT INTO kwh (datum, tijd, timestamp, pulsetime, counter, watt) VALUES('%s', '%s', '%s', '%s', '%s', '%s')" % \
    (time.strftime("%Y-%m-%d"), time.strftime("%H:%M"), timestamp, vtijd, teller, watt)
    cursor.execute(sql)
    sql = []
    con.commit()
    con.close()
  except mdb.Error as e:
    print(e)
 
while True:
    Pin22=GPIO.input(22)
    if Pin22:
        if status22==0:puls(0)
    status22=Pin22  
    if(datetime.datetime.now()>next_minute):      
        next_minute=next_minute+datetime.timedelta(minutes=5)
        timestamp = time.time()
        timestamp = timestamp/10
        timestamp = int(timestamp)*10
        if teller < 2:
            teller=0
# uncommend the next line if you want to use the database            
#        insertDB(vtijd, teller, watt)  
        teller=0
 
