"""HashMap is 0(1), key functions are:
- An Array: to store data
- Hash function: function to convert key into an array index(not needed here)
- Collision handling"""

import csv
from Package import Package


class HashMap:
    def __init__(self):
        self.size = 41
        self.map = [None] * self.size

    def _get_hash(self, key):  # this function is only needed if not working with keys having unique immutable IDs
        # print("Key is: " + str(key))
        # hash = ord(key) % size
        hash = int(key)  # key it cast to int
        # print("Hash key is: " + str(hash))
        return hash  # as of right now returns the exact same thing

    def insert(self, key, value: Package):
        key_hash = self._get_hash(key)   # index value. -1 because package ID starts at 1, not 0
        key_value = [int(key), value]  # what to insert into that index.  in this case a list  with [key,value]

        if self.map[key_hash] is None:  # check if that index is empty
            self.map[key_hash] = list([key_value])  # add at that index, a new list having the key_value pair
            return True
        else:
            for pair in self.map[key_hash]:  # for [key,value] pair at the index
                if pair[0] == key:  # if the key already exist(info is being updated)
                    pair[1] = value  # replace the value with new value
                    return True
                self.map[key_hash].append(key_value)  # otherwise add (key_value) at that index
                return True

    def look_up(self, key):
        key_hash = self._get_hash(key)  # takes key and gets the index
       # print("key is: ", key)
        if self.map[key_hash] is not None:  # if there is something at that index
            for pair in self.map[key_hash]:
               # print("pair is: ", pair)
                if pair[0] == key:  # if the key matches
                   # print("value being returned is: ", pair[1])
                    return pair[1]  # return the value
        return None

    def delete(self, key):
        key_hash = self._get_hash(key)
        if self.map[key_hash] is None:
            return False
        for i in range(0, len(self.map[key_hash])):
            if self.map[key_hash][i][0] == key:
                print("deleting: " + key + " " + self.look_up(key))
                self.map[key_hash].pop(i)
                return True

    def print_hash(self):
        index = 0
        for item in self.map:

            if item is not None:
                package = item[0][1]
                package.print()

            index += 1
        print('Done')


class PackageHashTable():

    def __init__(self):
        super().__init__()
        # this table uses my HashMap class and will hold the Package objects
        self.hash_table = HashMap()
        # read cvs file and use these values to populate our table of Packages
        with open('Package File.csv', mode='r', encoding='utf-8-sig') as infile:
            reader = csv.reader(infile)
            for rows in reader:
                rows[1] = rows[1].replace("North", "N")  # used to normalize address data
                rows[1] = rows[1].replace("South", "S")  # used to normalize address data
                rows[1] = rows[1].replace("East", "E")  # used to normalize address data
                rows[1] = rows[1].replace("West", "W")  # used to normalize address data

                new_package_obj = Package(rows[0], rows[1], rows[2], rows[3], rows[4], rows[5], rows[6], rows[7])
                self.hash_table.insert(rows[0], new_package_obj)


