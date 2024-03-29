#!/usr/bin/python3
"""takes in arguments and displays all values in the states table"""
import MySQLdb
import sys

if __name__ == '__main__':

    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         password=sys.argv[2], database=sys.argv[3])

    cursor = db.cursor()

    cursor.execute(
        "SELECT * FROM states WHERE name LIKE %s \
        ORDER BY states.id ASC", (sys.argv[4], ))

    result = cursor.fetchall()

    for item in result:
        print(item)

    cursor.close()
    db.close()
