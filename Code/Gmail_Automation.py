# -------------------------------------------------------------------------
#
# Copyright Altran, 2019 
#
# -------------------------------------------------------------------------
# Description:This python script includes following tasks.
#    1. to send an email to specific person.
#    2. to send an email to group.
#    3. to read subject from the latest email.
#    4. to read body of the message from the latest email.
#    5. to get all the links from latest email.
#    6. to get the email sender(From).
#    7. to get the email receiver(toList).
#
# -------------------------------------------------------------------------
#   Referal links:
#   https://www.freecodecamp.org/news/send-emails-using-code-4fcea9df63f/
#
#   https://stackoverflow.com/questions/2230037/how-to-fetch-an-email-body-using-imaplib-in-python
# -------------------------------------------------------------------------


#In String module,Template Class allows to create 
#simplified syntax for output specification.
from string import Template

# A Content-Type header of multipart/_subtype will 
#be added to the message object.
from email.mime.multipart import MIMEMultipart

#The MIMEText class is used to create MIME objects of major 
#type text. _text is the string for the payload.
from email.mime.text import MIMEText

#Used for calculating differences in dates and 
#also can be used for date manipulations.
import datetime


import email

#This module defines three classes, IMAP4, IMAP4_SSL and IMAP4_stream. 
import imaplib

#This module defines two classes, Mailbox and Message, for accessing and 
#manipulating on-disk mailboxes and the messages they contain.
#Mailbox offers a dictionary-like mapping from keys to messages
import mailbox

#This module provides regular expression matching operations.
import re

#The smtplib module defines an SMTP client session object that can be used 
#to send mail to any Internet machine with an SMTP.
import smtplib

#Used to handle time-related tasks.
import time

#Login Credentials to check receiver details.
RECEIVER_EMAIL = "mckeemckee23@gmail.com"
PASSWORD_RECEIVER = "MckeeMckee@23"

#Login credentials of sender.
SENDER_EMAIL = 'mcleemclee21@gmail.com'
PASSWORD_SENDER = 'McleeMclee@21'

#List to store the email contacts.
gmail_contact_list = {'Mckee':'mckeemckee23@gmail.com','Padmini':'padmini2.v@aricent.com','Supriya':'supriya.j@aricent.com'}

#Variable to store the message body.
message_body = "Hello\n\
    This is a TEST MESSAGE.\n\
    Happy Weekend!\n\
    https://www.onlinegdb.com/online_python_compiler#"
    

#class for gmail automation task.
class Task_01:

        
    def send_gmail(self):
        """
            To send gmail for the contacts mentioned in list
            
            :param: None
            :return: None
        """
       
        print(message_body)
        s = smtplib.SMTP("smtp.gmail.com",587)
        print("SMTP login successful")
        s.starttls()

        s.login(SENDER_EMAIL, PASSWORD_SENDER)
        for email in gmail_contact_list.values():

            #MIMEMultipart() class in Python represents Multipart messages
            #which consists of multiple messages and each of them defines
            #its own Content-Type such as "To", "From" etc.
            msg = MIMEMultipart()    
            
            msg['From']=SENDER_EMAIL

            msg['To']= email

            msg['Subject']="TEST MESSAGE"

            #MIMEText is for text if the whole message is in text format
            msg.attach(MIMEText(message_body, 'plain'))     #(text/plain or text/html)
            s.send_message(msg)
    
    def receive_gmail(self):
        mail = imaplib.IMAP4_SSL('imap.gmail.com')
        mail.login(RECEIVER_EMAIL, PASSWORD_RECEIVER)
        mail.list()
        mail.select('inbox')
        result, data = mail.uid('search', None, "UNSEEN") # (ALL/UNSEEN)
        i = len(data[0].split())
        for x in range(i):
            latest_email_uid = data[0].split()[x]
            result, email_data = mail.uid('fetch', latest_email_uid, '(RFC822)')
		 
	    # this might work to set flag to seen, if it doesn't already
            raw_email = email_data[0][1]
            raw_email_string = raw_email.decode('utf-8')

            email_message = email.message_from_string(raw_email_string)
            email_from = str(email.header.make_header\
                             (email.header.decode_header(email_message['From'])))
            email_to = str(email.header.make_header\
                           (email.header.decode_header(email_message['To'])))
            subject = str(email.header.make_header\
                          (email.header.decode_header(email_message['Subject'])))
			
	    # Body details
            for part in email_message.walk():
		#Returns the message content type. The returned string is
                #coerced to lower case of the form maintype/subtype
                #Different types of content types are : text/plain, text/html
                if part.get_content_type() == "text/plain":
                    body = part.get_payload(decode=True)
                    file_name = "email_" + str(x) + ".txt"
                    try:
                        output_file = open(file_name, 'w')
                    except IOError as fnf_error:
                        print(fnf_error)
                    else:
                        output_file.write("Subject: %s\n" %(subject))
                        output_file.write("Body: %s\n" %(body.decode('utf-8')))
                        output_file.write("Email_Sender: %s\n" %(email_from))
                        output_file.write("Email_Receiver: %s\n" %(email_to))
                        output_file.close()
    
                        #to extract link from message body of the gmail received.
                        for one_link in re.findall('https?://[\w./%-]+', \
                                                   email_message.as_string()):
                            print(one_link) 
                            exit(0)
                else:
                    continue
    
def main():
    
    #Creating new object for class Task_01
    gmail_automation_obj = Task_01()
    
    #Calling the method send_gmail()
    gmail_automation_obj.send_gmail()
        
    #Calling the method receive_gmail()
    gmail_automation_obj.receive_gmail()
   
        
       
if __name__ == "__main__":
    main()
