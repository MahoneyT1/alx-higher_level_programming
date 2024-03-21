#!/usr/bin/python3

"""
This script takes in the name if a state as an argument and liss
all the cities of that state, using the database hbtn_0e_4_usa

It takes 4 arguments `username` `password` `database name` `state_name`,
using the module `import MySQL` running the server on `localhost` on
port `3306`. results must be in `ASC`, you can only use `execute()` once

"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    # connect engine by creating the instance
    db = MySQLdb.connect(
            host='localhost',
            port=3306,
            user=argv[1],
            passwd=argv[2],
            db=argv[3]
            )
    # create an instance of a cursor object
    cursor = db.cursor()

    # store the name of the state in a variable
    state_name = argv[4]

    querry = """
             SELECT cities.name
             from states
             INNER JOIN cities ON states.id = cities.state_id
             WHERE states.name = %s
             ORDER BY cities.id ASC

             """
    # execute the querry
    cursor.execute(querry, (state_name,))

    # fetch the data returned

    results = cursor.fetchall()

    newS = [result[0] for result in results]
    print(', '.join(newS))

    # close the cursor and the db
    cursor.close()
    db.close()
