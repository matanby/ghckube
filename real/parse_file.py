from real.drone import Drone
from real.models import Product, Warehouse, Location, Order
import real.globals


def load_data(path):
    with open(path, 'r') as input_file:
        content = input_file.readlines()
        
        first_row = content[0].split(" ")
        real.globals.map_rows = int(first_row[0])
        real.globals.map_columns = int(first_row[1])
        real.globals.drones_num = int(first_row[2])
        real.globals.turns = int(first_row[3])
        real.globals.payload = int(first_row[4])

        num_of_products = int(content[1])
        products_weights = content[2].split(" ")

        for i in range(num_of_products):
            real.globals.products.append(Product(i, products_weights[i]))

        num_of_warehouses = int(content[3])
        
        idx = 4
        
        for i in range(num_of_warehouses):
            location = content[idx].split(" ")
            products = content[idx + 1].split(" ")
            products_map = {}

            for j in range(len(products)):
                products_map[j] = int(products[j])

            real.globals.warehouses.append(Warehouse(i, products_map, Location(int(location[0]), int(location[1]))))

            idx += 2

        num_of_orders = int(content[idx])
        idx += 1

        for i in range(num_of_orders):
            location = content[idx].split(" ")
            # products_num = int(content[idx + 1])
            products = content[idx + 2].split(" ")
            products_map = {}

            # init map
            # for j in range(num_of_products):
            #     products_map[j] = 0

            for k in range(len(products)):
                products_map.setdefault(int(products[k]), 0)
                products_map[int(products[k])] += 1

            real.globals.orders.append(Order(Location(int(location[0]), int(location[1])), products_map))

            idx += 3


def init_drones():
    start_location = real.globals.warehouses[0].location
    payload = real.globals.payload

    for i in range(real.globals.drones_num):
        real.globals.drones.append(Drone(i, start_location, payload))

