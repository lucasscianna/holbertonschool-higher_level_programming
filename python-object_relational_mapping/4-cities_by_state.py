#!/usr/bin/python3
"""
Lists all cities from the database hbtn_0e_4_usa.
The script joins the cities and states tables.
"""
import MySQLdb
import sys


def list_cities():
    """
    Connects to the database and fetches cities with their state names.
    """
    if len(sys.argv) == 4:
        u_name = sys.argv[1]
        u_pass = sys.argv[2]
        db_name = sys.argv[3]

        db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=u_name,
            passwd=u_pass,
            db=db_name
        )

        cursor = db.cursor()

        cursor.execute("SELECT cities.id, cities.name, states.name \
FROM cities JOIN states ON cities.state_id = states.id \
ORDER BY cities.id ASC")

        rows = cursor.fetchall()
        for row in rows:
            print(row)

        cursor.close()
        db.close()


if __name__ == "__main__":
    list_cities()