#!/usr/bin/python3
"""
This module lists all states from the database hbtn_0e_0_usa.
The script takes 3 arguments: mysql username, password and database name.
It uses the MySQLdb module to connect to a MySQL server on localhost.
"""
import MySQLdb
import sys


def select_states():
    """
    Connects to the database and fetches all states sorted by id.
    """
    if len(sys.argv) != 4:
        return

    u_name = sys.argv[1]
    u_pass = sys.argv[2]
    db_name = sys.argv[3]

    try:
        db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=u_name,
            passwd=u_pass,
            db=db_name
        )

        cursor = db.cursor()
        
        cursor.execute("SELECT * FROM states ORDER BY id ASC")
        
        rows = cursor.fetchall()
        for row in rows:
            print(row)

        cursor.close()
        db.close()
    except Exception:
        pass


if __name__ == "__main__":
    select_states()