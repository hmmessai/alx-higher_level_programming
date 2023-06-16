#!/usr/bin/python3
"""Searches for entries with the given name but safe from sql injections"""

if __name__ == '__main__':
    import MySQLdb
    import sys

    db = MySQLdb.connect(host='localhost',
                         user=sys.argv[1],
                         passwd=sys.argv[2],
                         database=sys.argv[3],
                         port=3306)
    cur = db.cursor()
    match = sys.argv[4]
    cur.execute("""SELECT * FROM states WHERE name LIKE BINARY %s""",
                (match, ))
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
