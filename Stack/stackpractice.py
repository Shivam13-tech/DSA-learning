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
            self.height = 1  

    def print_stack(self):
        temp = self.top
        while temp is not None:
            print(temp.value, "Stack item")
            temp = temp.next

    def reversestring(self,str):
        stack = []
        for x in range(len(str)):
            if str[x] != ' ':
                stack.append(str[x])
            else:
                while stack:
                    print(stack.pop(),end='')
                print(' ', end='')
        while stack:
            print(stack.pop(),end='')
        

        


my_stack = stack(4)
# my_stack.print_stack()
my_stack.reversestring("Hello World")