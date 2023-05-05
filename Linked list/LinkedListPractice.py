class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class LengthofLL:
    def __init__(self,value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def number_of_nodes(self):
        temp = self.head
        count = 0
        while temp is not None:
            print(temp.value, "Linkedlist")
            count += 1
            temp = temp.next
        return count

    def looping(self):
        visited_nodes = set()
        temp = self.head
        while temp is not None:
            if temp in visited_nodes:
                length = 1
                start = temp
                curr = start.next
                while curr != start:
                    length += 1
                    curr = curr.next
                return length
            visited_nodes.add(temp)
            temp = temp.next
        return 0


    def append(self,value):
        node_to_append = Node(value)
        if self.head == None:
            self.head = node_to_append
            self.tail = node_to_append
        else:
            self.tail.next = node_to_append
            self.tail = node_to_append
        self.length += 1
        return True

my_linked_list = LengthofLL(1)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(4)
my_linked_list.append(3)
# print(my_linked_list.number_of_nodes())
print(my_linked_list.looping())