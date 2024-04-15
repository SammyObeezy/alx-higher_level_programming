#!/usr/bin/python3
"""This is a script that lists all states from DB htb_0e_0_usa"""
import MySQLdb
from sys import argv


def main():
    # The following code should not be executed when imported
    if __name__ == '__main__':
        # Make a connection to the database now
        db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=argv[1],
            passwd=argv[2],
            db=argv[3]
        )

        # This gives us the ability to have separate multiple working environments
        # with the same connection to the database
        cur = db.cursor()
        cur.execute("SELECT * FROM states")

        rows = cur.fetchall()
        for i in rows:
            print(i)

        # Clean up the entire process
        cur.close()
        db.close()


if __name__ == '__main__':
    main()
