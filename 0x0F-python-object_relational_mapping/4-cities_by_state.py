#!/usr/bin/python3
"""
A script that lists all cities from the database hbtn_0e_4_usa
"""

if __name__ == "__main__":
    import MySQLdb
    import sys

    USERNAME, PASSWORD, DB = sys.argv[1:4]

    db = MySQLdb.connect(host="localhost", port=3306,
                         user=USERNAME, passwd=PASSWORD, db=DB)
    cur = db.cursor()
    cur.execute("SELECT c.id, c.name, s.name FROM cities AS c \
                 INNER JOIN states AS s ON c.state_id = s.id \
                 ORDER BY c.id ")
    rows = cur.fetchall()
    [print(row) for row in rows]
