import Package
import HashMap
import Distance
from main import distance_list_dict


class Truck:
    package_list = list
    current_location = str
    total_distance = float

    def __init__(self, package_list, size):

        self.size = size
        self.package_list = [None] * self.size
        self.total_distance = 0.0
        self.current_location = ' 195 W Oakland Ave'

    def deliver_NNA(self):
        index = 0
        closest_address = 0.0

        for package in range(len(self.package_list) -1):
            current_address = distance_list_dict.get_dict_key_str(
                self.current_location, distance_list_dict)
            temp_closest_address = distance_list_dict.find_distance(current_address, self.package_list[index].address,
                                                                    distance_list_dict)
            closest_address = distance_list_dict.find_distance(current_address,
                                                               self.package_list[index + 1].address, distance_list_dict)

            if (temp_closest_address < closest_address):
                closest_address = temp_closest_address
                index += 1

            print(current_address)
