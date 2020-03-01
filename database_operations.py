import mysql.connector


class DataBase:
    def __init__(self):
        self.my_db = mysql.connector.connect(
                      host="localhost",
                      user="root",
                      password="123"
        )
        self.my_cursor = self.connect.cursor()

    def create_databases(self):
        for sql_query in sql_create_databases:
            self.my_cursor.execute(sql_query)

    def create_tables(self):
        for sql_query in sql_create_tables:
            self.my_cursor.execute(sql_query)


sql_create_databases = [
                """CREATE SCHEMA IF NOT EXISTS task4_new_db DEFAULT CHARACTER SET utf8;""",
    ]

sql_create_tables = [
    """CREATE TABLE IF NOT EXISTS task4_new_db.students (
        id INT PRIMARY KEY,
        birthday DATE NOT NULL,
        name VARCHAR(50) NOT NULL,
        room_id INT NOT NULL, 
        sex ENUM("M","F") NOT NULL,
        FOREIGN KEY (room_id) REFERENCES rooms(id) 
            ON DELETE CASCADE
        );"""

    """CREATE TABLE IF NOT EXISTS task4_new_db.rooms(
        id INT PRIMARY KEY,
        name VARCHAR(50) NOT NULL
        );"""
    ]

