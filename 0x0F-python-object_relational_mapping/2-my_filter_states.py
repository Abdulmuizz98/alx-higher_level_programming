#!/usr/bin/python3
"""
A script that takes in an argument and displays all values in the
states table of hbtn_0e_0_usa where name matches the argument.
"""

if __name__ == "__main__":
    import MySQLdb
    import sys

    USERNAME, PASSWORD, DB, statename = sys.argv[1:5]

    db = MySQLdb.connect(host="localhost", port=3306,
                         user=USERNAME, passwd=PASSWORD, db=DB)
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name='{}'
                ORDER BY id".format(statename))
    rows = cur.fetchall()
    [print(row) for row in rows]
