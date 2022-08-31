#!/usr/bin/python3
""" script that lists all states from the database hbtn_0e_0_usa: """


from re import M


if __name__ == '__main__':
    """ Module to select states"""

    import MySQLdb
    import sys

    db = MySQLdb.connect(
        host='localhost', user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    mycursor = db.cursor()
    st = sys.argv[4].split('\'')
    mycursor.execute("SELECT cities.name \
FROM cities JOIN states ON cities.state_id = states.id \
WHERE states.name = '{}' \
ORDER BY cities.id ASC".format(st[0]))
    myresult = mycursor.fetchall()
    for x in range(0, len(myresult)):
        if x < (len(myresult) - 1):
            print(myresult[x][0], end=", ")
        else:
            print(myresult[x][0], end="")
    print()
