#!/usr/bin/python3
"""Matches an argument taken with the values of the states table"""
import MySQLdb
import sys

if __name__ == '__main__':
    argv = sys.argv
    user = argv[1]
    password = argv[2]
    dbname = argv[3]
    name = argv[4]
    db = MySQLdb.connect('localhost', user, password, dbname, port=3306)
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE BINARY '{}' ORDER BY id ASC".format(name))
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
