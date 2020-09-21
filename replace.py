import sys


class Replace:

    def __init__(self):
        try:
            self.new_string = sys.argv[1]
            self.old_string = sys.argv[2]
            self.file = sys.argv[3]
        except IndexError:
            raise Exception('ERROR: not all arguments passed. Format: python replace.py <new_string> <old_string> '
                            '<path_to_file>')

    def replace(self):
        try:
            with open(self.file, 'r') as read_file:
                file_data = read_file.read()
                file_data = file_data.replace(self.old_string, self.new_string)
                with open(self.file, 'w') as write_file:
                    write_file.write(file_data)
        except FileNotFoundError:
            return 'ERROR: file not found'


if __name__ == '__main__':
    start = Replace()
    start.replace()
