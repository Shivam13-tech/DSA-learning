class Node:                 #  This will just create a node 
    def __init__(self,value):
        self.value = value
        self.next = None

class LinkedList:             
    def __init__(self, value):
        new_node = Node(value)                          # Creates a new node
        self.head = new_node                            # the head is pointing at none (default values)
        self.tail = new_node                            # the tail is pointing at none (default values)
        self.length = 1                                 # Initial length is 1 (default value )

    def print_list(self):                               # While loop to just print the linked list
        temp = self.head
        while temp is not None:
            print(temp.value, "Linkedlist")
            temp = temp.next       

    def append(self,value):
        node_to_append = Node(value)                   # Creates a new node for the value passed
        if self.head.value == None:                          # if no value exist in our linked list
            self.head = node_to_append   # Make the head point to new node created
            self.tail = node_to_append   # Make the tail point to new node created
        else:
            self.tail.next = node_to_append   # we point the tail to the new added node
            self.tail = node_to_append        # we provide the new value to our tail pointer
        self.length += 1                      # Whatever scenario we increase the initial length by 1 of our Linkedlist
        return True                           # Just in case there will be functions which will call this function and expect a reply of T or F
        
my_linked_list = LinkedList(None)
my_linked_list.append(7)
# my_linked_list.append(12) 
my_linked_list.print_list()


print("Head:", my_linked_list.head.value, "Tail:", my_linked_list.tail.value, "Length:", my_linked_list.length) #gives the value where the head is pointing

