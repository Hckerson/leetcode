class MyHashSet:

    def __init__(self, count=1000):
        self.count = count
        self.buckets = [[] for _ in range(count)]
        pass

    def hash_function(self, key):
        return key % self.count

    def get_bucket(self, key):
        hash = self.hash_function(key)
        bucket = self.buckets[hash]
        return bucket

    def add(self, key: int) -> None:
        bucket = self.get_bucket(key)
        bucket.append(key) if key not in bucket else None

    def remove(self, key: int) -> None:
        bucket = self.get_bucket(key)
        bucket.remove(key) if key in bucket else None

    def contains(self, key: int) -> bool:
        bucket = self.get_bucket(key)
        return key in bucket
