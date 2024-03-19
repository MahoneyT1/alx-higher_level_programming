#!/usr/bin/python3

"""
Script that lists all states with a name starting with 'N'
from the database hbtn_0e_0_usa.
Parameters for script: mysql username, mysql password, database name.
Must use the `MySQLdb` module.
Script should connect to a MySQL server runnimg on `localhost` at port `3306`
Results must be in ascending order by `states.id`.
Code should not be executed when imported.
"""

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
