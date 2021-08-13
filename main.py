# KAMRON ZELL
#Student ID: 001355235

# import Distance  # O(N)
from HashMap import PackageHashTable  # O(1)
from Truck import Truck, list_of_all_packages_after_delivery, today
import datetime

package_list_dict = PackageHashTable()


def id_to_package(id_list):  # O(N) Loads packages to truck
    list_of_packages = []

    for i in range(len(id_list)):
        key = id_list[i]

        if package_list_dict.hash_table.look_up(key) is not None:  # 0(1)
            package = package_list_dict.hash_table.look_up(key)

            package.print()
            list_of_packages.append(package_list_dict.hash_table.look_up(key))  # O(1)
    print()

    return list_of_packages


def main():
    # distance_list_dict = Distance.populate_distance_table()  # O(N)
    # total_miles_traveled = 0.0  # tracks total miles for both trucks

    truck_one_prio_package_list_ID = [1, 7, 13, 14, 15, 16, 20, 22, 23, 34, 35, 37, 39,
                                      40]  # 15 needs to reach destination by 9am,
    # everything else by 10:30
    truck_one_package_list_ID = [2, 4, 5, 8, 9, 10, 11, 12]  # all of these are end of the day
    truck_two_prio_package_list_ID = [3, 17, 18, 19, 21, 24, 27, 29, 30, 31, 33]
    truck_two_package_list_ID = [6, 25, 26, 28, 32, 36, 38]  # all of these are end of day

    #      TRUCK 1 LOADING AND DELIVERY         #
    truck1 = Truck([], 16, "Truck1")
    print("***** LOADING PACKAGES ONTO", truck1.name, "*****")
    truck1 = Truck(id_to_package(truck_one_prio_package_list_ID), 16, "Truck1")  # O(N)

    truck1.deliver_NNA()  # O(N^2)

    truck1.hub_return()  # O(1)

    truck1.package_list = id_to_package(truck_one_package_list_ID)  # O(N)
    truck1.deliver_NNA()  # O(N^2)

    truck1.hub_return()  # O(1)

    print("Truck1 completed all of its deliveries at: ", truck1.current_time, "in a total distance of: ",
          truck1.total_distance)
    #       TRUCK 2 LOADING AND DELIVERY         #
    truck2 = Truck(id_to_package(truck_two_prio_package_list_ID), 16, "Truck2")  # O(N)
    truck2.deliver_NNA()  # O(N^2)

    truck2.hub_return()  # N(1)

    truck2.package_list = id_to_package(truck_two_package_list_ID)  # O(N)
    truck2.deliver_NNA()  # O(N^2)

    truck2.hub_return()  # O(1)

    total_miles_traveled = truck1.total_distance + truck2.total_distance
    package_list_dict.hash_table.print_hash()  # O(N)

    print("Make a selection:\n"
          "1: See all packages delivered for specific time range\n"
          "2: See total distance traveled by all trucks\n"
          "3: See package status at a specific time\n"
          "4: Run the entire simulation and give all packages sorted by delivered time (earliest to latest)\n"
          "5: Exit"
          )

    choice = int(input("Make your selection: "))
    while choice != 5:  # O(1)

        if choice == 1:
            start_hour = (int(input("Enter hour you wish to get packages status:")))
            start_minute = (int(input("Enter minute you wish to get packages status:")))

            # start_hour = int(input("Enter hour you wish to set range to: "))
            # start_minute = int(input("Enter minute you was to set start range to: "))

            # end_hour = int(input("Enter hour you wish to end range at: "))
            # end_minute = int(input("Enter minute you was to end range at: "))

            start_range = datetime.datetime(today.year, today.month, today.day, start_hour, start_minute, 00)
            # end_range = datetime.datetime(today.year, today.month, today.day, end_hour, end_minute, 00)

            for package in sorted(list_of_all_packages_after_delivery, key=lambda x: x.delivery_timestamp):  # O(N)
                package.package_status(start_range)

            print("Make a selection:\n"
                  "1: See status of all packages at a specific time(sorted by earliest delivered time)\n"
                  "2: See total distance traveled by all trucks\n"
                  "3: See package status at a specific time\n"
                  "4: Run the entire simulation and give all packages sorted by delivered time (earliest to latest)\n"
                  "5: Exit"
                  )
            choice = int(input("Make your selection: "))

        if choice == 2:
            print("Total distance traveled is: ", round(total_miles_traveled, 2), " miles")
            print("Make a selection:\n"
                  "1: See all packages delivered for specific time range\n"
                  "2: See total distance traveled by all trucks\n"
                  "3: See package status at a specific time\n"
                  "4: Run the entire simulation and give all packages sorted by delivered time (earliest to latest)\n"
                  "5: Exit"
                  )

            choice = int(input("Make your selection: "))
        if choice == 3:
            package_id = int(input("Enter package ID to check: "))
            start_hour = int(input("Enter hour for time you would like to check: "))
            start_minute = int(input("Enter minute for time you like to check "))
            time_to_check = datetime.datetime(today.year, today.month, today.day, start_hour, start_minute, 00)
            for package in list_of_all_packages_after_delivery:  # O(N)
                if int(package.package_ID) == package_id:
                    package.package_status(time_to_check)

            print("Make a selection:\n"
                  "1: See all packages delivered for specific time range\n"
                  "2: See total distance traveled by all trucks\n"
                  "3: See package status at a specific time\n"
                  "4: Run the entire simulation and give all packages sorted by delivered time (earliest to latest)\n"
                  "5: Exit"
                  )
            choice = int(input("Make your selection: "))

        if choice == 4:
            for package in sorted(list_of_all_packages_after_delivery, key=lambda x: x.delivery_timestamp):  # O(N)
                package.print()
            print("Make a selection:\n"
                  "1: See all packages delivered for specific time range\n"
                  "2: See total distance traveled by all trucks\n"
                  "3: See package status at a specific time\n"
                  "4: Run the entire simulation and give all packages sorted by delivered time (earliest to latest)\n"
                  "5: Exit"
                  )
            choice = int(input("Make your selection: "))

        if choice == 5:
            print("DONE")

        # else:
        #     print("Please make a valid selection")
        #     print("Make a selection:\n"
        #           "1: See all packages delivered for specific time range\n"
        #           "2: See total distance traveled by all trucks\n"
        #           "3: See package status at a specific time\n"
        #           "4: Exit"
        #           )
        #     choice = int(input("Make your selection: "))


if __name__ == "__main__":
    main()
