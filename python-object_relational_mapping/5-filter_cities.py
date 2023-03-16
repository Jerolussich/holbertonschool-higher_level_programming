#!/usr/bin/python3
"""script that takes in the name of a state as an argument and lists all cities of that state, using the database hbtn_0e_4_usa"""

import MySQLdb
import sys

db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                     password="", database=sys.argv[3])


if __name__ == "__main__":

    cursor = db.cursor()

    cursor.execute(
        "SELECT cities.name FROM cities INNER JOIN states ON cities.state_id = states.id WHERE states.name = %s ORDER BY cities.id", ((sys.argv[4]), ))

    result = cursor.fetchall()

    size = len(result)
    for idx, item in enumerate(result):

        if idx != size - 1:
            print(f"{item[0]}, ", end="")
        else:
            print(f"{item[0]}")

    cursor.close()
    db.close()
