#!/usr/bin/python3
"""Searches the states table in the db for the argument entered
    But, safe from MySQL injections"""

import MySQLdb
import sys

if __name__ == '__main__':
    user = sys.argv[1]
    password = sys.argv[2]
    dbname = sys.argv[3]
    name = sys.argv[4]
    db = MySQLdb.connect('localhost', user, password, dbname, port=3306)
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE %s", (name, ))
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
