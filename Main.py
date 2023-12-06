import sqlite3

help = "Command List: /h - Show full list of commands, /n - Create new user, /l - Login to user, /e - Exit"

db = sqlite3.connect('User.db')
sql = db.cursor()
sql.execute("""CREATE TABLE IF NOT EXISTS users (
    username TEXT,
    password TEXT,
    birthday_year INT,
    birthday_month INT,
    birthday_day INT
    )""")
db.commit()


def reg():
    while (True):
        username = str(input("Come up with username: "))
        if not username.isalpha():
            print("Your username must consist of letters only")
        else:
            break

    while (True):
        password = input("Come up with password: ")
        if not password.isdigit():
            print("Your password must consist of numbers only")
        else:
            break

    while (True):
        try:
            birthday_year = int(input("Enter birthday year (1801-2023): "))
            if not birthday_year > 1800 and birthday_year < 2024:
                print("Your birthday year must consist of 1801-2023 only")
                continue
            else:
                break
        except:
            print("Your birthday year must consist of numbers only")
            continue

    while (True):
        try:
            birthday_month = int(input("Enter birthday month (1-12): "))
            if not birthday_month > 0 and birthday_month < 13:
                print("Your birthday month must consist of 1-12 only")
                continue
            else:
                break
        except:
            print("Your birthday month must consist of numbers only")
            continue

    while (True):
        try:
            birthday_day = int(input("Enter birthday day (1-31): "))
            if not birthday_day > 0 and birthday_day <= 31:
                print("Your birthday day must consist of 1-31 only")
                continue
            else:
                break
        except:
            print("Your birthday day must consist of numbers only")
            continue


    sql.execute(f"SELECT username, password, birthday_year, birthday_month, birthday_day FROM users "
                f"WHERE username = '{username}' AND password = '{password}' AND birthday_year = '{birthday_year}' AND birthday_month = '{birthday_month}' AND birthday_day = '{birthday_day}'")

    if sql.fetchone() is None:
        sql.execute(f"INSERT INTO users VALUES (?,?,?,?,?)", (username, password, birthday_year, birthday_month, birthday_day))
        db.commit()
        print('You have registered.')
    else:
        print('Such a user already exist!')
        for i in sql.execute('SELECT * FROM users'):
            print(i)


def login():
    username = input("Username: ")
    password = input("Password: ")
    a = sql.execute(f"SELECT username, password FROM users WHERE username = '{username}' AND password = '{password}'")
    db.commit()
    if not sql.fetchone():
        print("User not exist!")
        for i in sql.execute('SELECT * FROM users'):
            print(i)
        reg()
    else:
        print('Welcome')


def main():
    print(help)
    while (True):
        enter = input("Enter the command: ")
        match enter:
            case 'h':
                print(help)
            case 'n':
                reg()
            case 'l':
                login()
            case 'e':
                break
            case _:
                print("Choose command!")
                print(help)
                continue


main()