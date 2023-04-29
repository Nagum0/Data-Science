import mysql.connector
import random

""" Gen student ID """
def genStudentID(gradeIndex: str) -> str:
    ID = gradeIndex
    abc = "QWERTYUIOPASDFGHJKLZXCVBNM"
    nums = "123456789"

    for i in range(4):
        if i % 2 == 0:
            randLetter = random.randrange(len(abc))
            ID = ID + abc[randLetter]
        else:
            randNum = random.randrange(len(nums))
            ID = ID + nums[randNum]

    return ID

""" Password generator """
def passwordGenerator() -> str:
    genPass = ""
    abc = "qwertyuiopasdfghjklzxcvbnm"
    nums = "123456789"

    for i in range(5):
        if i % 2 == 0:
            randLetter = random.randrange(len(abc))
            genPass = genPass + abc[randLetter]
        else:
            randNum = random.randrange(len(nums))
            genPass = genPass + nums[randNum]

    return genPass

""" Add student """
def addStudent(argCursor: any, argDB: any) -> None:
    lastName = str(input("Last name $ "))
    firstName = str(input("First name $ "))
    password = passwordGenerator()
    address = str(input("Address $ "))
    grade = str(input("Grade $ "))
    age = int(input("Age $ "))
    classes = "Default"
    specClasses = str(input("Special classes $ "))
    studentID = genStudentID(grade)

    val = (studentID, password, lastName, firstName, address, grade, age, classes, specClasses)

    argCursor.execute("INSERT INTO Students VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)", val)
    argDB.commit()

""" Gen teacher ID """
def genTeacherID() -> str:
    ID = ""
    abc = "QWERTYUIOPASDFGHJKLZXCVBNM"
    nums = "123456789"

    for i in range(5):
        if i % 2 == 0:
            randLetter = random.randrange(len(abc))
            ID = ID + abc[randLetter]
        else:
            randNum = random.randrange(len(nums))
            ID = ID + nums[randNum]

    return ID

""" Add teacher """
def addTeacher(argCursor: any, argDB: any) -> None:
    lastName = str(input("Last name $ "))
    firstName = str(input("First name $ "))
    password = passwordGenerator()
    address = str(input("Address $ "))
    age = int(input("Age $ "))
    subjects = str(input("Subjects $ "))
    teacherID = genTeacherID()

    val = (teacherID, password, lastName, firstName, address, age, subjects)

    argCursor.execute("INSERT INTO Teachers VALUES (%s, %s, %s, %s, %s, %s, %s)", val)
    argDB.commit()