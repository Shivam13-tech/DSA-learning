class Node:
    def __init__(self,value):         # Here we create a normal node and next and prev pointing to none
        self.value = value
        self.next = None
        self.prev = None

class DoublyLinkedList:               
    def __init__(self,value):         # Same as prev linked list creation with head and tail pointing to new node
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        if new_node.value is not None:
            self.length = 1                                 # Initial length is 1 (default value )
        else:
            self.length = 0                                 # Initial lenght is 0

    def print_list(self):              # While loop to just print the linked list
        temp = self.head
        while temp is not None:
            print(temp.value, "Linkedlist")
            temp = temp.next     

    def append(self,value):
        node_to_append = Node(value)
        if self.head.value is None:          # To check if the linked list is empty then head and tail points to the new node
            self.head = node_to_append
            self.tail = node_to_append
        else :
            self.tail.next = node_to_append     # we make tail(last node .next) point to our new node
            node_to_append.prev = self.tail     # and new node prev pointer to the last node that was tail
            self.tail = node_to_append          # and finally move tail to the last node we appended
        self.length += 1 
        return True 

    def prepend(self,value):
        node_to_prepend = Node(value)
        if self.length == 0:                    # if no node exist then make head and tail point to this new created node
            self.head = node_to_prepend 
            self.tail = node_to_prepend
        else:
            node_to_prepend.next = self.head     # we make new node.next point to the head node ie first node
            self.head.prev = node_to_prepend     # we make head node ie first node . prev point to the new node created
            self.head = node_to_prepend          # then we make the new node the head of our linked list
        self.length += 1
        return True
    
    
    def get(self,index):
        if index < 0 or index > self.length:        #we check for index is not out of range
            return None
        temp = self.head                          # we set temp to head
        if index < self.length / 2:             #i.e if index is less then half our linked list length then
            for _ in range(index):
                temp = temp.next
        else:
            temp = self.tail                         # else we set temp to tail and do backwards for loop to get item
            for _ in range(index, self.length - 1, -1):  #index is passed for range, second parameter is length - 1 and third parameter is decrement by 1
                temp = temp.prev
        return temp

    def insert(self,index,value):
        if index < 0 or index > self.length:           # to check if index is not out of range
            return False
        if index == 0:                             # if in the start of our list then prepend method
            return self.prepend(value) 
        if index == self.length:                   # if in the end our list then append method
            return self.append(value)
        node_to_insert = Node(value)           # else we create a new node 
        before = self.get(index - 1)          #before variable which will point to the prev index to the index we want to add
        after = before.next                  #after vairbale will be at the index we want to add ie before.next
        before.next = node_to_insert         #we make before.next which is pointing to the place we want to add our node to point at our new node
        after.prev = node_to_insert        #we make after.prev which is pointing to the previous node we make it point at our new node
        node_to_insert.prev = before         #we make new node prev to point at before node ie index before where we want to add
        node_to_insert.next = after           #we make new node next to point at after node ie index where we want to add
        self.length += 1
        return True




my_doubly_linked_list = DoublyLinkedList(4)
my_doubly_linked_list.append(3)
my_doubly_linked_list.prepend(7)
print(my_doubly_linked_list.insert(2,12))

my_doubly_linked_list.print_list()

print("Head:", my_doubly_linked_list.head.value, "Tail:", my_doubly_linked_list.tail.value, "Length:", my_doubly_linked_list.length) #gives the value where the head is pointing