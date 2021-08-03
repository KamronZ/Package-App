"""HashMap is 0(1), key functions are:
- An Array: to store data
- Hash function: function to convert key into an array index(not needed here)
- Collision handling"""

import csv
from Package import Package


class HashMap:
    def __init__(self):
        self.size = 40
        self.map = [None] * self.size

    def _get_hash(self, key):
        #print("Key is: " + str(key))
        # hash = ord(key) % 41  # not needed
        hash = int(key)
        #print("Hash key is: " + str(hash))
        return hash

    def insert(self, key, value: Package):
        key_hash = self._get_hash(key) - 1 # index value
        key_value = [key, value]  # what to insert into that index.  in this case a list  with [key,value]

        if self.map[key_hash] is None:  # check if that index is empty
            self.map[key_hash] = list([key_value])  # add at that index, a new list having the key_value pair
            return True
        else:
            for pair in self.map[key_hash]:  # for [key,value] pair at the index
                if pair[0] == key:  # if the key already exist
                    pair[1] = value  # replace the value with new value
                    return True
                self.map[key_hash].append(key_value)  # otherwise add key_value at that index
                return True

    def look_up(self, key):
        key_hash = self._get_hash(key)  # takes key and gets the index
        if self.map[key_hash] is not None:  # if there is something at that index
            for pair in self.map[key_hash]:
                if pair[0] == key:  # if the key matches
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

                    # package_obj = Package(item[0][1].package_ID,item[0][1].address,item[0][1].city,
                    #                   item[0][1].state,item[0][1].zip,item[0][1].deadline,
                    #                   item[0][1].weight,item[0][1].status)
                    #
                    # print(package_obj.print())
                index += 1
    print('Done')


class PackageHashTable(HashMap):
    def __init__(self):
        super().__init__()
        # this table uses my HashMap class and will hold the Package objects

        self.package_hash_table = HashMap()
        # read cvs file and use these values to populate our table of Packages
        with open('Package File.csv', mode='r', encoding='utf-8-sig') as infile:
            reader = csv.reader(infile)
            for rows in reader:
                #rows[0] = int(rows[0]) should no longer be an issue after previous typecasting to int
                new_package_obj = Package(rows[0], rows[1], rows[2], rows[3], rows[4], rows[5], rows[6], rows[7])
                self.package_hash_table.insert(rows[0], new_package_obj)

        self.package_hash_table.print_hash()











