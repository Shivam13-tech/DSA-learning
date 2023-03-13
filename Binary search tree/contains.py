class Node:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None                            # we don't start with a default node we just make root point to none and will add values with insert method


    def insert(self,value):
        new_node = Node(value)           # we create a new node
        if self.root == None:           # check if tree is empty then make root point to our new node
            self.root = new_node
            return True
        temp = self.root            # we make a temp variable point to root so from there we can loop through our tree
        while (True):                # we keep on looping till we find our condition and then will switch to False
            if new_node.value == temp.value:         # we compare if the value we plan to add already exist in our tree hence no comparison 
                return False
            if new_node.value < temp.value:           # we start comparison 1 to make the node move to the left
                if temp.left is None:               # case 1.1 if left side of temp is empty then we add our node there
                    temp.left = new_node
                    return True                # return so we can exit
                temp = temp.left           # we make temp variable move to the left 
            else :                        # we start comparison 2 ie if new node value is greater then temp we move to the right
                if temp.right is None:
                    temp.right = new_node        # All same code for right side  scenario
                    return True
                temp = temp.right

    def contains(self,value):
        if self.root == None:          # we check if our tree is empty then return false
            return False
        temp = self.root           # we create a temp variable to point at root from where we will loop
        while (temp is not None):             # temp will only point at none if it has done travelling and the value doesnt exist
            if value < temp.value:  
                temp = temp.left                  # if value is less move to left and it will again go through the loop
            elif value > temp.value:
                temp = temp.right                 # if value is greater it will move to right and again loop
            else:                          
                return True                       # untill it finds the value and then will exit
        return False                              # if item doesnt exist we will exit our loop


        

my_binary_search_tree = BinarySearchTree()
my_binary_search_tree.insert(2)
my_binary_search_tree.insert(3)
my_binary_search_tree.insert(1)



print(my_binary_search_tree.contains(7))



            
        
