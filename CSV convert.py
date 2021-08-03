import csv
from collections import OrderedDict

# # method is used to create a dictionary from CSV
# def create_distance():
#     with open('Distance Table.csv') as csv_file:
#         csv_reader = csv.reader(csv_file, delimiter=',')
#         distance_dict = OrderedDict()
#
#         for line in csv_reader:
#             key = line[0].replace("\n", " ")
#             distance_dict[key] = line[2:30]
#
#     return distance_dict

# method returns the key as a String when given an index
# def get_dict_key_str(index, dict):
#     i = 0
#     for key in dict.keys():
#         if i != index:
#             i += 1
#         else:
#             return str(key)


# my_dict = create_distance()
# # this updates dictionary to complete data
# for key, value in my_dict.items():
#     index = 0
#     dictionary_index = 0
#     for distance in value:
#
#         if distance == '':
#             # PSUEDO CODE-- value[index] = the dictionary that is at the value's index[dictionary_index] (gettting reciprocal)
#             dictionary_list = my_dict[get_dict_key_str(index, my_dict)]
#             value[index] = dictionary_list[dictionary_index]
#             print()
#             index += 1
#         else:
#             index += 1
#     dictionary_index += 1




# this will now create a new csv with complete data
# with open('cleaned_data.csv', 'w') as outfile:
#     csv_writer = csv.writer(outfile)
#     for key,value in my_dict.items():
#         csv_writer.writerow([key,value])





