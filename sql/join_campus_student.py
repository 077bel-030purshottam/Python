import sqlite3

conn = sqlite3.connect("sqlite.db")
# data=conn.execute('SELECT  c.std_id, s.std_name,c.std_result FROM campus as c inner join student as s on c.std_id=s.std_id') # for full table 
data=conn.execute('SELECT  c.std_id, s.std_name,c.std_result FROM campus as c left join student as s on c.std_id=s.std_id')# for left join only 
# data=conn.execute('SELECT  c.std_id, s.std_name,c.std_result FROM campus as c right join student as s on c.std_id=s.std_id')# for right join only 
print("student_id\t\tstd_name\t\tstd_result")
for n in data:
   print(n[0],"\t\t",n[1],"\t\t\t",n[2])


conn.close()