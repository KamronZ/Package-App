import csv

from collections import OrderedDict


def create_distance_dict(): # clean and normalize data
    with open('Distance Table.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        distance_dict = OrderedDict()

        for line in csv_reader:
            key = line[1].replace("\n", " ")
            key = key.replace("North", "N")
            key = key.replace("South", "S")
            key = key.replace("East", "E")
            key = key.replace("West", "W")
            distance_dict[key] = line[2:30]

    return distance_dict


# FIXME this needs more work to match same formatting as original, BUT MIGHT NOT EVEN THIS THIS
def clean_distance_csv(distance_dict: dict):
    # this will now create a new csv with complete data
    with open('cleaned_data.csv', 'w') as outfile:
        csv_writer = csv.writer(outfile)
        for key, value in distance_dict.items():
            csv_writer.writerow([key, value])


def get_dict_key_str(index, dict):
    i = 0
    for key in dict.keys():
        if i != index:
            i += 1
        else:
            return str(key)


'''Dict has a key value for every source destination.  Each value is a list.  Each list containts the distances 
between every point.  This works because csv file is ordered and each source  '''

# O(1)
def find_distance(address_source, address_dest, dict):
        # dict is in format of <string, List<int> >
    if address_source not in dict.keys():
        print("source address not found")
        return -1
    if address_dest not in dict.keys():
        print("destination address not found.")
        return -1
    index = 0

    for key in dict.keys():
        if key == address_dest: # checks for destination rather than source.  If i get the destination index then all I
            # need to do is  access the dictionary key that is at the index value
            break
        else: # check the next entry
            index += 1
    list = dict[address_source] # create a list for the key, value pair
    return float(list[index]) # grab the value at the column matching the index


def populate_distance_table():
    distance_dict = create_distance_dict()
    dictionary_index = 0
    for key, value in distance_dict.items():
        index = 0

        for distance in value:

            if distance == '':
                # PSUEDO CODE-- value[index] = the dictionary that is at the value's index[dictionary_index] (gettting reciprocal)
                dictionary_list = distance_dict[get_dict_key_str(index, distance_dict)]
                value[index] = dictionary_list[dictionary_index]
                index += 1

            else:
                index += 1
        dictionary_index += 1
    return distance_dict


#distance_dict = populate_distance_table()
# print(distance_dict)
#
# print(find_distance(' 177 W Price Ave', ' 6351 S 900 E', distance_dict))
# print(get_dict_key_str(2, distance_dict))
