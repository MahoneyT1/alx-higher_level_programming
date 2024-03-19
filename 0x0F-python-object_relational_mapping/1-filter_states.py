#!/usr/bin/python3
"""A script that lists all states with a name starting with N (upper N)"""

import MySQLdb
from sys import argv

if __name__ == '__main__':

    # connect to the database
    db = MySQLdb.connect(
            host='localhost',
            port=3306,
            user=argv[1],
            passwd=argv[2],
            db=argv[3]
            )
    # create a cursor object as a reference to the database
    mycursor = db.cursor()

    # fetch data from data-base by name starting with N

    mycursor.execute("SELECT id, name FROM states WHERE name LIKE 'N%'
                     ORDER BY id ASC")
    # print the roles

    rows = mycursor.fetchall()

    for row in rows:
        print(row)

    # close database and cursor

    mycursor.close()
    db.close()
