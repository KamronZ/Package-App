import Distance
import datetime

import Time

from Package import Package
from HashMap import PackageHashTable

distance_list_dict = Distance.populate_distance_table()
list_of_all_packages_after_delivery = []
today = today = datetime.datetime.today()
class Truck:

    distance_list_dict = Distance.populate_distance_table()

    package_list = list
    current_location = str
    total_distance = float

    def __init__(self, package_list, size, name):



        self.current_time = datetime.datetime(today.year, today.month, today.day, 8, 00, 0, 0)
        # self.hub_leave_time = datetime.datetime(today.year,today.month,today.day,0,00,0,0)

        self.name = name
        self.size = size
        self.package_list = package_list
        self.total_distance = 0.0
        self.current_location = ' HUB'  # space is added for data normalization. All entries also have this space.

    def deliver_NNA(self):
        print("STARTING DELIVERY, current time is:  ", self.current_time)

        out_index = 0  # outer loop
        index = 0  # for inner loop
        package_index = 0
        new_package = self.package_list[0]

        closest_address = Distance.find_distance(self.current_location,  # first distance from starting point
                                                 # to first package's address from list
                                                 self.package_list[0].address, distance_list_dict)

        while 0 < len(
                self.package_list):  # Do inner loop for every package object current still in the list of packages
            index = 0  # for inner loop
            package_index = 0
            new_package = self.package_list[0]

            closest_address = Distance.find_distance(self.current_location,  # first distance from starting point
                                                     # to first package's address from list
                                                     self.package_list[0].address, distance_list_dict)

            for package in self.package_list:  # for every package in the list
                # distance value acquired from incremented index

                temp_address_distance = Distance.find_distance(self.current_location,
                                                               self.package_list[index].address,
                                                               distance_list_dict)
                if temp_address_distance < closest_address:  # checks for smaller value
                    closest_address = temp_address_distance  # swaps value
                    new_package = self.package_list[index]

                    package_index = index
                    index += 1  # temp_address_distance moves to next entry in package_list

                else:  # distance was not less
                    index += 1  # go to next entry

            print(self.name, "'s current location: ", self.current_location)
            print(self.name, "'s is headed to: ", new_package.address)
            self.current_location = new_package.address
            # print("Current address is: ", self.current_location)

            print("Package ID being delivered is: ", self.package_list[package_index].package_ID)

            self.current_time = Time.convert_distance_to_time(self.current_time, closest_address)
            print("Delivery time is: ", self.current_time, "\nPromised delivery time was: ",
                  self.package_list[package_index].deadline)

            new_package.update_package_delivery_time(self.current_time)
            list_of_all_packages_after_delivery.append(new_package)

            if self.package_list[package_index].special != "":
                print("Packing being removed special notes: ", self.package_list[package_index].special)
            else:
                print("Packing being removed special notes: NONE")

            self.package_list.pop(package_index)

            self.total_distance += closest_address

            print("Total distance traveled by", self.name, 'is: ', self.total_distance)
            print()
            print(self.name, " now contains the following packages:  ")

            for i in self.package_list:
                i.print()

    def hub_return(self):
        self.total_distance += Distance.find_distance(self.current_location,
                                                      ' HUB', distance_list_dict)
        self.current_location = ' HUB'
        print(self.name, "has returned to hub...")
        print("Total distance traveled to deliver load and return to HUB: ", self.total_distance, end='\n')






