from Truck import Truck
import HashMap
import Distance
from HashMap import package_list


def main():
    def id_to_package(id_list):
        package_list_dict = HashMap.PackageHashTable()
        package_list_dict.print_hash()

        list_of_packages = []
        for i in range(len(id_list)):
            key = int(i)
            if package_list_dict.look_up(key) is not None:
                package = package_list_dict.look_up(i)
                package.print()
                list_of_packages.append(package_list_dict.look_up(key))

            else:
                print("none")

    distance_list_dict = Distance.populate_distance_table()
    print(distance_list_dict)
    print(Distance.find_distance(' 177 W Price Ave', ' 6351 S 900 E', distance_list_dict))

    truck_one_prio_package_list_ID = [1, 13, 14, 15, 16, 19, 20, 34, 37,
                                      40]  # 15 needs to reach destination by 9am, everything else by 10:30
    truck_one_package_list_ID = [2, 4, 5, 8, 9, 10, 11, 12, 35, 39]

    truck_two_prio_package_list_ID = [3, 6, 18, 29, 30, 31]
    truck_two_package_list_ID = [17, 19, 21, 22, 23, 24, 25, 26, 27, 28, 32, 33, 36, 38]

    id_to_package(truck_one_prio_package_list_ID)


if __name__ == "__main__":
    main()
