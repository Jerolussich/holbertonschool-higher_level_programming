#!/usr/bin/python3
"""script that lists all cities from the database hbtn_0e_4_usa"""

import MySQLdb
import sys

db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                     password=sys.argv[2], database=sys.argv[3])


if __name__ == "__main__":
    cursor = db.cursor()

    cursor.execute(
        "SELECT cities.id, cities.name, states.name FROM cities\
            INNER JOIN states ON states.id = cities.state_id ORDER BY cities.id")

    results = cursor.fetchall()

    for items in results:
        print(items)

    cursor.close()

    db.close()
