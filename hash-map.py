class MyHashMap:

    def __init__(self, count=1009):
        self.count = count
        self.buckets = [[] for _ in range(count)]

    def hash_function(self, key):
        return key % self.count

    def put(self, key: int, value: int) -> None:
        hash = self.hash_function(key)
        bucket = self.buckets[hash]

        for idx, (k, v) in enumerate(bucket):
            if k == key:
                bucket[idx] = (key, value)
                return
        bucket.append((key, value))

    def get(self, key: int) -> int:
        hash = self.hash_function(key)
        bucket = self.buckets[hash]

        for (k, v) in bucket:
            if (k == key):
                return v

        return -1
            

    def remove(self, key: int) -> None:
        hash = self.hash_function(key)
        bucket = self.buckets[hash]

        for idx, (k, v) in enumerate(bucket):
            if (k == key):
                del bucket[idx]
                return

