# def bubble_sort(my_list):
#     for i in range(len(my_list) - 1, 0, -1):
#         for j in range(i):
#             if my_list[j] > my_list[j+1]:
#                 temp = my_list[j]
#                 my_list[j] = my_list[j+1]
#                 my_list[j+1] = temp
#     return my_list


def bubble_sort(my_list):
    n = len(my_list)
    for i in range(n - 1):     
        for j in range(n - i - 1): 
            if my_list[j] > my_list[j+1]:
                my_list[j],my_list[j+1] = my_list[j+1],my_list[j]
    return my_list 





print(bubble_sort([4,2,6,5,1,3]))

# Working of this code :

# We define a function called bubble_sort that takes a list called my_list as input.

# We determine the length of the list and store it in the variable n.

# We use the first loop to iterate n - 1 times. 
# This loop controls the number of passes through the list.

# Within the outer loop, we use the second loop to compare adjacent elements 
# and swap them if they are in the wrong order.

# In the second loop, j iterates from 0 to n - i - 1. 
# The n - i - 1 is used to avoid comparing already sorted elements in subsequent iterations. 
# So in each pass, we compare elements up to the unsorted portion of the list.
# Pass 1: j iterates from 0 to 5 (all elements are compared)
# Pass 2: j iterates from 0 to 4 (the largest element 6 is already in place)
# Pass 3: j iterates from 0 to 3 (the two largest elements 5 and 6 are already in place)
# Pass 4: j iterates from 0 to 2 (the three largest elements 4, 5, and 6 are already in place)

# If the element at position j is greater than the element at position j+1, 
# we swap their positions.

# After completing all the passes and comparisons, we return the sorted list.
# Let's take an example to see how it works:

# my_list = [4, 2, 6, 5, 1, 3]
# In the first pass, we compare adjacent elements and swap them if necessary. 
# The largest element will bubble up to the last position.
# Compare 4 & 2 then swap since j is bigger then j + 1 = [2,4,6,5,1,3]
# Compare 4 & 6 since j is not bigger then j + 1 = [2,4,6,5,1,3]
# Compare 6 & 5 then swap since j is bigger then j + 1 = [2,4,5,6,1,3]
# Compare 6 & 1 then swap since j is bigger then j + 1 = [2,4,5,1,6,3]
# Compare 6 & 3 then swap since j is bigger then j + 1 = [2,4,5,1,3,6]
# After the first pass: [2, 4, 5, 1, 3, 6]

# In the second pass, we compare adjacent elements and swap them if necessary.
# The second largest element will bubble up to the second-to-last position.
# After the second pass: [2, 4, 1, 3, 5, 6]

# In the third pass, we compare adjacent elements and swap them if necessary.
# The third largest element will bubble up to the third-to-last position.
# After the third pass: [2, 1, 3, 4, 5, 6]

# In the fourth pass, we compare adjacent elements and swap them if necessary. 
# The fourth largest element will bubble up to the fourth-to-last position.
# After the fourth pass: [1, 2, 3, 4, 5, 6]

# The list is now sorted in ascending order.