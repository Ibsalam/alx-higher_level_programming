#!/usr/bin/python3
"""Lists states"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    dbconn = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                           passwd=argv[2], db=argv[3], charset="utf8")
    curr = dbconn.cursor()
    curr.execute("SELECT * FROM states ORDER BY states.id ASC")
    query_rows = curr.fetchall()
    for row in query_rows:
        print(row)
    curr.close()
   dbconn.close()
