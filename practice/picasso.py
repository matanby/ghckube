#!/usr/bin/python3

PAINT_LINE = 'PAINT_LINE {0} {1} {2} {3}'   # row1, column1, row2, column2
PAINT_SQUARE = 'PAINT_SQUARE {0} {1} {2}'   # center_row, center_column, radius
ERASE_CELL = 'ERASE_CELL {0} {1}'           # row, column

class Picasso:
    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns
        self.commands = []

    def paint_hline(self, row, column_start, column_end):
        if (not self.__is_valid_row(row)) \
                or (not self.__is_valid_column(column_start)) \
                or (not self.__is_valid_column(column_end)):
            return False

        if column_start > column_end:
            column_start, column_end = column_end, column_start     # swap

        self.commands.append(PAINT_LINE.format(row, column_start, row, column_end))
        return True

    def paint_vline(self, column, row_start, row_end):
        if (not self.__is_valid_column(column)) \
                or (not self.__is_valid_row(row_start)) \
                or (not self.__is_valid_row(row_end)):
            return False

        if row_start > row_end:
            row_start, row_end = row_end, row_start     # swap

        self.commands.append(PAINT_LINE.format(row_start, column, row_end, column))
        return True

    def paint_square(self, center_row, center_column, radius):
        if (not self.__is_valid_row(center_row - radius)) \
                or (not self.__is_valid_row(center_row + radius)) \
                or (not self.__is_valid_column(center_column - radius)) \
                or (not self.__is_valid_column(center_column + radius)):
            return False

        self.commands.append(PAINT_SQUARE.format(center_row, center_column, radius))
        return True

    def erase_cell(self, row, column):
        if (not self.__is_valid_row(row)) or (not self.__is_valid_column(column)):
            return False

        self.commands.append(ERASE_CELL.format(row, column))
        return True

    def save(self, path):
        with open(path, 'r') as output_file:
            output_file.write(repr(self))

    def __repr__(self):
        output = '{0}\n'.format(len(self.commands))
        output += '\n'.join(self.commands)
        output += '\n'
        return output

    def __str__(self):
        # TODO: paint commands on a canvas
        return repr(self)

    def __is_valid_row(self, row):
        return (row >= 0) and (row < self.rows)

    def __is_valid_column(self, column):
        return (column >= 0) and (column < self.columns)


if __name__ == '__main__':
    picasso = Picasso(10, 5)

    picasso.paint_hline(9, 0, 4)    # ok
    picasso.paint_hline(10, 0, 4)   # illegal row
    picasso.paint_hline(9, 0, 5)    # illegal end column

    picasso.paint_vline(4, 0, 9)    # ok
    picasso.paint_vline(5, 0, 4)    # illegal column
    picasso.paint_vline(5, -1, 5)   # illegal everything

    picasso.paint_square(2, 2, 2)   # ok
    picasso.paint_square(0, 0, 2)   # illegal bounds
    picasso.paint_square(9, 4, 1)   # illegal bounds

    picasso.erase_cell(0, 0)        # ok
    picasso.erase_cell(-1, 0)       # illegal row
    picasso.erase_cell(0, -1)       # illegal column
    picasso.erase_cell(10, 0)       # illegal row
    picasso.erase_cell(0, 5)        # illegal column

    print(picasso)  # should contain 4 commands only
