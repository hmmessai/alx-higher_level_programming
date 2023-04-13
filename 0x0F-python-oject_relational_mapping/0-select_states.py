#!/usr/bin/python3
"""Lists all states from the database hbtn_0e_0_usa"""

if __name__ == '__main__':
    import MySQLdb
    import sys
    argv = sys.argv
    user = argv[1]
    password = argv[2]
    dbname = argv[3]
    db = MySQLdb.connect('localhost', user, password, dbname)
    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    rows = cur.fetchall()
    for row in rows:
        print(row)
