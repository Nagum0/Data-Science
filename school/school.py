import mysql.connector
from admin import *

""" Menu """
def menu() -> None:
    print("------------------------------------------------")
    print("\t\t0.Add student")
    print("\t\t1.Add teacher")
    print("\t\t2.Remove student")
    print("\t\t3.Remove teacher")
    print("\t\t4.Find student")
    print("\t\t5.Find teacher")
    print("\t\t6.Exit")

""" MySQL Connection """
mainDB = mysql.connector.connect(
    host="b9syngpkzy7gldxwdbjk-mysql.services.clever-cloud.com",
    user="uov5wkc5efcarh2f",
    password="tVaFBwD3ZiYPhAs4xWXF",
    database="b9syngpkzy7gldxwdbjk"
)

""" MySQL Cursor """
mainCursor = mainDB.cursor()

if __name__ == "__main__":
    cmd = ""

    menu()

    while cmd != 6:
        cmd = int(input("$ "))
        
        if cmd == 6:
            print("------------------------------------------------")
            break
        elif cmd == 0:
            addStudent(mainCursor, mainDB)
            continue
        elif cmd == 1:
            addTeacher(mainCursor, mainDB)
            continue
        else:
            print("Invalid command")
            continue