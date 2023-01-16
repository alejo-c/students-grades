import sqlite3


class Database:
    def __init__(self, name: str) -> None:
        self.name = name
        self.connection_db, self.cursor = open_database(self.name)

    def execute(self, expression: str):
        self.cursor.execute(expression)
        self.connection_db.commit()

        return self.cursor.fetchall()

    def close(self):
        self.cursor.close()
        self.connection_db.close()


def open_database(database_name: str):
    connection_db = sqlite3.connect(database_name)
    cursor = connection_db.cursor()
    return connection_db, cursor


def execute(database_name: str, expression: str):
    db = Database(database_name)
    output = db.execute(expression)
    db.close()
    return output