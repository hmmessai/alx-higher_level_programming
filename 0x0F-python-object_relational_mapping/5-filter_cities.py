#!/usr/bin/python3
""" Lists all cities of the state 
    that has the same name as the inserted name"""

if __name__ == '__main__':
    import MySQLdb
    import sys

    db = MySQLdb.connect(host='localhost',
                         user=sys.argv[1],
                         passwd=sys.argv[2],
                         database = sys.argv[3],
                         port=3306)
    cur = db.cursor()
    cur.execute("""SELECT cities.name 
                FROM cities
                INNER JOIN states
                ON cities.state_id = states.id
                WHERE states.name LIKE %s""", (sys.argv[4], ))
    rows = cur.fetchall()
    temp = list(row[0] for row in rows)
    print(*temp, sep=", ")
    cur.close()
    db.close()
