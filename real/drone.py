from real import globals

FAILURE = -1


class Drone:
    def __init__(self, did, starting_pos, max_load):
        self.did = did
        self.location = starting_pos
        self.max_load = max_load
        self.products = {}
        self.customer_id = None
        self.customer_location = None
        self.turns_left = globals.turns

    def distance_to(self, destination):
        return self.location.distance(destination)

    def current_load(self):
        return sum((globals.products[product].weight * self.products[product] \
                for product in self.products))

    def set_customer(self, customer_location, customer_id):
        self.customer_location = customer_location
        self.customer_id = customer_id

    def try_load(self, warehouse_id, product_id, amount):
        """Returns FAILURE (-1) if there's any problem (including final delivery)
        or the total time until delivery"""

        # Is product in the given warehouse?
        warehouse = globals.warehouses[warehouse_id]
        if product_id not in warehouse.products_map:
            return FAILURE
        # Do we have enough of this product?
        product_left = warehouse.products_map[product_id]
        if product_left < amount:
            return FAILURE
        # Can we lift this product (x amount)?
        product_weight = globals.products[product_id].weight
        if self.current_load() + product_weight > self.max_load:
            return FAILURE
        # Do we have enough time to load and deliver everything?
        original_location = self.location
        distance = self.distance_to(warehouse.location)
        self.location = warehouse.location
        total_delivery_time = self.try_deliver_all()
        if self.turns_left < distance + total_delivery_time:
            self.location = original_location
            return FAILURE
        self.location = original_location
        return self.try_deliver_all()

    def load(self, warehouse_id, product_id, amount):
        warehouse = globals.warehouses[warehouse_id]
        # Update warehouse
        warehouse.products_map[product_id] -= amount
        # Update drone load
        if product_id not in self.products:
            self.products[product_id] = 0
        self.products[product_id] += amount
        # Update location
        distance = self.distance_to(warehouse.location)
        self.location = warehouse.location
        if product_id in self.products:
            self.products[product_id] += amount
        # Update time
        self.turns_left -= (distance + 1)
        # Print command
        cmd = "{0} L {1} {2} {3}".format(self.did, warehouse_id, product_id, amount)
        print cmd
        return cmd

    def try_deliver(self, customer_location, product_id, amount = None):
        # Do we have this product?
        if product_id not in self.products:
            return FAILURE
        product_left = self.products[product_id]
        if amount is None:
            amount = product_left
        # Do we have enough of this product?
        if amount <= 0 or amount > product_left:
            return FAILURE
        # Do we have enough time to deliver?
        distance = self.distance_to(self.customer_location)
        if self.turns_left < distance + 1:
            return FAILURE
        return distance + 1

    def deliver(self, customer_location, product_id, amount = None):
        # Update inventory
        if amount is None:
            amount = self.products[product_id]
        self.products[product_id] -= amount
        # Update time
        distance = self.distance_to(customer_location)
        self.turns_left -= (distance + 1)
        # Update location
        self.location = customer_location
        # Print command
        cmd = "{0} D {1} {2} {3}".format(self.did, self.customer_id, product_id, amount)
        print(cmd)
        return cmd

    def try_deliver_all(self):
        original_location = self.location
        total_time = 0
        for product_id in self.products:
            product_amount = self.products[product_id]
            deliver_time = self.try_deliver(self.customer_location, product_id, product_amount)
            if deliver_time < 0:
                self.location = original_location
                return FAILURE
            self.location = self.customer_location
            total_time += deliver_time
        self.location = original_location
        return total_time

    def deliver_all(self):
        for product_id in self.products:
            product_amount = self.products[product_id]
            self.deliver(self.customer_location, product_id, product_amount)
