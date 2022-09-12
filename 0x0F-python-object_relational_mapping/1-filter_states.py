#!/usr/bin/python3
"""
Module that lists all states with name starting with "N" in a database,
given a username, a password and the said database.
"""

if __name__ == "__main__":
    import MySQLdb
    import sys

    USERNAME, PASSWORD, DB = sys.argv[1:4]

    db = MySQLdb.connect(host="localhost", port=3306,
                         user=USERNAME, passwd=PASSWORD, db=DB)
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE BINARY 'N%' ORDER BY id ")
    rows = cur.fetchall()
    [print(row) for row in rows]
