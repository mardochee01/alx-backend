#!/usr/bin/python3
"""LFUCache module
"""


from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """LFUCache class
    """
    def __init__(self):
        """constructor"""
        super().__init__()
        self.__key = []
        self.__count = {}

    def put(self, key, item):
        """put item into cache_data with LFU algorithm
        """
        if not key or not item:
            return
        if len(self.cache_data) == self.MAX_ITEMS and key not in self.__key:
            self.discard()
        if key not in self.cache_data:
            self.__count[key] = 1
        else:
            self.__count[key] += 1
            self.__key.remove(key)
        self.__key.append(key)
        self.cache_data[key] = item

    def get(self, key):
        """get value of cache_data dictionary
        """
        if not key or key not in self.cache_data:
            return None
        self.__count[key] += 1
        self.__key.remove(key)
        self.__key.append(key)
        return self.cache_data[key]

    def discard(self):
        """discard item and print
        """
        time = min(self.__count.values())
        keys = [k for k, v in self.__count.items() if v == time]
        low = 0
        while self.__key[low] not in keys:
            low += 1
        discard = self.__key.pop(low)
        del self.cache_data[discard]
        del self.__count[discard]
        print('DISCARD: {}'.format(discard))
