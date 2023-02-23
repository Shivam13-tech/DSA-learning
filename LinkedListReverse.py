class Node:                 #  This will just create a node 
    def __init__(self,value):
        self.value = value
        self.next = None

class LinkedList:             
    def __init__(self, value):
        new_node = Node(value)                          # Creates a new node
        self.head = new_node                            # the head is pointing at firstnode (default values)
        self.tail = new_node                            # the tail is pointing at firstnode (default values)
        if new_node.value is not None:
            self.length = 1                                 # Initial length is 1 (default value )
        else:
            self.length = 0                                 # Initial lenght is 0

    def print_list(self):                               # While loop to just print the linked list
        temp = self.head
        while temp is not None:
            print(temp.value, "Linkedlist")
            temp = temp.next 

    
    def get(self,index):
        if index < 0 or index >= self.length:      # we check if the index pass is not negative or the index is not greater then the length of our linkedlist
            return None
        temp = self.head                           # we make a temporary variable which is pointing to head 
        for _ in range(index):                     # when we do not plan to use a variable from a for loop we use underscore(_) this loop so it can iterate through the linked list
            temp = temp.next                       # we move the temp ahead to the next node
        return temp                                # this will move temp ahead till the index we want and then we simply return the temp node

    def append(self,value):
        node_to_append = Node(value)                   # Creates a new node for the value passed
        if self.head.value == None:                          # if no value exist in our linked list
            self.head = node_to_append              # Make the head point to new node created
            self.tail = node_to_append              # Make the tail point to new node created
        else:
            self.tail.next = node_to_append   # we point the tail to the new added node
            self.tail = node_to_append        # we provide the new value to our tail pointer
        self.length += 1                      # Whatever scenario we increase the initial length by 1 of our Linkedlist
        return True                           # Just in case there will be functions which will call this function and expect a reply of T or F

        
    def reverse(self):
        temp = self.head                     # to make the head point to tail and tail point to head we use a temporary variable
        self.head = self.tail                # we make the head point to tail
        self.tail = temp                     # we make the tail point to temp ie head
        after = temp.next                    # Now we create two extra variable one before temp ie head and one after temp
        before = None                        # Variable 2
        for _ in range(self.length):         # we iterate through our Linkedlist
            after = temp.next                # we make after to temp.next {which will be the same initially declared earlier}
            temp.next = before               # we make temp.next which is pointing ahead to be switch on the opp side {which is initially ie before is none so first node is now pointing at None}       
            before = temp                    # now we cannot break our linked list directly its bad to make a gap like this therefore we now make the before pointing to temp
            temp = after                     # and temp is pointing to after and this way the cycle continues with after = temp.next so it keeps moving ahead and closes the gap
              




my_linked_list = LinkedList(4) 
my_linked_list.append(7)  
my_linked_list.append(12)  
my_linked_list.reverse()
my_linked_list.print_list()

print("Head:", my_linked_list.head.value, "Tail:", my_linked_list.tail.value, "Length:", my_linked_list.length)
  