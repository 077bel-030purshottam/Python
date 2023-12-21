import sqlite3

conn = sqlite3.connect("sqlite.db")
conn.execute(
    """
create table campus (
 std_id int auto_increment primary key,
std_result varchar (50)
             
 )


"""
)
