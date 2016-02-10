#!/usr/bin/python3

import sys

FILL_CELL = '#'
EMPTY_CELL = '.'

class Canvas:
    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns
        self.canvas = [[False for column in range(self.columns)] for row in range(self.rows)]

    def fill_cell(self, row, column):
        if (not self.is_valid_row(row)) or (not self.is_valid_column(column)):
            return False
        self.canvas[row][column] = True
        return True

    def is_filled(self, row, column):
        if (not self.is_valid_row(row)) or (not self.is_valid_column(column)):
            return None
        return self.canvas[row][column]

    def is_valid_row(self, row):
        return (row >= 0) and (row < self.rows)

    def is_valid_column(self, column):
        return (column >= 0) and (column < self.columns)

    def __repr__(self):
        return "A {0}X{1} canvas".format(self.rows, self.columns)

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


def load_canvas(path):
    """Load a Canvas from an input file"""
    with open(path, 'r') as input_file:
        # Read header (M N)
        header = input_file.readline()
        rows, columns = [int(num) for num in header.split(' ')]
        # Read the actual painting
        canvas = Canvas(rows, columns)
        for row, line in enumerate(input_file):
            canvas.canvas[row] = list(map(lambda cell: cell == FILL_CELL, line.strip()))
        return canvas

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("usage: {0} <input_file_path>".format(sys.argv[0]))
        exit(1)
    canvas = load_canvas(sys.argv[1].strip())
    print(repr(canvas))
    print(canvas)
