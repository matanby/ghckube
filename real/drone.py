from location import Location

class Drone:
    def __init__(self, id, starting_pos, max_load):
        self.id = id
        self.position = starting_pos
        self.max_load = max_load
        self.products = ProductMap()
        self.commands = []  # (Command Letter, Time, )

    def distance_to(destination):
        return self.position.distance(destination)

    def available_in():
        pass

    def load(warehouse, product_type, amount):
       pass
