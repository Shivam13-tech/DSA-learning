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


    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    # def number_of_nodes(self):
    #     temp = self.head
    #     count = 0
    #     while temp is not None:
    #         print(temp.value, "Linkedlist")
    #         count += 1
    #         temp = temp.next
    #     return count

    # def looping(self):
    #     visited_nodes = set()
    #     temp = self.head
    #     while temp is not None:
    #         if temp in visited_nodes:
    #             length = 1
    #             start = temp
    #             curr = start.next
    #             while curr != start:
    #                 length += 1
    #                 curr = curr.next
    #             return length
    #         visited_nodes.add(temp)
    #         temp = temp.next
    #     return 0

    # def palindrome(self):
    # # Step 1: Push nodes onto a stack
    #     temp = self.head
    #     stack = []
    #     while temp is not None:
    #         stack.append(temp)
    #         temp = temp.next
    
    # # Step 2: Compare nodes with popped nodes from stack
    #     curr = self.head
    #     while curr is not None:
    #         node = stack.pop()
    #         print(node.value, "Node")
    #         print(curr.value, "Curr")
    #         if curr.value != node.value:
    #             return False
    #         curr = curr.next
    #     return True

    # def pallindromsecond(self):
    #     slow = self.head
    #     fast = self.head
    #     while fast.next and fast.next.next is not None:   # Finding middle node of LL
    #         slow = slow.next
    #         fast = fast.next.next
    #     # print(slow.value, "slow", fast.value, "fast")  
    #     curr = slow.next
    #     nextnode = curr.next
    #     prev = None
    #     while curr is not None:
    #         nextnode = curr.next
    #         curr.next = prev
    #         prev = curr
    #         curr = nextnode
    #     print(prev.value, 'prev')
    #     pre = self.head
    #     temp = self.tail
    #     while pre is not None and temp is not None:
    #         if pre.value != temp.value:
    #             return False
    #         pre = pre.next
    #         temp = temp.next
    #     return True

    # def removeduplicate(self):
    #     temp = self.head
    #     while temp is not None and temp.next is not None:
    #         if temp.value == temp.next.value:
    #             temp.next = temp.next.next
    #         else:
    #             temp = temp.next
    #     temp = self.head
    #     while temp is not None:
    #         print(temp.value)
    #         temp = temp.next

    # def remove_duplicates_unsorted(self):
    #     stored_nodes = set()
    #     temp = self.head
    #     pre = None
    #     while temp is not None:
    #         if temp.value in stored_nodes:
    #             pre.next = temp.next
    #             temp = None
    #         else:
    #             stored_nodes.add(temp.value)
    #             pre = temp
    #         temp = pre.next
    #     temp = self.head
    #     while temp is not None:
    #         print(temp.value)
    #         temp = temp.next
    #         return True


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

def find_intersection(head1,head2):
        intersection = []
        ptr1 = head1
        ptr2 = head2
        while ptr1 and ptr2 is not None:
            if ptr1.value == ptr2.value:
                intersection.append(ptr1.value)
                ptr1 = ptr1.next
                ptr2 = ptr2.next
            elif ptr1.value < ptr2.value:
                ptr1 = ptr1.next
            else:
                ptr2 = ptr2.next
        return intersection
     

my_linked_list = LengthofLL(1)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(4)
my_linked_list.append(6)
my_linked_list2 = LengthofLL(2)
my_linked_list2.append(4)
my_linked_list2.append(6)
my_linked_list2.append(8)
# print(my_linked_list.print_list())
# print(my_linked_list2.print_list())
result = find_intersection(my_linked_list.head, my_linked_list2.head)
print(result)


# print(my_linked_list.remove_duplicates_unsorted())
# print(my_linked_list.pallindromsecond())
# print(my_linked_list.number_of_nodes())
# print(my_linked_list.looping())