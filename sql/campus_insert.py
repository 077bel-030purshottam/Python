import sqlite3

conn = sqlite3.connect("sqlite.db")

ins = """
insert into campus (std_result)
values ("fail")

"""
conn.execute(ins)
conn.commit()
conn.close()
