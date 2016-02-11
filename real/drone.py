from models import Location

FAILURE = -1

class Drone:
    def __init__(self, did, starting_pos, max_load):
        self.did = did
        self.position = starting_pos
        self.max_load = max_load
        self.products = {}
        self.customer_location = None

    def distance_to(self, destination):
        return self.position.distance(destination)

    def total_turns(self):
        pass

    def current_load(self):
        return sum((products[product].weight * self.products[product] \
                for product in self.products))

    def set_customer(customer_location):
        self.customer_location = customer_location

    def try_load(self, warehouse_id, product_id, amount):
        """Returns FAILURE (-1) if there's any problem (including final delivery)
        or the total time until delivery"""

        # Is product in the given warehouse?
        warehouse = warehouses[warehouse_id]
        if product_id not in warehouse.products_map:
            return FAILURE
        # Do we have enough of this product?
        product_left = warehouse.products_map[product_id]
        if product_left < amount:
            return FAILURE
        # Can we lift this product (x amount)?
        product_weight = products[product_id].weight
        if current_load + product_weight > self.max_load:
            return FAILURE
        # Do we have enough time to load and deliver everything?
        original_location = self.location
        distance = self.distance_to(self.warehouse.location)
        self.location = self.warehouse.location
        total_delivery_time = self.try_deliver_all()
        if (turns_left < distance + 1):
            self.location = original_location
            return False
        return self.try_deliver_all()

    def load(self, warehouse, product, amount):
        # Print command
        # Update warehouse
        # Update location
        if product.id in self.products:
            self.products[product.id] += amount
        cmd = "{0} L {1} {2} {3}".format(self.id, warehouse.id, product.id, amount)
        self.commands.append(cmd)
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
        if (turns_left < distance + 1):
            return FAILURE
        return True

    def try_deliver_all(self):
        pass

    def deliver(self):
        pass

    def deliver_all(self):
        pass
