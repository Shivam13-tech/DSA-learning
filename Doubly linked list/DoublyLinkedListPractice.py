class Node:
    def __init__(self,value):
        self.next = None
        self.prev = None
        self.value = value

class Doublylinkedlist:
    def __init__(self,value):
        node = Node(value)
        self.head = node
        self.tail = node
        self.length = 1

    def append(self,value):      #Not taking edge cases for practice 
        append_node = Node(value)
        self.tail.next = append_node
        append_node.prev = self.tail
        self.tail = append_node
        self.length += 1
    
    def print_list(self):
        temp = self.head
        while temp:
            print(temp.value)
            temp = temp.next

    def reverseDll(self):
        temp = self.head
        before = None
        while temp:
            temp.prev = temp.next
            temp.next = before
            before = temp
            temp = temp.prev
        self.head = before

my_DLL = Doublylinkedlist(1)
my_DLL.append(2)
my_DLL.append(3)
my_DLL.reverseDll()
my_DLL.print_list()