import MySQLdb
from sys import argv

"""
Write a script that lists all states from the database hbtn_0e_0_usa
"""
if __name__ == '__main__':
    db = MySQLdb.connect(
            host="localhost",
            user=argv[1],
            passwd=argv[2],
            db=argv[3],
            port=3306
            )

    mycursor = db.cursor()

    mycursor.execute("SELECT id, name FROM states ORDER BY id ASC ")

    for i in mycursor:
        print(i)

    mycursor.close()
    db.close()
