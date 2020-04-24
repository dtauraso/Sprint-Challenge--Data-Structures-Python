import time
from binary_search_tree import BinarySearchTree

def binary_search_tree_version(names_1, names_2):
    my_tree = BinarySearchTree('root')

    for name in names_1:
        # O(log(n))
        if(my_tree.contains(name)):
            duplicates.append(name)
        else:
            my_tree.insert(name)

    for name in names_2:
        if(my_tree.contains(name)):
            duplicates.append(name)
        else:
            my_tree.insert(name)
    return duplicates
def stretch_goal_find(array, new_item):

    low = 0
    high = len(array) - 1

    while low <= high:
        mid = (low + high) // 2
        if new_item <= array[mid]:
            high = mid - 1
        else:
            low = mid + 1

    # might also work for contains but have no time to test that
    return low
def stretch_goal_contains(array, new_item):

    low = 0
    high = len(array) - 1

    while low <= high:
        mid = (low + high) // 2
        if new_item < array[mid]:
            high = mid - 1
        elif new_item == array[mid]:
            return mid
        else:
            low = mid + 1

    return -1

def stretch_goal_insert(array, new_item):
    location = stretch_goal_find(array, new_item)

    # print(location)
    if len(array) == 0:
        array = [new_item]
    else:

        # big slowdown probably occurred here
        if location == 0:
            array = array[0:location] + [new_item] + array[location:]
        elif location == len(array) - 1:
            array.append(new_item)
        else:
            # print('here')
            array = array[0: location] + [new_item] + array[location:]
    return array

def stretch_goal_check_names(names_1, names_2):
    # my_tree = BinarySearchTree('root')

    # 4 seconds faster than default and missed 1 duplicate(only found 123 instead of 124 for both files)

    
    array = []

    for name in names_1:
        # O(log(n))
        if(stretch_goal_contains(array, name) > -1):
            duplicates.append(name)
        else:
            array = stretch_goal_insert(array, name)
            # my_tree.insert(name)

    for name in names_2:
        if(stretch_goal_contains(array, name) > -1):
            duplicates.append(name)
        else:
            array = stretch_goal_insert(array, name)
    return duplicates
def add_to_dict(my_names, name):

    if name not in my_names:
        my_names[name] = 1
    else:
        my_names[name] += 1
def dictionary_version(names_1, name_2):

    my_names = {}
    duplicates = []
    for name in names_1:
        add_to_dict(my_names, name)

        if my_names[name] > 1:
            duplicates.append(name)

    for name in names_2:
        add_to_dict(my_names, name)

        if my_names[name] > 1:
            duplicates.append(name)
    return duplicates
start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure


# my_tree = BinarySearchTree('root')

# O(n^2)
# only found 64 duplicates
# Replace the nested for loops below with your improvements
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)

# all 3 improvements detected more duplicates than original
# each file has duplicates too so the number nearly doubled in a 10th of the time
# for name in names_1:
#     if(my_tree.contains(name)):
#         duplicates.append(name)
#     else:
#         my_tree.insert(name)

# for name in names_2:
#     if(my_tree.contains(name)):
#         duplicates.append(name)
#     else:
#         my_tree.insert(name)

# binary search tree way O(nlog(n)) extra n for all the items bein added
# runtime: 0.2764101028442383 seconds
# duplicates = binary_search_tree_version(names_1, names_2)


# the accepted stretch goal O(nlog(n)) - almost as slow as the original
# binary search style insert into array
# input_ = [1,3,5,6]

# array = []
# for item in input_:
#     array = stretch_goal_insert(array, item)
#     print(array)

# array = stretch_goal_insert(array, 2)
# print(array)

# array = stretch_goal_insert(array, 0)
# print(array)

# array = stretch_goal_insert(array, 7)
# print(array)
# runtime: 2.8387720584869385 seconds
duplicates = stretch_goal_check_names(names_1, names_2)

# the illegal but fast way  O(n) no log(n) as dicts use O(1) lookups
# runtime: 0.007953882217407227 seconds
# duplicates = dictionary_version(names_1, names_2)
end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")


# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
