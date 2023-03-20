class HashTable:                    # will only create the table 
    def __init__(self, size = 7):   # the only argument we pass to it is the size and default parameter is 7
        self.data_map = [None] * size      # list is called data_map which is equal to NONE for each table address and total size we pass will the number of table address created
 
    def _hash(self,key):            # we pass the key to our hash method
        my_hash = 0                # initial value of our variable is 0
        for letter in key:      # Then we loop through each letter from our key
            my_hash = (my_hash + ord(letter) * 23) % len(self.data_map)   # this calculation does is hash + ord(letter) will give the asci key of letter then multiply by 23 bcoz 23 is prime number (any prime number will do) then modulo will give remainder of len of self.data_map ie 7 for now 
        return my_hash       # this will give out a address from 0-6 where our key value pair will be stored

    def print_table(self):
        for i, val in enumerate(self.data_map):
            print(i, ": ", val)

    def set_item(self,key,value):       # recieves a key and value 
        index = self._hash(key)        # we pass the key to our hash function and in return will get an address ie index
        if self.data_map[index] == None:   # we check if that index is empty or not
            self.data_map[index] = []      # we create a empty list only if empty list is not been created at that address
        self.data_map[index].append([key,value])   # we add that key value pair as a list and add it to our initial big list


 
my_hash_table = HashTable()

my_hash_table.set_item("washer", 50)
my_hash_table.set_item("bolts", 140)
my_hash_table.set_item("lumber", 30)



my_hash_table.print_table()