import sqlite3

conn = sqlite3.connect("sqlite.db")

ins = """

insert into  student(std_name,std_class,std_email)
values ("purshottam Sthakur","12th","rohit528gmail.com")

"""
conn.execute(ins)
conn.commit()
conn.close()