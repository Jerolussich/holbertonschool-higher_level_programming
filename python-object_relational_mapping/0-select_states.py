#!/usr/bin/python3

import MySQLdb
import sys

db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                     password="", database=sys.argv[3])

cursor = db.cursor()

cursor.execute("""SELECT id, name FROM states
         ORDER BY states.id ASC""")

result = cursor.fetchmany(5)

for item in result:
    print(item)
cursor.close()
db.close()
