import MySQLdb
import time

#        replace mysql.server with "localhost" if you are running via your own server!
#                        server       MySQL username	MySQL pass  Database name.
conn = MySQLdb.connect("mysql.server","beginneraccount","cookies","beginneraccount$tutorial")

c = conn.cursor()

username='python'

tweet='man im so cool'

c.execute("INSERT INTO taula (time, username, tweet) VALUES (%s,%s,%s)",
            (time.time(), username, tweet))

conn.commit()

c.execute("SELECT * FROM taula")

rows = c.fetchall()

for eachRow in rows:
    print eachRow
