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

    def pop(self):
        if self.length == 0:             #if no value to pop then directly exit
            return None
        temp = self.tail                     # temp variable pointing to tail
        if self.length == 1:
             self.head = None
             self.tail = None
        else:
            self.tail = self.tail.prev           # making tail move to the prev node
            self.tail.next = None                # making tail.next to none (making it last node)
            temp.prev = None                     # detaching the last node from new tail
        self.length -= 1                     # decrement the length of our linked list by 1
        return temp

    def popfirst(self):
        if self.length == 0:         #if no value to pop then directly exit
            return None
        temp = self.head             # a temporary variable pointing to head
        if self.length == 1:         # if only 1 node so after pop head and tail will be pointing to none
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next        # we move head to the next node
            self.head.prev = None        # we make new head . previous pointer to none 
            temp.next = None             # then make temp.next which is pointing to new head to be none so its completely detached
        self.length -= 1
        return temp
    
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

    def remove(self,index):
        if index < 0 or index >= self.length:           # to check if index is not out of range
            return False
        if index == 0:                             # if in the start of our list then popfirst method
            return self.popfirst() 
        if index == self.length - 1:                   # if in the end our list then pop method
            return self.pop()
        remove_node = self.get(index)              # we make a variable point to the index we want to remove
        before = remove_node.prev           # we make a before variable pointing to previous of the node we want to remove
        after = remove_node.next           # we make a after variable pointing to next of the node we want to remove
        before.next = after             # then we first make before and after connect with one another
        after.prev = before
        remove_node.next = None        # then we make the node we want to remove both prev and next pointer to None so its detached
        remove_node.prev = None
        self.length -= 1

        # remove_node.next.prev = remove_node.prev            # if we dont want multiple variable
        # remove_node.prev.next = remove_node.next
        # remove_node.prev = None
        # remove_node.next = None


my_doubly_linked_list = DoublyLinkedList(4)
my_doubly_linked_list.append(3)
my_doubly_linked_list.append(12)
# my_doubly_linked_list.popfirst()
# my_doubly_linked_list.pop()
print(my_doubly_linked_list.remove(2))
my_doubly_linked_list.print_list()

print("Head:", my_doubly_linked_list.head.value, "Tail:", my_doubly_linked_list.tail.value, "Length:", my_doubly_linked_list.length) #gives the value where the head is pointing