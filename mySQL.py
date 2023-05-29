import pymysql
from config import DB_my_password
con = pymysql.connect(host='localhost', user='DB_Admin',
                      password=DB_my_password, db='MySQL')

with con:
    cur = con.cursor()
    cur.execute("SELECT 12*3 FROM Dual")

    rows = cur.fetchall()

    for row in rows:
        print(f"12 * 3 = {row[0]}")
