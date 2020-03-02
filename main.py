from argparse import ArgumentParser
from reader import JsonReader
from database import DatabaseCreate, DatabaseEdit, DatabaseOperations
from file_creator import FileCreator
import json


def argument_parse():
    parser = ArgumentParser()
    parser.add_argument('students_file', type=str, help='Path to file "students.json"')
    parser.add_argument('rooms_file', type=str, help='Path to file "rooms.json"')
    parser.add_argument('format_file', type=str, choices=['json', 'xml'], help='Format JSON or XML')
    parser.add_argument('db_settings', type=str, help='Database settings')
    p = parser.parse_args()
    return p


def read_db_settings(db_settings):
    with open(db_settings, encoding='UTF-8') as file:
        data = json.load(file)
    return data


def main():

    print("Hello")

    data_from_rooms_file = JsonReader().read(argument_parse().rooms_file)

    data_from_students_file = JsonReader().read(argument_parse().students_file)

    db_settings = read_db_settings(argument_parse().db_settings)

    db_create = DatabaseCreate(db_settings)

    db_create.create_databases()
    db_create.create_tables()

    db_create.create_index('index_room_id', 'rooms', 'id')
    db_create.create_index('index_students_room', 'students', 'room_id')

    db_edit = DatabaseEdit(db_settings)

    db_edit.insert_rooms(data_from_rooms_file)
    db_edit.insert_students(data_from_students_file)

    db_operations = DatabaseOperations(db_settings)

    rooms_list_and_count_students_inside = db_operations.rooms_list_and_count_students_inside()
    top_5_rooms_with_smallest_average_age = db_operations.top_5_rooms_with_smallest_average_age()
    top5_rooms_with_biggest_age_difference = db_operations.top5_rooms_with_biggest_age_difference()
    rooms_list_with_different_sex = db_operations.rooms_list_with_different_sex()

    file_creator = FileCreator(argument_parse().format_file)
    file_creator.create_file("rooms_list_and_count_students_inside", rooms_list_and_count_students_inside)
    file_creator.create_file("top_5_rooms_with_smallest_average_age", top_5_rooms_with_smallest_average_age)
    file_creator.create_file("top5_rooms_with_biggest_age_difference", top5_rooms_with_biggest_age_difference)
    file_creator.create_file("rooms_list_with_different_sex", rooms_list_with_different_sex)

    print("Please check result files")


if __name__ == '__main__':
    main()
