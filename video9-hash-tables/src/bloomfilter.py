import pprint

class BloomFilter:
    def __init__(self):
        # initialize an empty table
        self.bitfield = [False]*100
        print(self.bitfield)

    def get_index(self, key):
        print(key, hash(key)%16)
        return hash(key) % len(self.bitfield)

    def insert(self, key):
        for i in range(4):
            index = self.get_index(key + str(i))
            print("insert", key, index)
            self.bitfield[index] = True

    def lookup(self, search_key):
        for i in range(4):
            index = self.get_index(search_key  + str(i))
            if not self.bitfield[index]:
                return False
        return True

    def __str__(self):
        return pprint.pformat(self.buckets)

if __name__ == "__main__":
    bf = BloomFilter()
    bf.insert("Mark")
    print(bf.lookup("Mark"))
    print(bf.lookup("Brad"))
          
