#!/usr/bin/python

import whois
from datetime import datetime
from sys import argv,exit

now = datetime.now()

domain = argv[1]

w = whois.query(domain)
w.expiration_date = w.expiration_date
domain_expiration_date = str(w.expiration_date.day) + '/' + str(w.expiration_date.month) + '/' + str(w.expiration_date.year)
timedelta = w.expiration_date - now
print (timedelta.days)
