'''
Design a HashMap without using any built-in hash table libraries.

Implement the MyHashMap class:

    MyHashMap() initializes the object with an empty map.
    void put(int key, int value) inserts a (key, value) pair into the HashMap. If the key already exists in the map, update the corresponding value.
    int get(int key) returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key.
    void remove(key) removes the key and its corresponding value if the map contains the mapping for the key.
'''

class MyHashMap:

    def __init__(self):
        self.map = {}

    def put(self, key: int, value: int) -> None:
        self.map[key] = value

    def get(self, key: int) -> int:
        if self.map.get(key)==None:
            return -1
        else:
            return self.map.get(key)

    def remove(self, key: int) -> None:
        self.map.pop(key, None)

if __name__ == "__main__":
    myHashMap = MyHashMap()
    myHashMap.put(1, 1)  # The map is now [[1,1]]
    myHashMap.put(2, 2)  # The map is now [[1,1],[2,2]]
    print(myHashMap.get(1))  # return 1
    print(myHashMap.get(3))  # return -1 (not found)
    myHashMap.put(2, 1)  # update the existing value
    print(myHashMap.get(2))  # return 1 (updated)
    myHashMap.remove(2)  # remove the mapping for 2
    print(myHashMap.get(2))  # return -1 (not found)