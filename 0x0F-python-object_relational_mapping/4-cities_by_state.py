#!/usr/bin/python3
"""Lists all cities from the database"""
import MySQLdb
import sys

if __name__ == '__main__':
    db = MySQLdb.connect('localhost', user, password, dbname, port=3306)
    cur = db.cursor()
    cur.execute("")
    rows = cur.fetchall()
    cur.close()
    db.close()
