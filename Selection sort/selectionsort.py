# def selection_sort(my_list):
#     for i in range(len(my_list)-1):
#         min_index = i
#         for j in range(i+1, len(my_list)):
#             if my_list[j] < my_list[min_index]:
#                 min_index = j
#         if i != min_index:
#             temp = my_list[i]
#             my_list[i] = my_list[min_index]
#             my_list[min_index] = temp
#     return my_list

def selection_sort(my_list):
    n = len(my_list)
    for i in range(n - 1):
        min_index = i
        for j in range(i+1, n):
            if my_list[j] < my_list[min_index]:
                min_index = j
        my_list[i],my_list[min_index] = my_list[min_index],my_list[i]
    return my_list

print(selection_sort([4,2,6,5,1,3]))

# Steps: 

# The variable n is assigned the length of the list my_list, 
# which represents the total number of elements in the list. In this case, n will be 6.

# The variable min_index is initialized with the value of i. 
# It represents the index of the minimum element in the unsorted portion of the list.

# The inner loop iterates from i + 1 to n ie end of the list.
# In the first iteration of the outer loop, it runs from 1 to 5.
# The loop variable j represents the index of the elements in the unsorted portion.


# In each iteration of the inner loop, we compare the element at index j with the element at index min_index.
# If the element at j is smaller than the current minimum element (my_list[min_index]),
# we update min_index to j. This helps us find the index of the minimum element in the unsorted portion of the list.

# For example, when j = 1 and min_index = 0, the element at index 1 (my_list[1]) is 2, 
# which is smaller than the current minimum element (my_list[0] = 4). 
# Therefore, min_index is updated to 1.

# After finding the index of the minimum element, 
# we swap it with the element at index i. 
# This places the minimum element in its correct position at the beginning of the sorted portion of the list.

# For example, when i = 1 and min_index = 4, 
# the minimum element (my_list[min_index]) is 1, and the element at index 1 (my_list[i]) is 2. 
# The swap operation exchanges the positions of these elements, resulting in the updated list: 
# [4, 1, 6, 5, 2, 3]

#Code flow: 

# Round 1:

# i = 0, min_index = 0, n = 6
# Inner loop (from j = 1 to j = 5):
# j = 1: Compare my_list[1] (2) with my_list[0] (4). Since 2 is smaller, update min_index = 1.
# j = 2: Compare my_list[2] (6) with my_list[1] (2). No update to min_index.
# j = 3: Compare my_list[3] (5) with my_list[1] (2). No update to min_index.
# j = 4: Compare my_list[4] (1) with my_list[1] (2). Update min_index = 4.
# j = 5: Compare my_list[5] (3) with my_list[1] (2). No update to min_index.
# Swap my_list[0] (4) with my_list[4] (1): [1, 2, 6, 5, 4, 3]
# Round 2:

# i = 1, min_index = 1, n = 6
# Inner loop (from j = 2 to j = 5):
# j = 2: Compare my_list[2] (6) with my_list[1] (2). No update to min_index.
# j = 3: Compare my_list[3] (5) with my_list[1] (2). No update to min_index.
# j = 4: Compare my_list[4] (4) with my_list[1] (2). No update to min_index.
# j = 5: Compare my_list[5] (3) with my_list[1] (2). Update min_index = 5.
# Swap my_list[1] (2) with my_list[5] (3): [1, 2, 6, 5, 4, 3]
# Round 3:

# i = 2, min_index = 2, n = 6
# Inner loop (from j = 3 to j = 5):
# j = 3: Compare my_list[3] (5) with my_list[2] (6). No update to min_index.
# j = 4: Compare my_list[4] (4) with my_list[2] (6). Update min_index = 4.
# j = 5: Compare my_list[5] (3) with my_list[2] (6). Update min_index = 5.
# Swap my_list[2] (6) with my_list[4] (4): [1, 2, 4, 5, 6, 3]
# Round 4:

# i = 3, min_index = 3, n = 6
# Inner loop (from j = 4 to j = 5):
# j = 4: Compare my_list[4] (6) with my_list[3] (5). No update to min_index.
# j = 5: Compare my_list[5] (3) with my_list[3] (5). Update min_index = 5.
# Swap my_list[3] (5) with my_list[5] (3): [1, 2, 4, 3, 6, 5]
# Round 5:

# i = 4, min_index = 4, n = 6
# Inner loop (from j = 5 to j = 5):
# j = 5: Compare my_list[5] (5) with my_list[4] (6). No update to min_index.
# No swap is performed as the minimum element is already at its correct position.
# The sorting process is now complete. The final sorted list is [1, 2, 3, 4, 5, 6].