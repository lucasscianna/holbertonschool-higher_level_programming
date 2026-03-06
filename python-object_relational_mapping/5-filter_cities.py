#!/usr/bin/python3
"""
Lists all cities of a specific state from the database hbtn_0e_4_usa.
The state name is passed as an argument and protected from SQL injection.
"""
import MySQLdb
import sys


def filter_cities():
    """
    Connects to the database and displays cities of a given state
    separated by commas.
    """
    if len(sys.argv) == 5:
        u_name = sys.argv[1]
        u_pass = sys.argv[2]
        db_name = sys.argv[3]
        state_name = sys.argv[4]

        db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=u_name,
            passwd=u_pass,
            db=db_name
        )

        cursor = db.cursor()

        query = "SELECT cities.name FROM cities \
JOIN states ON cities.state_id = states.id \
WHERE states.name = %s ORDER BY cities.id ASC"

        cursor.execute(query, (state_name,))

        rows = cursor.fetchall()

        cities_list = [row[0] for row in rows]
        print(", ".join(cities_list))

        cursor.close()
        db.close()


if __name__ == "__main__":
    filter_cities() 