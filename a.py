from datetime import datetime, timedelta
import sys
import re
import MySQLdb

activity = {}

conn = MySQLdb.connect(host= "localhost", user="root", passwd="1234", db="Nuevo")
x = conn.cursor()
x.execute("""SELECT * FROM Application""")
for item in x.fetchall():
    activity[item[1]] = item[0]

print(activity["Blast"])
