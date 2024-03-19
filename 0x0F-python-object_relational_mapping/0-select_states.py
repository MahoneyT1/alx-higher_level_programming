import MySQLdb
from sys import argv

""" Write a script that lists all states from the database hbtn_0e_0_usa """

if __name__ == '__main__':
    db = MySQLdb.connect(
            host="localhost",
            user=argv[1],
            passwd=argv[2],
            db=argv[3],
            port=3306
            )

    mycursor = db.cursor()

    mycursor.execute("SELECT * FROM states")
    rows = mycursor.fetchall()

    for row in rows:
        print(row)

    mycursor.close()
    db.close()
