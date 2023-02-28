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


    def popfirst(self):
        if self.length == 0:                  # if we have no item in our linked list then we have nothing to pop from first therefore directly return
            return None
        temp = self.head                 # then if we have item so we store the first item that we plan to pop in a variable to return
        self.head = self.head.next            # then we make the head value point to the next item of the list
        temp.next = None                 # to remove that item from the list and have it point to none
        self.length -= 1                      # reduce the length of the list by 1 since 1 item is poped
        if self.length == 0:                # if after reducing the length of our linked list and there is no item left 
            self.head = None                       # then we make our head and tail point to none ie now currently we have no item in our linked list
            self.tail = None
        return temp    

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

    def remove(self,index):
        if index < 0 or index > self.length:        # to check if the index where we plan to add value is not out of range
            return None                             # In insert we return false bcoz we want to know if successfull then true or false but in remove we want to return a node therefore its none here
        if index == 0:                               # if we want to remove from the start of our list then we call to our popfirst function to remove node at the start of Linked List
            return self.popfirst()                    # and return bcoz once remove we just want to exit 
        if index == self.length - 1:               # if we want to remove to the end of our linked list then we call to our pop function which remove node to the end of our Linked List 
            return self.pop()
        # temp = self.get(index)                # we create a temp variable which will be equal to the value we get from index but this is o(n) there is more effiecient way on next to next line 
        pre = self.get(index - 1)             # we create a pre variable which will be equal to the value we get from index - 1 ie will give one value previous to the temp value
        temp = pre.next                        # same as creating a temp variable from index but more efficient
        pre.next = temp.next                  # then we make pre variable point to the node which is after the temp variable
        temp.next = None                      # so that temp node is now pointing at none and not the next node
        self.length -= 1
        return temp                          #return the removed node
        
            




my_linked_list = LinkedList(4) 
my_linked_list.append(7)  
my_linked_list.append(12)  
my_linked_list.remove(1)
my_linked_list.print_list()

print("Head:", my_linked_list.head.value, "Tail:", my_linked_list.tail.value, "Length:", my_linked_list.length)
  