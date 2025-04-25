import psycopg2


conn = psycopg2.connect(host = 'localhost',
    dbname = 'Database',
    user = 'postgres',
    password = 'Pass@STU2015',
    port = 1671  )
cur = conn.cursor()

cur.execute("SELECT * FROM phonebook")

rows = cur.fetchall()

for row in rows:
    print(row)
cur.close()
conn.close()