from argparse import ArgumentParser


def main():

    print("Hello")

    def arg_parse():
        parser = ArgumentParser()
        parser.add_argument('students_file', type=str, help='Path to file "students.json"')
        parser.add_argument('rooms_file', type=str, help='Path to file "rooms.json"')
        parser.add_argument('format_file', type=str, choices=['json', 'xml'], help='Format JSON or XML')
        p = parser.parse_args()
        return p

    def main():
        pass

if __name__ == '__main__':
    main()