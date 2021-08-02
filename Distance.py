import csv

from collections import OrderedDict


def create_distance_dict():
    with open('Distance Table.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        distance_dict = OrderedDict()

        for line in csv_reader:
            key = line[0].replace("\n", " ")
            distance_dict[key] = line[2:30]

    return distance_dict

'''Dict has a key value for every source destination.  Each value is a list.  Each list containts the distances 
between every point.  This works because csv file is ordered and each source  '''
def find_distance(address_source, address_dest, dict): \
        # dict is in format of <string, List<int> >
    if address_source not in dict.keys():
        print("source address not found")
        return -1
    if address_dest not in dict.keys():
        print("destination address not found.")
        return -1

    index = 0
    for key in dict.keys():
        if key == address_dest:
            break
        else:
            index += 1
    list = dict[address_source]
    return list[index]



print(find_distance('Western Governors University 4001 South 700 East,  Salt Lake City, UT 84107',
                    'Western Governors University 4001 South 700 East,  Salt Lake City, UT 84107', create_distance_dict()))
print(create_distance_dict())
