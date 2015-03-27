import MySQLdb


#        replace mysql.server with "localhost" if you are running via your own server!
#                        server       MySQL username	MySQL pass  Database name.
conn = MySQLdb.connect("mysql.server","beginneraccount","cookies","beginneraccount$tutorial")

c = conn.cursor()

c.execute("SELECT * FROM taula")

rows = c.fetchall()

for eachRow in rows:
    print eachRow
