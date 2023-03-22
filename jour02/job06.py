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
        X = 0
        for i in c.fetchall():
            X += i[-1]
        print("La capacite de toutes les salles est de " + str(X))
