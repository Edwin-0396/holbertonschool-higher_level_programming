#!/usr/bin/python3
# script that lists all states from the database hbtn_0e_0_usa:

import MySQLdb
import sys

db = MySQLdb.connect(
    host='localhost', user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
mycursor = db.cursor()

sql = "SELECT * FROM states ORDER BY states.id ASC"

mycursor.execute(sql)
myresult = mycursor.fetchall()

for x in myresult:
    print(x)
