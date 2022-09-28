import MySQLdb

db = MySQLdb.connect(
    host="localhost",
    user="pvrts",
    passwd="123",
    db="tonika_db"
)

c = db.cursor()
c.execute("INSERT INTO authors (name, description) VALUES (%s, %s);", ('Author', 'Description'))
c.execute("SELECT * FROM authors")
print(c.fetchall())
c.execute("TRUNCATE authors")
db.commit()
c.close()
db.close()
