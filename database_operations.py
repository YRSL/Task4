import mysql.connector


class DataBase:
    def __init__(self):
        self.db = mysql.connector.connect(
                      host="localhost",
                      user="root",
                      password="123"
        )
        self.cursor = self.connect.cursor()

    def create_databases(self):
        for sql_query in sql_create_databases:
            self.cursor.execute(sql_query)

    def create_tables(self):
        for sql_query in sql_create_tables:
            self.cursor.execute(sql_query)

    def create_index(self, index_name, table_name, column_name):
        self.cursor.execute("CREATE INDEX {} ON {} ({})".format(index_name, table_name, column_name))

    def insert_rooms(self, rooms):
        for room in rooms:
            self.cursor.execute("INSERT INTO rooms (id, name) VALUES ({},{})".format(room['id'], room['name']))

    def insert_students(self, students):
        for student in students:
            self.cursor.execute("INSERT INTO students (id ,birthday, name, room_id, sex) VALUES ({},{},{},{})".format(
                student['id'],
                student['birthday'],
                student['name'],
                student['room'],
                student['sex']))

    def save_changes(self):
        self.connect.commit()


sql_create_databases = [
    """CREATE SCHEMA IF NOT EXISTS task4_new_db DEFAULT CHARACTER SET utf8;""",
    ]

sql_create_tables = [
    """CREATE TABLE IF NOT EXISTS task4_new_db.rooms(
        id INT PRIMARY KEY,
        name VARCHAR(50) NOT NULL
        );""",

    """CREATE TABLE IF NOT EXISTS task4_new_db.students (
        id INT PRIMARY KEY,
        birthday DATE NOT NULL,
        name VARCHAR(50) NOT NULL,
        room_id INT NOT NULL, 
        sex ENUM("M","F") NOT NULL,
        FOREIGN KEY (room_id) REFERENCES rooms(id) 
            ON DELETE CASCADE
        );"""
    ]
