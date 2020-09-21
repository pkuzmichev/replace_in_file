import unittest
import os
from unittest.mock import patch
from parameterized import parameterized
from replace import Replace


class ReplaceTest(unittest.TestCase):

    def setUp(self):
        file = 'test_file.txt'
        with open(file, 'a') as f:
            f.write('test data')

        self.args = ['sys', 'new_string', 'test', file]

    def test_replace_with_path_to_file(self):
        self.path_to_file = '../test_file_path.txt'
        with open(self.path_to_file, 'w') as f:
            f.write('test data')

        self.test_args = ['sys', 'new_string', 'test', self.path_to_file]

        with patch('sys.argv', self.test_args):
            self.r = Replace()
            self.r.replace()

        with open(self.path_to_file, 'r') as f:
            self.text_from_file = f.read()
            self.assertTrue('new_string' in self.text_from_file)

        os.remove(self.path_to_file)

    def test_replace_in_file(self):
        with patch('sys.argv', self.args):
            self.r = Replace()
            self.r.replace()

        with open('test_file.txt', 'r') as f:
            self.text_from_file = f.read()
            self.assertTrue('new_string' in self.text_from_file)
            self.assertTrue('test' not in self.text_from_file)

    def test_file_not_found(self):
        self.path_to_file = 'file_not_exist.txt'
        self.test_args = ['sys', 'new_string', 'test', self.path_to_file]

        with patch('sys.argv', self.test_args):
            self.r = Replace()
            self.assertEqual(self.r.replace(), 'ERROR: file not found')

    @parameterized.expand([
        'not_test',
        'TEST'
    ])
    def test_old_string_not_in_file(self, test_value):
        self.test_args = ['sys', 'new_string', test_value, 'test_file.txt']

        with patch('sys.argv', self.test_args):
            self.r = Replace()
            self.r.replace()
            with open(self.test_args[3], 'r') as f:
                self.text_from_file = f.read()
                self.assertFalse(self.test_args[2] in self.text_from_file)

    def test_for_not_all_arguments(self):
        self.test_args = ['sys', 'new_string', 'test_file.txt']

        with patch('sys.argv', self.test_args):
            self.assertRaises(Exception, Replace)

    def tearDown(self):
        os.remove('test_file.txt')


if __name__ == '__main__':
    unittest.main()
