#!/usr/bin/python3

import sys

FILL_CELL = '#'
EMPTY_CELL = '.'

class Canvas:
    def __init__(self, input_file_path):
        self.input_file_path = input_file_path
        with open(input_file_path, 'r') as input_file:
            self.__read_header(input_file)
            self.__read_canvas(input_file)

    def __read_header(self, input_file):
        header = input_file.readline()
        self.rows, self.columns = [int(num) for num in header.split(' ')]

    def __read_canvas(self, input_file):
        self.canvas = [None for row in range(self.rows)]
        for row, line in enumerate(input_file):
            self.canvas[row] = list(map(lambda cell: cell == FILL_CELL, line.strip()))

    def is_filled(self, row, column):
        if (row < 0) or (row >= self.rows) or (column < 0) or (column >= self.columns):
            return None
        return self.canvas[row][column]

    def __repr__(self):
        return "A {0}X{1} canvas. Loaded from {2}".format(self.rows, self.columns, self.input_file_path)

    def __str__(self):
        output = ''
        for row in range(self.rows):
            for column in range(self.columns):
               if self.canvas[row][column]:
                   output += FILL_CELL
               else:
                   output += EMPTY_CELL
            output += '\n'
        return output

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("usage: {0} <input_file_path>".format(sys.argv[0]))
        exit(1)
    canvas = Canvas(sys.argv[1].strip())
    print(repr(canvas))
    print(canvas)
