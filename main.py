import Distance
from HashMap import PackageHashTable, HashMap
from Truck import Truck

package_list_dict = PackageHashTable()





def id_to_package(id_list):
    list_of_packages = []
    for i in range(len(id_list)):
        key = id_list[i]

        if package_list_dict.hash_table.look_up(key) is not None:
            package = package_list_dict.hash_table.look_up(key)
            package.print()
            list_of_packages.append(package_list_dict.hash_table.look_up(key))

    return list_of_packages


def main():

    distance_list_dict = Distance.populate_distance_table()



    total_miles_traveled = 0.0 # tracks total miles for both trucks
    truck_one_prio_package_list_ID = [1, 13, 14, 15, 16, 19, 20, 34, 37, 40]  # 15 needs to reach destination by 9am,
    # everything else by 10:30
    truck_one_package_list_ID = [2, 4, 5, 8, 9, 10, 11, 12, 35, 39] # all of these are end of the day
    truck_two_prio_package_list_ID = [3, 6, 18, 29, 30, 31]
    truck_two_package_list_ID = [17, 19, 21, 22, 23, 24, 25, 26, 27, 28, 32, 33, 36, 38] # all of these are end of day

#      TRUCK 1 LOADING AND DELIVERY         #
    truck1 = Truck(id_to_package(truck_one_prio_package_list_ID), 16, "Truck1")
    truck1.deliver_NNA()

    truck1.hub_return()


    truck1.package_list = id_to_package(truck_one_package_list_ID)
    truck1.deliver_NNA()

    truck1.hub_return()

    print("Truck1 completed all of its deliveries at: ", truck1.current_time, "in a total distance of: ", truck1.total_distance)
#       TRUCK 2 LOADING AND DELIVERY         #
    truck2 = Truck(id_to_package(truck_two_prio_package_list_ID), 16, "Truck2")
    truck2.deliver_NNA()

    truck2.hub_return()



    truck2.package_list = id_to_package(truck_two_package_list_ID)
    truck2.deliver_NNA()

    truck2.hub_return()

    total_miles_traveled = truck1.total_distance + truck2.total_distance

    print("Total miles traveled to deliver everything is: ", total_miles_traveled)



if __name__ == "__main__":
    main()
