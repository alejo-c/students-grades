import sqlite3

from menu import main_menu
from database_operations import Database


def create_tables():
    db = Database('studentsgrades.db')
    ## Subject table
    db.execute(
        '''CREATE TABLE subjects (
			id INTEGER PRIMARY KEY AUTOINCREMENT,
			name VARCHAR(30) NOT NULL
		)'''
    )
    ## Students table
    db.execute(
        '''CREATE TABLE students (
			id INTEGER PRIMARY KEY AUTOINCREMENT,
			name varchar(20) NOT NULL,
			lastname varchar(20) NOT NULL
		)'''
    )
    ## Grades table
    db.execute(
        '''CREATE TABLE grades (
			id INTEGER PRIMARY KEY AUTOINCREMENT,
			student CHAR(3) NOT NULL,
			subject CHAR(2) NOT NULL, 
			value FLOAT NOT NULL
		)'''
    )
    db.close()


def main():
    # create_tables()
    main_menu()


if __name__ == '__main__':
    main()
