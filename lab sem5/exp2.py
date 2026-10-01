'''
Write a program to illustrate iteration over the list and dictionary.
'''

my_list = [1, 2, 3, 4, 5]
print("Iterating over the list:")
for item in my_list:
    print(item, end=' ')

my_dict = {'a': 1, 'b': 2, 'c': 3}
print("\nIterating over the dictionary:")
for key, value in my_dict.items():
    print(key, ":", value)