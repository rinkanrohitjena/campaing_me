import os
import sys
import time
import csv
print("ALL RIGHTS RESERVED @2020 RINKAN ROHIT JENA >>>SECURE CORE SEC    ")



aol=('aol.com\n')
gmail = ("gmail.com\n")
yahoo = ('yahoo.com\n')
ymail = ('ymail.com\n')
scb=('sbcglobal.net\n')
frontier=('frontier.com\n')
verizon=('verizon.net\n')
netzero=('netzero.net\n')
juno=('juno.com\n')
att=('att.net\n')
bellsouth=('bellsouth.net\n')
hitter=('hittermail.com\n')
rocket=('rocketmail.com\n')
outlook = ('outlook.com\n')
hotmail = ('hotmail.com\n')
live=('live.com\n')
cox=('cox.net\n')
roadrunner=('roadrunner.com\n')
comcast=('comcast.net\n')
optonline=('optonline.net\n')
earthlink=('earthlink.net\n')



email_list='email.csv'
list = open(email_list, "r")
email_lines = list.readlines()


for each_email in email_lines:
    if each_email.endswith(aol):
        file = open("finalset.txt","a")
        file.write((each_email)+"")
        file.close() 

                           
    if each_email.endswith(gmail):
        file = open("finalset.txt","a")
        file.write((each_email)+"")
        file.close()

                    
    if each_email.endswith(yahoo):
        file = open("finalset.txt","a")
        file.write((each_email)+"")
        file.close()
    
    if each_email.endswith(ymail):
        file = open("finalset.txt","a")
        file.write((each_email)+"")
        file.close()
                    
    
    if each_email.endswith(scb):
        file = open("finalset.txt","a")
        file.write((each_email)+"")
        file.close()
                         
    
    if each_email.endswith(frontier):
        file = open("finalset.txt","a")
        file.write((each_email)+"")
        file.close()       
    
    if each_email.endswith(verizon):
        file = open("finalset.txt","a")
        file.write((each_email)+"")
        file.close()
    
    if each_email.endswith(netzero):
        file = open("finalset.txt","a")
        file.write((each_email)+"")
        file.close()
    
    if each_email.endswith(juno):
        file = open("finalset.txt","a")
        file.write((each_email)+"")
        file.close()
    
    if each_email.endswith(att):
        file = open("finalset.txt","a")
        file.write((each_email)+"")
        file.close()
    
    if each_email.endswith(bellsouth):
        file = open("finalset.txt","a")
        file.write((each_email)+"")
        file.close()
    
    if each_email.endswith(hitter):
        file = open("finalset.txt","a")
        file.write((each_email)+"")
        file.close()
    
    if each_email.endswith(rocket):
        file = open("finalset.txt","a")
        file.write((each_email)+"")
        file.close()
    
    if each_email.endswith(outlook):
        file = open("finalset.txt","a")
        file.write((each_email)+"")
        file.close()
    
    if each_email.endswith(hotmail):
        file = open("finalset.txt","a")
        file.write((each_email)+"")
        file.close()
    
    if each_email.endswith(live):
        file = open("finalset.txt","a")
        file.write((each_email)+"")
        file.close()
    
    if each_email.endswith(cox):
        file = open("finalset.txt","a")
        file.write((each_email)+"")
        file.close()
    
    if each_email.endswith(roadrunner):
        file = open("finalset.txt","a")
        file.write((each_email)+"")
        file.close()
    
    if each_email.endswith(comcast):
        file = open("finalset.txt","a")
        file.write((each_email)+"")
        file.close()
    
    if each_email.endswith(optonline):
        file = open("finalset.txt","a")
        file.write((each_email)+"")
        file.close()
    
    if each_email.endswith(earthlink):
        file = open("finalset.txt","a")
        file.write((each_email)+"")
        file.close()
print("Its all done")

