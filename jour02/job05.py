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
        c.execute("SELECT * FROM etage")
        X = 0
        for i in c.fetchall():
            X += i[-1]
        print("La superficie de La Plateforme est de " + str(X) + " m2.")
