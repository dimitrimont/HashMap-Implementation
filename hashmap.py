


class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class HashMap:
    def __init__(self, size):
        self.size = size
        self.table = [None] * self.size
        self.keys = []


    def _hash(self, key):
        if isinstance(key, str):
            key_hash = hash(key)
        else:
            key_hash = key
        return abs(key_hash) % self.size


    def __setitem__(self, key, value):
        index = self._hash(key)

        if self.table[index] is None:
            self.table[index] = Node(key, value)
            if key not in self.keys:
                self.keys.append(key)
            return

        current = self.table[index]

        while current:
            if current.key == key:
                current.value = value
                return
            if current.next is None:
                break
            current = current.next


        current.next = Node(key, value)
        if key not in self.keys:
            self.keys.append(key)


    def __getitem__(self, key):
        index = self._hash(key)
        current = self.table[index]

        while current:
            if current.key == key:
                return current.value
            current = current.next

        raise KeyError(f"{key} not in hashmap")

    def __delitem__(self, key):
        index = self._hash(key)
        current = self.table[index]

        if current is None:
            raise KeyError(f"{key} not in hashmap")

        if current.key == key:
            self.table[index] = current.next
            self.keys.remove(key)
            return

        while current.next:
            if current.next.key == key:
                current.next = current.next.next
                self.keys.remove(key)
                return
        current = current.next

        raise KeyError(f"{key} not in hashmap")

    def __contains__(self, key):
        index = self._hash(key)
        current = self.table[index]

        while current:
            if current.key == key:
                return True
            current = current.next
        return False

    def get_keys(self):
        return self.keys.copy()

        
#=====================================================================


def test_hashmap():
    hm = HashMap(size=5)
    

    print("Inserting")
    hm["apple"] = 3
    hm["banana"] = 2
    hm["orange"] = 5
    
    
    print(f"apple: {hm['apple']}")  
    print(f"banana: {hm['banana']}")
    
    
    print(f"apple in hashmap? {'apple' in hm}")  
    print(f"grape in hashmap? {'grape' in hm}")  
    

    
    print("\nUpdate")
    hm["apple"] = 4
    print(f"Updated apple: {hm['apple']}")  
    
    
    print(f"\nAll keys: {hm.get_keys()}")
    
    
    print("\nDeleting")
    del hm["banana"]
    
    
    
    print("\nCollisions")
    hm["mango"] = 6
    hm["peach"] = 7
    print(f"mango: {hm['mango']}")
    print(f"peach: {hm['peach']}")
    
    
    print("\nErrors")
    try:
        print(hm["testerror"])
    except KeyError as error:
        print(f"Error: {error}")
        

if __name__ == "__main__":
    test_hashmap()

        
        
        
        


