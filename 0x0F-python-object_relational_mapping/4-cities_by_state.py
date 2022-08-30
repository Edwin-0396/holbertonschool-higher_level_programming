#!/usr/bin/python3
""" script that lists all states from the database hbtn_0e_0_usa: """


if __name__ == '__main__':
    """ Module to select states"""

    import MySQLdb
    import sys

    db = MySQLdb.connect(
        host='localhost', user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    mycursor = db.cursor()
    sql = "SELECT cities.id, cities.name, states.name\
FROM cities JOIN states ON states.id = cities.state_id ORDER BY \
cities.id ASC"

    mycursor.execute(sql)
    myresult = mycursor.fetchall()

    for x in myresult:
        print(x)
