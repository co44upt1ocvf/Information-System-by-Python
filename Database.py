import sqlite3 as sql

class Database:

    def delete(table, value):
        try:
            conn = sql.connect("Production Department.db")
            cursor = conn.cursor()

            delete = f"delete from {table} where id = ?"
            cursor.execute(delete, (value,))

            conn.commit()
            conn.close()
        except sql.Error as error:
            print(f"Error {error}")

    def adding(self, table):
        script = f"insert into {table} {tuple(self.dict.keys())} values {tuple(self.dict.values())}"
        return script

    def update(table, column, value, id):
        update = f"update {table} set {column} = \"{value}\" where id = \"{id}\""
        table.executequery(update)

    def filter(table):
        try:
            conn = sql.connect("Production Department.db")
            cursor = conn.cursor()

            cursor.execute(f"SELECT * FROM {table}")
            all_results = cursor.fetchall()
            print(all_results)

        except sql.Error as error:
            print(f"Error {error}")

    def executequery(query, value = None):
        try:
            with sql.connect("Production Department.db") as conn:
                cursor = conn.cursor()
                if value:
                    cursor.execute(query, value)
                    conn.commit()
                else:
                    cursor.execute(query)
        except sql.Error as error:
            print(f"Error {error}")