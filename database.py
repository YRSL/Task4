import MySQLdb


class DatabaseConnection:
    def __init__(self, database_settings):
        self.database = self.database_connect(database_settings)
        self.cursor = self.database.cursor()

    @staticmethod
    def database_connect(database_settings):
        database_config = MySQLdb.connect(
            database_settings["host"],
            database_settings["user"],
            database_settings["password"])
        return database_config

    def disconnect(self):
        self.cursor.close()
        self.database.close()


class DatabaseCreate(DatabaseConnection):

    def create_databases(self):
        for sql_query in sql_create_databases:
            self.cursor.execute(sql_query)

    def create_tables(self):
        self.cursor.execute("USE task4_new_db")
        for sql_query in sql_create_tables:
            self.cursor.execute(sql_query)

    def create_index(self, index_name, table_name, column_name):
        self.cursor.execute("USE task4_new_db")
        self.cursor.execute("CREATE INDEX {} ON {} ({})".format(index_name, table_name, column_name))
        self.database.commit()


class DatabaseEdit(DatabaseConnection):

    def insert_rooms(self, rooms):
        self.cursor.execute("USE task4_new_db")
        sql = "INSERT INTO rooms (id, name) VALUES (%s, %s)"
        for room in rooms:
            self.cursor.execute(sql, (room['id'], room['name']))
        self.database.commit()

    def insert_students(self, students):
        self.cursor.execute("USE task4_new_db")
        sql = "INSERT INTO students (id ,birthday, name, room_id, sex) VALUES (%s, %s, %s, %s, %s)"
        for student in students:
            self.cursor.execute(sql, (
                    student['id'],
                    student['birthday'],
                    student['name'],
                    student['room'],
                    student['sex']))
        self.database.commit()


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


class DatabaseOperations(DatabaseConnection):

    def rooms_list_and_count_students_inside(self):
        self.cursor.execute("USE task4_new_db")
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
        self.cursor.execute("USE task4_new_db")
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
        self.cursor.execute("USE task4_new_db")
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
        self.cursor.execute("USE task4_new_db")
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
