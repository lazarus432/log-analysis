#!/usr/bin/env python2.7
# database python code to connect to newsdata.sql

import psycopg2

DBNAME = "news"

# connect to the database
db = psycopg2.connect(database=DBNAME)
c = db.cursor()
# query to get infomation from a created view
q = ("SELECT * FROM titleFinal")
c.execute(q)
rows = c.fetchall()
print "\nThe most popular three articles of all time:\n"
for row in rows:
    print "   ", row[0], "---", row[1], "views"

# second query to get additional information from a created view
q1 = ("SELECT * FROM authorFinal")
c.execute(q1)
rows1 = c.fetchall()
print "\nThe most popular authors of all time:\n"
for row in rows1:
    print "   ", row[0], "---", row[1], "views"

# third query to get additional information from a created view
q2 = ("SELECT * FROM errorfinal")
c.execute(q2)
rows2 = c.fetchall()
print "\nDays where more than 1 percent requests lead to error:\n"
for row in rows2:
    print "   ", row[0], "---", '{:.1f}%'.format(row[1] * 100), "errors"

db.close()
