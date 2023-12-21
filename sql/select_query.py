import sqlite3

conn = sqlite3.connect("sqlite.db")
data=conn.execute('SELECT * FROM STUDENT')
print("student_id\tstduent_name\t\t\tstudent_class\t\t\tstudent_email")
for n in data:
    print("\t",n[0],"\t",n[1],"\t\t\t",n[2],"\t\t\t",n[3],"\t")


print("\n\n")
# filtering data of your choice 
std_name=input("Enter the student name ")
std_class=input("Enter the student class ")
# data=conn.execute("select * from student where std_name='"+std_name+"'")
# data=conn.execute("select * from student where std_name like'%"+std_name+"%'")
# there are two operation like and and the next is or 
data=conn.execute("select * from student where std_name like'%"+std_name+"%'and std_class='"+std_class+"'")
for n in data:
    print("\t",n[0],"\t",n[1],"\t\t\t",n[2],"\t\t\t",n[3],"\t")
