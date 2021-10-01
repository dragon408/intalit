import sqlite3 as db

conn = db.connect('base.db')

def create(name_table, name1, type1, name2, type2, name3, type3):
    with db.connect("base.db") as con:
        cur = con.cursor()

        cur.execute("""CREATE TABLE """+ name_table +"""(
        """+ name1 +""" """+ type1 +"""
        """+ name2 +""" """+ type2 +"""
        """+ name3 +""" """+ type3 +"""
        )""")
        con.commit()

def create2(name_table, name1, type1, name2, type2, name3, type3, name4, type4):
    with db.connect("base.db") as con:
        cur = con.cursor()

        cur.execute("""CREATE TABLE """+ name_table +"""(
        """+ name1 +""" """+ type1 +"""
        """+ name2 +""" """+ type2 +"""
        """+ name3 +""" """+ type3 +"""
        """+ name4 +""" """+ type4 +"""
        )""")
        con.commit()

create("products", "ID", "INTEGER", "name", "TEXT", "price", "INTEGER")
create("Users", "ID", "INTEGER", "name", "TEXT", "type", "INTEGER")
create2("Clients", "ID", "INTEGER", "name", "TEXT", "telephone", "INTEGER", "purchases", "INTEGER")


