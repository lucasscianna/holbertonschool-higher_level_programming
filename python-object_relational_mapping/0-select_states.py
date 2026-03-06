#!/usr/bin/python3
"""Lists all states from the database hbtn_0e_0_usa"""
import MySQLdb
import sys

if __name__ == "__main__":
    """Connect to the DB the command line arguments"""
    db = MySQLdb.connect(
        host="localhost",
        port=3310,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )

    cur = db.cursor()
    cur.execute("SELECT id, name FROM states ORDER BY states.id ASC;")

    query_rows = cur.fetchall()

    for rows in query_rows:
        print(rows)

    cur.close()
    db.close()