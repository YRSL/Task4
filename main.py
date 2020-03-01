from argparse import ArgumentParser
from writer import JsonWriter, XmlWriter
from reader import JsonReader
from database_operations import DataBase


def argument_parse():
    parser = ArgumentParser()
    parser.add_argument('students_file', type=str, help='Path to file "students.json"')
    parser.add_argument('rooms_file', type=str, help='Path to file "rooms.json"')
    parser.add_argument('format_file', type=str, choices=['json', 'xml'], help='Format JSON or XML')
    p = parser.parse_args()
    return p


def main():

    print("Hello")

    data_from_rooms_file = JsonReader().read(argument_parse().rooms_file)

    data_from_students_file = JsonReader().read(argument_parse().students_file)

    DataBase.create_databases()
    DataBase.create_tables()

    DataBase.create_index('index_room_id', 'rooms', 'id')
    DataBase.create_index('index_students_room', 'students', 'room_id')

    DataBase.insert_rooms(data_from_rooms_file)
    DataBase.insert_students(data_from_students_file)

    DataBase.save_changes()





if __name__ == '__main__':
    main()
