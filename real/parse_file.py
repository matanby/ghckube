import sys

fname =


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
