my_dict = {'apple': 3, 'orange': 1, 'banana': 2, 'grape': 4}

my_dict_reversed = {values:key for key, values in my_dict.items()}
# Sort by key (ascending)
print(my_dict)
print(my_dict_reversed.items)
# print(sorted(my_dict.items()), )