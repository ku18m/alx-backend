#!/usr/bin/python3
""""""
BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    """
    MRUCache class that inherits from BaseCaching.
    Implements a Most Recently Used (MRU) caching algorithm.
    """

    def __init__(self):
        """
        Initialize MRUCache.
        """
        self.stack = []
        super().__init__()

    def put(self, key, item):
        """
        Add an item to the cache.

        Args:
            key: The key of the item.
            item: The item to be added.
        """
        if key and item:
            if self.cache_data.get(key):
                self.stack.remove(key)
            while len(self.stack) >= self.MAX_ITEMS:
                delete = self.stack.pop()
                self.cache_data.pop(delete)
                print('DISCARD: {}'.format(delete))
            self.stack.append(key)
            self.cache_data[key] = item

    def get(self, key):
        """
        Retrieve an item from the cache.

        Args:
            key: The key of the item to be retrieved.

        Returns:
            The value associated with the given key,
            or None if the key is not found.
        """
        if self.cache_data.get(key):
            self.stack.remove(key)
            self.stack.append(key)
        return self.cache_data.get(key)
