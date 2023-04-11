from app import mysql

def config():
    sql = ""
    cur = mysql.connection.cursor()
    cur.execute(sql)
    mysql.connection.commit()
    cur.close()