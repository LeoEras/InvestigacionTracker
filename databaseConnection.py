import _mysql

db=_mysql.connect("localhost","root","1234","investigacion")
db.query("""Select * From datos where id < 5""")
r = db.store_result()
print(r.fetch_row())
