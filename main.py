from selenium import webdriver
from datetime import date, datetime
import sqlite3

URL = "https://intranet.inkua.de/dashboard"

driver = webdriver.Chrome()
driver.get(URL)


def get_time():
    now = datetime.now()

    current_time = now.strftime("%H:%M:%S")
    return current_time


def get_date():
    today = date.today()
    date_data = today.strftime("%d/%m/%Y")
    return date_data


def loading_site():
    navigationStart = driver.execute_script(
        "return window.performance.timing.navigationStart"
    )
    responseStart = driver.execute_script(
        "return window.performance.timing.responseStart"
    )
    domComplete = driver.execute_script("return window.performance.timing.domComplete")

    backendPerformance = responseStart - navigationStart
    frontendPerformance = domComplete - responseStart

    print("Back End: %s" % backendPerformance)
    print("Front End: %s" % frontendPerformance)

    driver.quit()
    return frontendPerformance


def write_db(load, date, time):

    con = sqlite3.connect("./example.db")
    cur = con.cursor()

    # detecta si hay una tabla llamada loggins, si no la hay la crea

    cur.execute(
        """CREATE TABLE IF NOT EXISTS loggins    (date text, time text, delay text)"""
    )

    # inserta los valores, guarda los cambios
    cur.execute(
        """INSERT INTO loggins VALUES (?,?,?)""",
        (date, time, load),
    )

    con.commit()

    # imprime los datos de la tabla (a modo de testeo)
    for row in cur.execute("SELECT * FROM loggins ORDER BY date"):
        print(row)

    con.close()


def main():
    # conseguir datos del tiempo
    time = get_time()
    date = get_date()

    # conseguir tiempo de carga
    loading_web = loading_site()

    # escribir en la base de datos fecha, hora, tiempo de carga
    write_db(loading_web, date, time)


main()
