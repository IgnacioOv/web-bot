from selenium import webdriver

import sqlite3

URL = "https://intranet.inkua.de/dashboard"


def connect_site():
    pass


def write_db():
    con = sqlite3.connect("./example.db")
    cur = con.cursor()

    # cur.execute("""CREATE TABLE loggins    (date text, time text, delay text)""")
    cur.execute("""INSERT INTO loggins VALUES ('2006-01-05','12pm','12ms')""")
    cur.execute("""INSERT INTO loggins VALUES ('2016-01-05','12pm','12ms')""")
    for row in cur.execute("SELECT * FROM loggins ORDER BY date"):
        print(row)

    con.commit()
    con.close()
    pass


def main():
    # conectar con la pagina
    print("anda")
    connect_site()
    write_db()


main()
