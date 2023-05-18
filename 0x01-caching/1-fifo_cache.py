#!/usr/bin/python3
""" FIFO Caching
"""


from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """ parameter:
    key, item
    """

    def __init__(self):
        """ initial """
        super().__init__()
        self.__key = []

    def put(self, key, item):
        """ must assign"""
        if len(self.cache_data) == self.MAX_ITEMS and key not in self.__key:
            discard = self.__key.pop(0)
            del self.cache_data[discard]
            print('DISCARD: {}'.format(discard))
        if key and item:
            self.__key.append(key)
            self.cache_data[key] = item

    def get(self, key):
        """ get value"""
        if not key or key not in self.cache_data:
            return None
        return self.cache_data[key]
