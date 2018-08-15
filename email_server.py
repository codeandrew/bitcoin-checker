#!/usr/bin/env python
import smtplib

from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText

from settings import SENDER_EMAIL, RECEIVER_EMAIL, PASSWORD

email_to = RECEIVER_EMAIL
email_from = SENDER_EMAIL
password = PASSWORD

from_addr = email_from
to_addr = email_to

def main(message,buy,sell):

    subject = 'Bitcoin Price, Buy:%s Sell:%s' % (buy, sell)
    print "sender email:",  SENDER_EMAIL
    msg = MIMEMultipart()
    msg['From'] = from_addr
    msg['To'] = to_addr
    msg['Subject'] = subject

    body = message
    msg.attach(MIMEText(body, 'plain'))
    print "[*] Sending email..."

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(from_addr, password)
        text = msg.as_string()
        server.sendmail(from_addr, to_addr, text)
        print "[*] Email Succesfully Sent!"
        server.quit()

    except Exception as e:
        print "[!!] Error in Sending email", e


if __name__ == '__main__':
    print 'email_server is main file'
    message = "Test Message"
    main(message, "none", "none")
