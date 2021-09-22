import sqlite3 as db

conn = db.connect('bd.db')

def fun1(name):
    with db.connect("bd.db") as con:
        cur = con.cursor()

        cur.execute("""CREATE TABLE """+ name +"""(
        chtoto1 TEXT
        chtoto2 INTEGER
        )""")

fun1("t")


def fun2(name):
    with db.connect("bd.db") as con:
        cur = con.cursor()
        cur.execute("""DROP TABLE """+name+""" """)
        con.commit()
fun2("t")


#3 не поняла что делать 
