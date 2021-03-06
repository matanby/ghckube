import math


class Location(object):
    def __init__(self, row, column):
        self.row = row
        self.column = column

    def distance(self, to, from_ = None):
        if from_ is None:
            from_ = self

        return int(math.ceil(math.sqrt(((to.row - from_.row) ** 2) + ((to.column - from_.column) ** 2))))


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

    def contains_product(self, pid):
        return pid in self.products_map and self.products_map[pid] > 0

