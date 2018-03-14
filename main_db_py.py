import sqlite3
import os.path

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, "people.db")

conn = sqlite3.connect(db_path)
cursor = conn.cursor()


def insert(phone=9276665858, dob='10.00.1202'):
    
    name = input("name->")
    sname = input("sname->")
    c = input("do you have phone? -> number/n")
    if c != "n":
        phone = c
    cursor.execute("""INSERT INTO people (name, 
                    second_name, phone, dob) VALUES (
                    '{}', '{}', '{}', '{}')""".format(name, sname, phone, dob))
    conn.commit()
    
    
def remove_doubles():

    s = "DELETE FROM people WHERE id_people NOT IN " \
    "(SELECT id_people FROM people GROUP BY phone)"
    cursor.execute(s)


print("Here's all people in the table:")
for row in cursor.execute("SELECT * FROM people ORDER BY id_people"):
    print(row)
print("=*=*=*=*=")
