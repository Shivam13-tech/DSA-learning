class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class Queue:
    def __init__(self,value):
        new_node = Node(value)
        self.first = new_node
        self.last = new_node
        if self.first is not None:
            self.length = 1
        else :
            self.length = 0

    def print_queue(self):
        temp = self.first
        while temp is not None:
            print(temp.value, "queue item")
            temp = temp.next

    def enqueue(self,value):
        node_to_enqueue = Node(value)        
        if self.length == 0:                 # if empty queue we make our first and last point to new node 
            self.first = node_to_enqueue
            self.last = node_to_enqueue
        else:
            self.last.next = node_to_enqueue     # we make old last node point to our new node
            self.last = node_to_enqueue          # then move last to our new node 
        self.length += 1

my_queue = Queue(4)
my_queue.enqueue(5)
my_queue.print_queue()
