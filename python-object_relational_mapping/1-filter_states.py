#!/usr/bin/python3
"""script that lists all states with a name starting with N (upper N)"""

import MySQLdb
import sys

if __name__ == '__main__':
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         password="", database=sys.argv[3])

    cursor = db.cursor()

    cursor.execute(
        "SELECT id, name FROM states WHERE name LIKE \
        'N%' ORDER BY states.id ASC")

    result = cursor.fetchall()

    for item in result:
        if item[1][0] == 'N':
            print(item)

    cursor.close()
    db.close()
