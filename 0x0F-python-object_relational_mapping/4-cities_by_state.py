#!/usr/bin/python3
"""Lists all cities from the database"""

if __name__ == '__main__':
    import MySQLdb
    import sys

    db = MySQLdb.connect(host='localhost',
                         user=sys.argv[1],
                         passwd=sys.argv[2],
                         database=sys.argv[3],
                         port=3306)
    cur = db.cursor()
    cur.execute("""SELECT cities.id, cities.name, states.name
                    FROM cities
                    INNER JOIN states
                    WHERE cities.state_id = states.id
                    ORDER BY cities.id""")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
