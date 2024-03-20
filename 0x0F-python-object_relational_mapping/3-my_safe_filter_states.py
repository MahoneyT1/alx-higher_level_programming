#!/usr/bin/python3

"""
Script that displays all values in the states table of hbtn_0e_0_usa
where name matches the provided argument, and is AFE from MySQL injection.
Parameters for script: mysql username, mysql password, database name
and state name searched.
Must use the `MySQLdb` module.
Script should connect to a MySQL server runnimg on `localhost` at port `3306`
Must use `format` to create the SQL query with the user input.
Results must be in ascending order by `states.id`.
Code should not be executed when imported.
"""

import MySQLdb
from sys import argv

# connect to the database
db = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=argv[1],
        passwd=argv[2],
        db=argv[3]
        )

# get a cursor, a reference for executing queries, objectify it
cursor = db.cursor()

# safefly capture stateName arg
state_name = argv[4]

# store querry in a var
querry = f"SELECT * FROM states WHERE name = %s "

# execute the querry
cursor.execute(querry, (state_name,))

# fetch the datas in list form
states = cursor.fetchall()

# loop through and print

for state in states:
    if state[1] == argv[4]:
        print(state)

# close the cursor and db

cursor.close()
db.close()
