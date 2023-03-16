#!/usr/bin/python3

import MySQLdb
import sys

db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                     password="", database=sys.argv[3])

cursor = db.cursor()

cursor.execute(
    "SELECT id, name FROM states WHERE name LIKE '%{}' ORDER BY states.id ASC".format(sys.argv[4]))

result = cursor.fetchall()

for item in result:
    print(item)

cursor.close()
db.close()
