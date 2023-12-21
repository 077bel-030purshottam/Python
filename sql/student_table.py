import sqlite3

conn = sqlite3.connect("sqlite.db")
conn.execute(
    """

create table student(

    std_id INT auto_increment primary key,
    std_name varchar(50),
    std_class varchar(10),
    std_email varchar(30)

)



"""
)
conn.close()
