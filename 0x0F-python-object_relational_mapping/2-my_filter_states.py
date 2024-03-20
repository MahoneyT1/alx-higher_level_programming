#!/usr/bin/python3
""" This is a script that takes in a argument and displays all vlaues
in the states table of database provided where name matches the argument

it takes 4 argument username, password,database name and state name
it connects to the MySQL Server on local host
using format strin to construct the queries
results should be in asc order
also this script doesnt run while imported
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    # connect the engine by objectifying it

    db = MySQLdb.connect(host='localhost', port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])
    # conect your cursor
    cursor = db.cursor()

    # saving last argv to a var

    state_name = argv[4]

    # create a query
    query = f"SELECT id, name FROM states WHERE name = %s ORDER BY id ASC"

    # execute the command using the cursor as a reference to the database
    cursor.execute(query, (state_name,))

    # fetch all the data
    states = cursor.fetchall()

    # loop through and print the datas
    for state in states:
        if state[1] == state_name:
            print(state)

    # successfully done now close the cursor and db

    cursor.close()
    db.close()
