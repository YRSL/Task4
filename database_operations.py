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


    #____________________________________________________________________________________--

    def rooms_list_and_count_students_inside(self):
        self.cursor.execute(
            """
            SELECT  rooms.id , rooms.name , COUNT(students.id) as students
            FROM rooms
            JOIN students ON rooms.id = students.room_id
            GROUP BY rooms.id
            """
        )
        result = self.cursor.fetchall()
        return result

    def top_5_rooms_with_smallest_average_age(self):
        self.cursor.execute(
            """
            SELECT rooms.id , rooms.name , AVG(TIMESTAMPDIFF(YEAR, students.birthday,NOW())) as average_age
            FROM rooms
            JOIN students ON rooms.id = students.room_id
            GROUP BY rooms.id 
            ORDER BY average_age
            LIMIT 5
            """
        )
        result = self.cursor.fetchall()
        return result

    def top5_rooms_with_biggest_age_difference(self):
        self.cursor.execute(
            """
            SELECT rooms.id , rooms.name , TIMESTAMPDIFF(YEAR , MAX(students.birthday) , MIN(students.birthday)) as max_diff
            FROM rooms
            JOIN students ON rooms.id = students.room_id
            GROUP BY rooms.id
            ORDER BY max_diff DESC
            LIMIT 5
            """
        )
        result = self.cursor.fetchall()
        return result

    def rooms_list_with_different_sex(self):
        self.cursor.execute(
            """
            SELECT DISTINCT rooms.id , rooms.name , COUNT(DISTINCT students.sex) as sex
            FROM rooms
            JOIN students ON rooms.id = students.room_id
            GROUP BY rooms.id 
            HAVING sex = 2
            """
        )
        result = self.cursor.fetchall()
        return result
    #____________________________________________________________________________________++


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
