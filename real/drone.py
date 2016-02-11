from location import Location

class Drone:
    def __init__(self, id, starting_pos, max_load):
        self.id = id
        self.position = starting_pos
        self.max_load = max_load

    def distance_to(row, column):
        return sqrt(((self.position.row - row) ** 2) + ((self.position.column - column) ** 2))
