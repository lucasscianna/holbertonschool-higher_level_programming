#!/usr/bin/python3
"""
Lists all values in the states table of hbtn_0e_0_usa
where name matches the argument.
"""
import MySQLdb
import sys


def filter_by_user_input():
    """
    Connects to the database and filters states by user input.
    """
    if len(sys.argv) == 5:
        user = sys.argv[1]
        passwd = sys.argv[2]
        db_name = sys.argv[3]
        state_searched = sys.argv[4]

        db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=user,
            passwd=passwd,
            db=db_name
        )

        cursor = db.cursor()

        query = "SELECT * FROM states WHERE name LIKE BINARY '{}' \
ORDER BY id ASC".format(state_searched)
        
        cursor.execute(query)

        rows = cursor.fetchall()
        for row in rows:
            print(row)

        cursor.close()
        db.close()


if __name__ == "__main__":
    filter_by_user_input()