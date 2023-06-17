#!/usr/bin/python3
"""Displays all values in states table where the name matches the argument"""

if __name__ == '__main__':
    import MySQLdb
    import sys

    a = sys.argv
    db = MySQLdb.connect(host='localhost',
                         user=a[1],
                         passwd=a[2],
                         database=a[3],
                         port=3306)

    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE BINARY '{}'"
                .format(a[4]))
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
