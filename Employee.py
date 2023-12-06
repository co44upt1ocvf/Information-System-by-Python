from Databases import Database

class Employee(Database):
    def __init__(self, surname, firstname, birthday):
        self.surname = surname
        self.firstname = firstname
        self.birthday = birthday
        super().adding('Employee')

    def new_table(self):
        table_1 = '''create table if not exists workers(
            id integer primary key,
            surname text not null,
            firstname text not null,
            birthday date not null
        )'''
        Database.executequery(table_1)