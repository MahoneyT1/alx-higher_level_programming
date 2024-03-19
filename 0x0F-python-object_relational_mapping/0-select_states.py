#!/usr/bin/python3
""" Write a script that lists all states from the database hbtn_0e_0_usa """

import MySQLdb
from sys import argv

if __name__ == '__main__':
    
    #connect the database
    db = MySQLdb.connect(
            host='localhost',
            port=3306,
            user=argv[1],
            passwd=argv[2],
            db=argv[3]
            )
    #create a cursor obect
    mycursor = db.cursor()

    #execute command using cursor a reference to database
    mycursor.execute("SELECT * FROM states ORDER BY id ASC")

    rows = mycursor.fetchall()

    for row in rows:
        print(row)

    #close both cursor and database
    mycursor.close()
    db.close()
