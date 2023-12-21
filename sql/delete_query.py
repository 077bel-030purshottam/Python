import sqlite3

conn = sqlite3.connect("sqlite.db")
std_id=input("Enter the student id number")
conn.execute("delete from student where std_id="+std_id)
conn.commit()
conn.close()
