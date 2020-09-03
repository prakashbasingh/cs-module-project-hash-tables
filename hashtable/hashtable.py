class HashTableEntry:
    """
    Linked List hash table key/value pair
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity):
        # Your code here          
        self.capacity = capacity
        self.table = [None] * capacity
        self.sum = 0
        
 

    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        # Your code here
        return self.capacity


    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        # Your code here
        return self.sum / self.capacity

    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """

        # Your code here
        pass


    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        
        unsigned long hash(char *str)
        {
            unsigned long hash = 5381;
            int c;

            while (c = *str++)
                hash = ((hash << 5) + hash) + c; /* hash * 33 + c */

            return hash;
        }
        """
        # Your code here
        hash_value = 5381
        
        for c in key:
            # hash_value = ((hash_value << 5) + hash_value) + ord(c)
            #  OR
            hash_value = (hash_value * 33) + ord(c)
            
        return hash_value
        


    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        #return self.fnv1(key) % self.capacity
        return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        # Your code here
        # Which slot (aka index) in the table is the value going?
        index = self.hash_index(key)
 
        # checking if cur index has something, if nothing then
        if self.table[index] == None:
            self.table[index] = HashTableEntry(key, value) # if there is nothing then it will create a new entry
            self.sum += 1 # keeping track of entry
        # if cur index has something then
        else:
            cur_node = self.table[index]
            # looping through the table
            while cur_node is not None:
                if cur_node.key == key: # checking if key is already there
                    cur_node.value = value # overriding the previous value
                    return
                # checking if cur_node key is equal to key
                if cur_node.next == None:
                    cur_node.next = HashTableEntry(key, value) # adding new entry
                    self.sum +=1
                    return
                cur_node = cur_node.next    
        # now checking load factor and if necessary need to double the capacity of the table
        if self.get_load_factor() > 0.7:
            self.resize(self.capacity * 2)
 
        
    def delete(self, key):
        """
        Remove the value stored with the given key.
        Print a warning if the key is not found.
        Implement this.
        """
        # Your code here
        # getting the key
        index = self.hash_index(key)
        cur = self.table[index]
 
        if cur.key == key: # if first element/ head is to be deleted
            if cur.next == None: # if there is no other items
                self.table[index] = None # deleting the head
                self.sum -= 1 # decrementing the item count
            else: # if there are other items
                new_head = cur.next # this will set new-head as the second item
                cur.next = None # removing the pointer from old head to the second item(new_head now)
                cur = new_head # this will assign current to the new_head
                self.sum -= 1 # decrementing the item count
        else: # if key is not the head or not found
            if cur == None: # if there is no entry
                return None
            else:
                prev = None
                # while loop- looking through all the items 
                while cur.next != None and cur.key != key:
                    prev = cur # current key is now previous item
                    cur = cur.next # the next item becomes the current item
                if cur.key == key: # if key is found
                    prev.next = cur.next # it removes the references/pointer to the key
                    self.sum -= 1 # decrementing the item count
                    return cur.value
                else: # if there is no key
                    return None
                     
                    
    def get(self, key):
        """
        Retrieve the value stored with the given key.
        Returns None if the key is not found.
        Implement this.
        """
        # Your code here
        # getting the key
        index = self.hash_index(key)
        # returning the value associated with that key
        current = self.table[index]
        
        while current != None: # if there is items in the list
            if current.key == key: # if key is there at hte index
                return current.value # returns the value
            current = current.next # 
        return None # if there is no key at the index


    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        # Your code here
        prev_table = self.table #copying prev table content to new one
        self.capacity = new_capacity #setting self capacity to new capacity
        self.table = [None] * new_capacity #allowing self table to multiply with its capacity
        # looping through the entries of the previous table
        for i in range(len(prev_table)):
            # if there is key/value in the table index
            if prev_table[i] is not None:
                cur = prev_table[i] #setting prev table index as cur
                self.put(cur.key, cur.value) # now adding the content in the new resized table
                cur = cur.next # it will allow to advance to new content          
    
            



if __name__ == "__main__":
    ht = HashTable(8)

    ht.put("line_1", "'Twas brillig, and the slithy toves")
    ht.put("line_2", "Did gyre and gimble in the wabe:")
    ht.put("line_3", "All mimsy were the borogoves,")
    ht.put("line_4", "And the mome raths outgrabe.")
    ht.put("line_5", '"Beware the Jabberwock, my son!')
    ht.put("line_6", "The jaws that bite, the claws that catch!")
    ht.put("line_7", "Beware the Jubjub bird, and shun")
    ht.put("line_8", 'The frumious Bandersnatch!"')
    ht.put("line_9", "He took his vorpal sword in hand;")
    ht.put("line_10", "Long time the manxome foe he sought--")
    ht.put("line_11", "So rested he by the Tumtum tree")
    ht.put("line_12", "And stood awhile in thought.")

    print("")

    # Test storing beyond capacity
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    # Test resizing
    old_capacity = ht.get_num_slots()
    ht.resize(ht.capacity * 2)
    new_capacity = ht.get_num_slots()

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    print("")
