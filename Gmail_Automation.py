# -------------------------------------------------------------------------
#
# Copyright Altran, 2019
#
# -------------------------------------------------------------------------
# Description:This python script includes following tasks.
#    1. to send an email to specific person.
#    2. to send an email to group.
#    3. to read subject from the latest email
#    4. to read body of the message from the latest email
#    5. to get all the links from latest email
#    6. to get the email sender(From)
#    7. to get the email receiver(toList)
#
# -------------------------------------------------------------------------


#In String module,Template Class allows to create simplified syntax for output specification.
from string import Template

# A Content-Type header of multipart/_subtype will be added to the message object.
from email.mime.multipart import MIMEMultipart

#The MIMEText class is used to create MIME objects of major type text. _text is the string for the payload.
from email.mime.text import MIMEText

#used for calculating differences in dates and also can be used for date manipulations.
import datetime

#
import email

#This module defines three classes, IMAP4, IMAP4_SSL and IMAP4_stream.
import imaplib

#This module defines two classes, Mailbox and Message, for accessing and manipulating on-disk mailboxes and the messages they contain.
#Mailbox offers a dictionary-like mapping from keys to messages
import mailbox

#This module provides regular expression matching operations
import re

#The smtplib module defines an SMTP client session object that can be used to send mail to any Internet machine with an SMTP
import smtplib

#Used to handle time-related tasks
import time

#Login Credentials to check receiver details
EMAIL_ACCOUNT = "mckeemckee23@gmail.com"
PASSWORD = "MckeeMckee@23"

#Login credentials of sender
MY_ADDRESS = 'mcleemclee21@gmail.com'
PASSWORD_SENDER = 'McleeMclee@21'

#File which has sender list
filename_con = 'mycontacts.txt'

#File which has the message to send
filename_msg ='message.txt'

class Task_01:
    def __init__(self):
        self.self=self

    def get_contacts(self,filename_con):
        self.filename_con=filename_con
        names = []
        emails = []
        with open(filename_con, mode='r') as contacts_file:
            for a_contact in contacts_file:
                names_0 = a_contact.split()[0]
                emails_0 = a_contact.split()[1]
                names.append(names_0)
                emails.append(emails_0)
                print(names)
                print(emails)
        return names, emails

    def read_template(self,filename_msg):
        self.filename_msg=filename_msg
        print("login successful")
        with open(filename_msg, 'r') as template_file:
            template_file_content = template_file.read()
            print(template_file_content)
        return Template(template_file_content)

def main():
    get_contacts_obj = Task_01()
    get_contacts_obj.get_contacts(self,filename_con)

    #names,emails = get_contacts(filename_con)
    #print(names)
    #print(emails)

    read_template_obj = Task_01()
    read_template_obj.read_template(self,filename_msg)

    message_template = read_template('message.txt')
    print(message_template)
    s = smtplib.SMTP("smtp.gmail.com",587)
    print("login successful")
    s.starttls()

    s.login(MY_ADDRESS, PASSWORD_SENDER)
    for name, email in zip(names, emails):

        msg = MIMEMultipart()
        message = message_template.substitute(PERSON_NAME=name.title())
        print(message)

        msg['From']=MY_ADDRESS

        msg['To']=email

        msg['Subject']="This is TEST MESSAGE"

        msg.attach(MIMEText(message, 'plain'))
        s.send_message(msg)
        #time.sleep(10)
        mail = imaplib.IMAP4_SSL('imap.gmail.com')
        #print(dir(mail))
        mail.login(EMAIL_ACCOUNT, PASSWORD)
        mail.list()
        mail.select('inbox')
        result, data = mail.uid('search', None, "UNSEEN") # (ALL/UNSEEN)
        i = len(data[0].split())
        for x in range(i):
            latest_email_uid = data[0].split()[x]
            result, email_data = mail.uid('fetch', latest_email_uid, '(RFC822)')
			# result, email_data = conn.store(num,'-FLAGS','\\Seen')
			# this might work to set flag to seen, if it doesn't already
            raw_email = email_data[0][1]
            raw_email_string = raw_email.decode('utf-8')
            #print(raw_email_string)
			#print(dir(email))
            email_message = str(email.message_from_string(raw_email_string))
			#email_from = str(email.header.make_header(email.header.decode_header(email_message['From'])))
			#email_to = str(email.header.make_header(email.header.decode_header(email_message['To'])))
			#subject = str(email.header.make_header(email.header.decode_header(email_message['Subject'])))

			# Body details
            for part in email_message.walk():
                if part.get_content_type() == "text/plain":
                    body = part.get_payload(decode=True)
                    file_name = "email_" + str(x) + ".txt"
                    output_file = open(file_name, 'w')
                    output_file.write("Subject: %s\n" %(subject))
                    output_file.write("Body: %s\n" %(body.decode('utf-8')))
                    output_file.write("Email_Sender: %s\n" %(email_from))
                    output_file.write("Email_Receiver: %s\n" %(email_to))
                    output_file.close()

                for one_link in re.findall('https?://[\w./%-]+', email_message.as_string()):
                    print(one_link)
                    exit(0)
                else:
                    continue
if __name__ == "__main__":
    main()

