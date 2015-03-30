#!/usr/bin/python

import smtplib
import string
import sys

LOGIN = ""
PASSWORD = ""
SMTP_SERVER = ""
SMTP_PORT = 25
TO = ""
FROM = ""
TEMP_LOG = ""
TEXT = ""

with open(TEMP_LOG,"r") as f:
        SUBJ = f.readline()
        for line in f:
                TEXT = string.join((
                        TEXT,
                        line
                        ),"\r\n")

BODY = string.join((
        "From: %s" % FROM,
        "To: %s" % TO,
        "Subject: %s" % SUBJ,
        "",
        TEXT
        ), "\r\n")
try:
        server = smtplib.SMTP(SMTP_SERVER,SMTP_PORT)
        server.login(LOGIN, PASSWORD)
        server.sendmail(FROM, [TO], BODY)
        print "E-mail inviata correttamente."
except SMTPException:
        print "Errore: Invio E-mail fallito / impossibile. verificare la situazione."