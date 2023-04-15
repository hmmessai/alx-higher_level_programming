#!/usr/bin/python3
"""Lists all states with a name starting with 'N' from the database"""

if __name__ == '__main__':
    import MySQLdb
    import sys

    argv = sys.argv
    user = argv[1]
    password = argv[2]
    dbname = argv[3]
    db = MySQLdb.connect('localhost', user, password, dbname, port=3306)
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name REGEXP '^N' ORDER BY id ASC")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
