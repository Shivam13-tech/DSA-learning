# def insertion_sort(my_list):
#     for i in range(1, len(my_list)):
#         temp = my_list[i]
#         j = i-1
#         while temp < my_list[j] and j > -1:
#             my_list[j+1] = my_list[j]
#             my_list[j] = temp
#             j -= 1
#     return my_list

def insertion_sort(my_list):
    n = len(my_list)
    for i in range(1,n):
        key = my_list[i]
        j = i - 1
        while j >= 0 and my_list[j] > key:
            my_list[j+1] = my_list[j]
            j -= 1
        my_list[j+1] = key
    return my_list


print(insertion_sort([4,2,6,5,1,3]))

# Steps:

# We start a loop from the second element of the array (i = 1) to the last element. 
# The variable i represents the current element that needs to be inserted at the correct position.

# We store the value of the current element (my_list[i]) in a variable called key.

# We initialize a variable j with the index of the element just before the current element (j = i - 1). 
# This variable represents the position of the last element in the sorted portion of the array.

# We enter a while loop that continues as long as j is greater than or equal to 0 (to avoid going out of bounds) 
# and the element at index j is greater than the key value.

# Inside the while loop, we shift the elements of the 
# sorted portion of the array that are greater than the key value one position ahead. 

# This creates space for the key element to be inserted at the correct position.

# We keep decrementing j by 1 in each iteration, effectively 
# moving towards the beginning of the sorted portion of the array.

# Once we find the correct position for the key element, 
# we insert it into the array at arr[j + 1]. 

# This position is one index ahead of the current j because we decremented j in the previous step.

# Round 1:

# i = 1, key = 2
# j = 0
# While loop condition: j >= 0 (True) and arr[j] > key (4 > 2)
# While loop condition: j >= 0 (False)
# Insertion: arr[j + 1] = key (arr[0] = 2)
# Updated array: [2, 4, 6, 5, 1, 3]

# Round 2:

# i = 2, key = 6
# j = 1
# While loop condition: j >= 0 (True) and arr[j] > key (4 > 6)
# While loop condition: j >= 0 (False)
# Insertion: arr[j + 1] = key (arr[1] = 6)
# Updated array: [2, 4, 6, 5, 1, 3]

# Round 3:

# i = 3, key = 5
# j = 2
# While loop condition: j >= 0 (True) and arr[j] > key (6 > 5)
# While loop condition: j >= 0 (False)
# Insertion: arr[j + 1] = key (arr[2] = 5)
# Updated array: [2, 4, 5, 6, 1, 3]

# Round 4:

# i = 4, key = 1
# j = 3
# While loop condition: j >= 0 (True) and arr[j] > key (6 > 1)
# Shifting: arr[4] = arr[3] (1 <- 6)
# j decremented: j = 2
# While loop condition: j >= 0 (True) and arr[j] > key (5 > 1)
# Shifting: arr[3] = arr[2] (6 <- 5)
# j decremented: j = 1
# While loop condition: j >= 0 (True) and arr[j] > key (4 > 1)
# Shifting: arr[2] = arr[1] (5 <- 4)
# j decremented: j = 0
# While loop condition: j >= 0 (True) and arr[j] > key (2 > 1)
# Shifting: arr[1] = arr[0] (4 <- 2)
# j decremented: j = -1
# While loop condition: j >= 0 (False)
# Insertion: arr[j + 1] = key (arr[0] = 1)
# Updated array: [1, 2, 4, 5, 6, 3]

# Round 5:

# i = 5, key = 3
# j = 4
# While loop condition: j >= 0 (True) and arr[j] > key (6 > 3)
# While loop condition: j >= 0 (True) and arr[j] > key (5 > 3)
# While loop condition: j >= 0 (True) and arr[j] > key (4 > 3)
# While loop condition: j >= 0 (True) and arr[j] > key (2 > 3)
# While loop condition: j >= 0 (False)
# Insertion: arr[j + 1] = key (arr[3] = 3)
# Updated array: [1, 2, 4, 3, 5, 6]
# After completing all the rounds, the array is fully sorted. The final sorted array is [1, 2, 3, 4, 5, 6].