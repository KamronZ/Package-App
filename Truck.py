import Distance

distance_list_dict = Distance.populate_distance_table()



class Truck:
    distance_list_dict = Distance.populate_distance_table()
    package_list = list
    current_location = str
    total_distance = float

    def __init__(self, package_list, size):

        self.size = size
        self.package_list = package_list #[None] * self.size
        self.total_distance = 0.0
        self.current_location = ' 4001 South 700 E'

    def deliver_NNA(self):

        index = 0
        '''count will track what index the smallest distance was found at.  count increments ONLY when a swap occurs!
        because of this, count is always checked to see if it equals the index.  When they do not equal that means that:
        a swap did not occur earlier in  the list but a swap does need to occur now.  If a swap never happens, that means
        count will pop the package at the index of count. '''
        count = 0
        closest_address = Distance.find_distance(self.current_location,  # first distance from starting point
                                                 # to first package's address from list
                                                 self.package_list[0].address, distance_list_dict.hash_table)
        i = 0
        while i < len(
                self.package_list):  # Do inner loop for every package object current still in the list of packages
            for package in range(len(self.package_list)):  # for every package in the list
                # distance value acquired from incremented index
                temp_address_distance = distance_list_dict.find_distance(self.current_location,
                                                                         self.package_list[index].address,
                                                                         distance_list_dict.hash_table)

                if count == len(self.package_list):  # if count is at the last index then a swap was made everytime,
                    # or a swap was made on the last index of list

                    self.current_location = self.package_list[
                        index].address  # truck moves to location that is last in list
                    self.package_list.pop(index)  # remove package that is last in list
                    self.total_distance += closest_address  # add the distance traveled to total_distance

                if index == len(self.package_list):  # if index is at last index of list
                    self.current_location = self.package_list[count].address  # truck moves to location where smallest
                    # value was found
                    self.package_list.pop(count)  # remove package from package_list[count]
                    self.total_distance += closest_address  # add the distance traveled to total_distance

                if temp_address_distance < closest_address:  # checks for smaller value
                    closest_address = temp_address_distance  # swaps value
                    index += 1  # temp_address_distance moves to next entry in package_list
                    count += 1  # tracks the current lowest values position in package_list
                    if count != index:
                        count = index
                    # if index > len(self.package_list) - 1:  # checks if our last increment exceeds our list length
                    #     if count != index:
                    #         count = index
                    #         index -= 1
                    #         count -= 1
                else:  # if condition failed, move to next entry
                    index += 1
            i += 1

    def hub_return(self):
        self.total_distance += distance_list_dict.find_distance(self.current_location,
                                                                ' 4001 South 700 E', distance_list_dict)
        self.current_location = '4001 South 700 E'
