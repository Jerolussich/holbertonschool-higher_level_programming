#!/usr/bin/python3
"""script that takes in an argument and displays all values in the states table of hbtn_0e_0_usa where name matches the argument"""
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
