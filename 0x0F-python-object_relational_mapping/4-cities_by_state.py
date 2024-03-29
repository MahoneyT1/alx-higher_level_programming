#!/usr/bin/python3

"""
Script that lists all cities from the database hbtn_0e_4_usa.
Parameters for script: mysql username, mysql password, database name.
Must use the `MySQLdb` module.
Script should connect to a MySQL server runnimg on `localhost` at port `3306`
Results must be in ascending order by `cities.id`.
Can only use `execute()` once
Code should not be executed when imported.
"""

import MySQLdb
from sys import argv

# if script it imported as a module,don't run
if __name__ == '__main__':

    # connect to the database
    db = MySQLdb.connect(
            host='localhost',
            port=3306,
            user=argv[1],
            passwd=argv[2],
            db=argv[3]
            )
    # create a cursor
    cursor = db.cursor()

    # create a querry
    querry = """SELECT cities.id, cities.name, states.name
                FROM states
                INNER JOIN cities ON states.id = cities.state_id
                ORDER BY cities.id ASC
                """
    # execute the querry
    cursor.execute(querry)

    # fetch the states
    states = cursor.fetchall()

    # print all
    for state in states:
        print(state)

    # close cursor and database
    cursor.close()
    db.close()
