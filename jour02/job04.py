import mysql

connection_params = {
    'host': "localhost",
    'user': "root",
    'password': "root",
    'database': "laplateforme",
}

with mysql.connector.connect(**connection_params) as db :
    db.autocommit = True
    with db.cursor() as c:
        c.execute("SELECT * FROM salles")
        for i in c.fetchall():
            print(i)
        pass
