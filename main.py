import Distance
from HashMap import PackageHashTable
from Truck import Truck,list_of_all_packages_after_delivery,today

package_list_dict = PackageHashTable()



def id_to_package(id_list):
    list_of_packages = []

    for i in range(len(id_list)):
        key = id_list[i]

        if package_list_dict.hash_table.look_up(key) is not None:
            package = package_list_dict.hash_table.look_up(key)

            package.print()
            list_of_packages.append(package_list_dict.hash_table.look_up(key))
    print()

    return list_of_packages


def main():

    distance_list_dict = Distance.populate_distance_table()

    total_miles_traveled = 0.0 # tracks total miles for both trucks
    truck_one_prio_package_list_ID = [1,13, 14, 15, 16, 19, 20,22,23,34,35, 37,39, 40]  # 15 needs to reach destination by 9am,
    # everything else by 10:30
    truck_one_package_list_ID = [2, 4, 5, 8,9, 10, 11, 12] # all of these are end of the day
    truck_two_prio_package_list_ID = [3,17,18,19,21,24,27, 29,30,31,33]
    truck_two_package_list_ID = [6,25,26,28,32,36,38] # all of these are end of day

#      TRUCK 1 LOADING AND DELIVERY         #
    truck1 = Truck([], 16, "Truck1")
    print("***** LOADING PACKAGES ONTO", truck1.name, "*****")
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


    # package_list.hash_table.print_hash()

    # print("Make a selection:\n"
    #       "1: See all packages delivered for specific time range\n"
    #       "2: See total distance traveled by all trucks\n"
    #       "3: Exit"
    #       )
    #
    # choice = int(input("Make your selection: "))
    # while(choice != 3):
    #     if choice == 1:
    #
    #         start_hour = int(input("Enter hour you wish to set range to: "))
    #         start_minute = int(input("Enter minute you was to set start range to: "))
    #
    #         end_hour = int(input("Enter hour you wish to end range at: "))
    #         end_minute = int(input("Enter minute you was to end range at: "))
    #
    #
    #         start_range = datetime.datetime(today.year, today.month, today.day, start_hour, start_minute, 00)
    #         end_range = datetime.datetime(today.year, today.month, today.day, end_hour, end_minute, 00)
    #
    #         for package in list_of_all_packages_after_delivery:
    #             package.get_package_status(start_range, end_range)
    #
    #     print("Make a selection:\n"
    #           "1: See all packages delivered for specific time range\n"
    #           "2: See total distance traveled by all trucks\n"
    #           "3: Exit"
    #           )
    #     choice = int(input("Make your selection: "))
    #     if choice == 2:
    #         print("Total distance traveled is: ", total_miles_traveled)
    #         print("Make a selection:\n"
    #               "1: See all packages delivered for specific time range\n"
    #               "2: See total distance traveled by all trucks\n"
    #               "3: Exit"
    #               )
    #
    #         choice = int(input())
    #     if choice == 3:
    #         print("Done")
    #     else:
    #         print("Please make a valid selection")
    #         print("Make a selection:\n"
    #               "1: See all packages delivered for specific time range\n"
    #               "2: See total distance traveled by all trucks\n"
    #               "3: Exit"
    #               )





















if __name__ == "__main__":
    main()
