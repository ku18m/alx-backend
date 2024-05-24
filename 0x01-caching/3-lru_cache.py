#!/usr/bin/python3
""""""
BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """
    LRUCache class that inherits from BaseCaching.
    Implements a Least Recently Used (LRU) caching algorithm.
    """

    def __init__(self):
        """ Initialize LRUCache """
        self.queue = []
        super().__init__()

    def put(self, key, item):
        """
        Add an item to the cache.
        If the cache is full, remove the least recently used item.
        """
        if key and item:
            if self.cache_data.get(key):
                self.queue.remove(key)
            self.queue.append(key)
            self.cache_data[key] = item
            if len(self.queue) > self.MAX_ITEMS:
                delete = self.queue.pop(0)
                self.cache_data.pop(delete)
                print('DISCARD: {}'.format(delete))

    def get(self, key):
        """
        Retrieve the value associated with the given key.
        If the key exists, move it to the end of the queue
        to mark it as the most recently used.
        """
        if self.cache_data.get(key):
            self.queue.remove(key)
            self.queue.append(key)
        return self.cache_data.get(key)
