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

    def pop(self):
        if self.length == 0:                  #edge case if no item is available in a linked list
            return None      
        self.pre = self.head                  # we make 2 random variables pre and temp
        self.temp = self.head                 # then make both of them point to head
        while self.temp.next is not None:     # then we check while temp.next i.e 4.next is not pointing to None 
            self.pre = self.temp              # we set the value of pre to temp and it will keep taking values of temp which it moves ahead from but since temp reaches end it will point at none and loop stops keeping pre at previous node(one before)
            self.temp = self.temp.next        # and move temp ahead to next node till it reaches the last
        self.tail = self.pre                  # since pre will be pointing to the node before the last node we make the tail to point at pre (basically second last node is now last node pointing to none)
        self.tail.next = None                 # Now tail will point at none instead of old node we popped
        self.length -= 1                      # reduce the length by 1
        if self.length == 0:                   # This case comes if only one node was there it will go in while loop and exit immediately Now self.tail will be already at the only node so same as self.tail = self.pre so doesnt matter and self.tail.next will also point at none so doesnt matter but the length will be reduced from 1 to 0 and therefore the new if
            self.head = None                   # Once the last item is also popped we make the head and tail point to none that is empty Linked List
            self.tail = None
        return self.temp                      # and simply return the node that is been popped
            
        
my_linked_list = LinkedList(4)
my_linked_list.append(7) 
my_linked_list.append(12)
my_linked_list.print_list()
print(my_linked_list.pop())
print(my_linked_list.pop())

print("Head:", my_linked_list.head.value, "Tail:", my_linked_list.tail.value, "Length:", my_linked_list.length)
