import sqlite3
import Databases
from Employee import Employee

def registration():
    while(True):
        surname = str(input("What is your Surname?\n")).capitalize()
        if not surname.isalpha():
            print("Your name must consist of letters only")
        else:
            print("Thank you for entering your Surname.")
            break

    while(True):
        firstname = str(input("What is your Name?\n")).capitalize()
        if not firstname.isalpha():
            print("Your name must consist of letters only")
        else:
            print("Thank you for entering your Name.")
            break

    while(True):
        try:
            day = int(input("Your birthday.\nDay: "))
            if day > 0 and day < 31:
                break
            else:
                continue
        except:
            print("Enter number")
            continue

    while(True):
        try:
            month = int(input("Month: "))
            if month > 0 and month < 13:
                break
            else:
                continue
        except:
            print("Enter number")
            continue

    while(True):
        try:
            year = int(input("Year: "))
            if year > 1899 and year < 2024:
                break
            else:
                continue
        except:
            print("Enter number")
            continue

    while(True):
        login = str(input("Come up with a Username:\n "))
        if not login.isalpha():
            print("Your name must consist of letters only")
        else:
            break

    while (True):
        password = (input("Come up with a password:\n "))
        if not password.isdigit():
            print("Your name must consist of letters only")
        else:
            break
    birthday = f"{day}.{month}.{year}"
    tt = Employee(surname, firstname, birthday)
    tt.new_table()
    gg = tt.adding('workers')
    Databases.Database.executequery(gg)

registration()