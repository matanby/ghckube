import itertools
from numpy import random

from real import globals
from real import parse_file


def run(orders):
    for oid in orders:
        customer_location = globals.orders[oid].customer_location
        used_drones = set()
        for pid, count in globals.orders[oid].products_map.iteritems():
            for i in range(count):
                did, wid = find_best_drone(pid, customer_location, oid)
                if did == -1:
                    # stop everything
                    break

                globals.drones[did].load(wid, pid, 1)
                used_drones.add(did)

        for did in used_drones:
            globals.drones[did].deliver_all()


def find_best_drone(pid, customer_location, oid):
    feasible_warehouse_ids = [w.wid for w in globals.warehouses if w.contains_product(pid)]
    chosen_did, chosen_wid, lowest_cost = -1, -1, -1
    for drone in globals.drones:
        drone.set_customer(customer_location, oid)
        for wid in feasible_warehouse_ids:
            cost = drone.try_load(wid, pid, 1)
            if cost != -1:
                if lowest_cost == -1 or cost < lowest_cost:
                    lowest_cost = cost
                    chosen_wid = wid
                    chosen_did = drone.did

    return chosen_did, chosen_wid


if __name__ == '__main__':
    import sys
    parse_file.load_data(sys.argv[1])
    parse_file.init_drones()

    order_list = list(range(len(globals.orders)))
    random.shuffle(order_list)
    order_permutations = itertools.permutations(range(len(globals.orders)))
    for orders in order_permutations:
        # run(orders)
        run(order_list)
        break
