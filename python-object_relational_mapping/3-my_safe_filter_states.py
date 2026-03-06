#!/usr/bin/python3
"""
Lists all values in the states table of hbtn_0e_0_usa
where name matches the argument, safe from SQL injection.
"""
import MySQLdb
import sys


def safe_filter_states():
    """
    Connects to the database and filters states using
    parameterized queries to prevent SQL injection.
    """
    if len(sys.argv) == 5:
        u_name = sys.argv[1]
        u_pass = sys.argv[2]
        db_name = sys.argv[3]
        state_searched = sys.argv[4]

        db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=u_name,
            passwd=u_pass,
            db=db_name
        )

        cursor = db.cursor()

        # Le secret : on utilise %s comme placeholder et on passe
        # la variable dans un tuple comme second argument de execute()
        query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
        cursor.execute(query, (state_searched,))

        rows = cursor.fetchall()
        for row in rows:
            print(row)

        cursor.close()
        db.close()


if __name__ == "__main__":
    safe_filter_states()