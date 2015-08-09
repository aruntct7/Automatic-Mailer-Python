#!/usr/bin/python
 
# Import smtplib for the actual sending function
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from time import sleep
import schedule
import time

 
# For guessing MIME type
import mimetypes
 
# Import the email modules we'll need
import email
import email.mime.application
 
#Import sys to deal with command line arguments
import sys

   
i=1
 
def mail():
        global i
        print("inside mail")
        msg = email.mime.multipart.MIMEMultipart()
        msg['Subject'] = 'Mobile Computing-'+str(i)
        msg['From'] = 'from address'
        #msg['To'] = ''
        
        i=i+1      

        body = email.mime.text.MIMEText("Reference Material for MC !!!")

        msg.attach(body)
         

        filename="file path"
         
         
        fp=open(filename,'rb')
        att = email.mime.application.MIMEApplication(fp.read(),_subtype=type)
        fp.close()
        att.add_header('Content-Disposition','attachment',filename=filename)
        msg.attach(att)
         
        s = smtplib.SMTP('smtp.gmail.com:587')
        s.starttls()
        s.login('your username','your password')
        s.sendmail('from address',['to address 1','to address 2'], msg.as_string())
        s.quit()

print("before schedule")

schedule.every(2).seconds.do(mail)
print ("after schedule")
while True:
    schedule.run_pending()
    time.sleep(1)











