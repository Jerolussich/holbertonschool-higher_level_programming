#!/usr/bin/python3
"""takes the name of a state as argument and lists all cities of that state"""

if __name__ == "__main__":

    import MySQLdb
    import sys

    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         password=sys.argv[2], database=sys.argv[3])
    cursor = db.cursor()

    cursor.execute(
        "SELECT cities.name FROM cities INNER JOIN states ON \
        cities.state_id = states.id WHERE \
        states.name = %s ORDER BY cities.id", ((sys.argv[4]), ))

    result = cursor.fetchall()

    size = len(result)

    if size != 0:
        for idx, item in enumerate(result):

            if idx != size - 1:
                print(f"{item[0]}, ", end="")
            else:
                print(f"{item[0]}")
    else:
        print("")

    cursor.close()
    db.close()
