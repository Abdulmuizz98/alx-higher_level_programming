#!/usr/bin/python3
"""
A script that takes in the name of a state as an argument and
lists all cities of that state, using the database hbtn_0e_4_usa
"""

if __name__ == "__main__":
    import MySQLdb
    import sys

    USERNAME, PASSWORD, DB, statename = sys.argv[1:5]

    db = MySQLdb.connect(host="localhost", port=3306,
                         user=USERNAME, passwd=PASSWORD, db=DB)
    cur = db.cursor()
    cur.execute("SELECT c.name FROM cities AS c \
                 INNER JOIN states AS s ON c.state_id = s.id \
                 WHERE s.name = %s \
                 ORDER BY c.id ", (statename,))
    rows = cur.fetchall()
    cities = [row[0] for row in rows]
    [print(city, end=", ") for city in cities[:-1]]
    print(cities[-1])
