#!/usr/bin/python3
"""Lists all states with a name starting with N"""
import MySQLdb
import sys

if __name__ == '__main__':
    a = sys.argv
    db = MySQLdb.connect(host='localhost',
                         user=a[1],
                         passwd=a[2],
                         database=a[3],
                         port=3306)
    cur = db.cursor()
    cur.execute("""SELECT * FROM states WHERE name LIKE BINARY 'N%' ORDER BY states.id""")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
