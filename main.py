from HashMap import PackageHashTable, HashMap
from Truck import Truck



package_list_dict = PackageHashTable()
print(package_list_dict)
package_list_dict.hash_table.print_hash()


def id_to_package(id_list):

    list_of_packages = []
    for i in range(len(id_list)):
        key = id_list[i]
        print(key)
        if package_list_dict.hash_table.look_up(key) is not None:
            package = package_list_dict.hash_table.look_up(key)
            package.print()
            list_of_packages.append(package_list_dict.hash_table.look_up(key))
            print(list_of_packages)
    return list_of_packages


def main():

    # distance_list_dict = Distance.populate_distance_table()
    # print(distance_list_dict)
    # print(Distance.find_distance(' 177 W Price Ave', ' 6351 S 900 E', distance_list_dict))

    truck_one_prio_package_list_ID = [1, 13, 14, 15, 16, 19, 20, 34, 37, 40]  # 15 needs to reach destination by 9am,
    # everything else by 10:30

    truck_one_package_list_ID = [2, 4, 5, 8, 9, 10, 11, 12, 35, 39]

    truck_two_prio_package_list_ID = [3, 6, 18, 29, 30, 31]
    truck_two_package_list_ID = [17, 19, 21, 22, 23, 24, 25, 26, 27, 28, 32, 33, 36, 38]

    truck1 = Truck(id_to_package(truck_one_prio_package_list_ID), 16)

    #truck1.deliver_NNA()


if __name__ == "__main__":
    main()
