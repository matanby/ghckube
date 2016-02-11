class Location(object):
    def __init__(self, row, column):
        self.row = row
        self.column = column


class Order(object):
    def __init__(self, customer_location, products_map):
        self.customer_location = customer_location
        self.products_map = products_map


class Product(object):
    def __init__(self, pid, weight):
        self.pid = pid
        self.weight = weight


class Warehouse(object):
    def __init__(self, wid, products_map, location):
        self.wid = wid
        self.products_map = products_map
        self.location = location

