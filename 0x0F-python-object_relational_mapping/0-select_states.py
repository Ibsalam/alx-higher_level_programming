#!/usr/bin/python3
"""Lists states"""

import MySQLdb
from sys

if __name__ == "__main__":
    dbconn = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                           passwd=sys.argv[2], db=sys.argv[3])
    curr = dbconn.cursor()
    curr.execute("SELECT * FROM states ORDER BY states.id ASC")
    query_rows = curr.fetchall()
    for row in query_rows:
        print(row)
    curr.close()
   dbconn.close()
