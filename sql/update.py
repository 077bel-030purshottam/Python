import sqlite3

conn = sqlite3.connect("sqlite.db")
conn.execute('''

update student set std_name="Rohit kumar thakur" where std_id=2



''')

conn.commit()
conn.close()