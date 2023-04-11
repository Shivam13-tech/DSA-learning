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

    def dfs_pre_order(self):
        results = []

        def traverse(current_node):
            results.append(current_node.value)
            if current_node.left is not None:
                traverse(current_node.left)
            if current_node.right is not None:
                traverse(current_node.right)
        
        traverse(self.root)
        return results

my_binary_search_tree = BinarySearchTree()
my_binary_search_tree.insert(47)
my_binary_search_tree.insert(21)
my_binary_search_tree.insert(76)
my_binary_search_tree.insert(18)
my_binary_search_tree.insert(27)
my_binary_search_tree.insert(52)
my_binary_search_tree.insert(82)

print(my_binary_search_tree.dfs_pre_order())




# print(my_binary_search_tree.root.value)       # gives initial value
# print(my_binary_search_tree.root.left.value)        # will give left side value
# print(my_binary_search_tree.root.right.value)       # will give right side value

            
        




