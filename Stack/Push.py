class createNode():
    def __init__(self,value):            # for creating a node
        self.value = value
        self.next = None

class stack():
    def __init__(self,value):
        node = createNode(value)
        self.top = node                   # we make the top point to new node and since we do all operations from the top itself o(1) we dont need bottom
        if self.top == None:
            self.height = 0
        else:
            self.height = 1                   # initial height as 1
        
    def print_stack(self):
        temp = self.top
        while temp is not None:
            print(temp.value, "Stack item")
            temp = temp.next

    def push(self,value):
        node_to_push = createNode(value)
        if self.height == 0:
            self.top = node_to_push
        else:
            node_to_push.next = self.top
            self.top = node_to_push
        self.height += 1
        return self.top.value
    
my_stack = stack(4)
my_stack.push(12)
my_stack.print_stack()
