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
        self.length = 1                # Initial length being 1

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
        return temp.value



my_doubly_linked_list = DoublyLinkedList(4)
my_doubly_linked_list.append(3)
my_doubly_linked_list.append(7)
my_doubly_linked_list.append(12)
print(my_doubly_linked_list.get(1))
my_doubly_linked_list.print_list()

print("Head:", my_doubly_linked_list.head.value, "Tail:", my_doubly_linked_list.tail.value, "Length:", my_doubly_linked_list.length) #gives the value where the head is pointing