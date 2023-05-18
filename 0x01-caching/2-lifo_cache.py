#!/usr/bin/python3
""" LIFO Caching
"""


from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """ aninherits caching system
    """
    def __init__(self):
        """inistate"""
        super().__init__()
        self.__key = []

    def put(self, key, item):
        """ put cahce
        Args:
            key ([type]): key of dictionary
            item ([type]): item to insert in dictionary
        """
        if len(self.cache_data) == self.MAX_ITEMS and key not in self.__key:
            discard = self.__key.pop()
            del self.cache_data[discard]
            print('DISCARD: {}'.format(discard))
        if key and item:
            self.__key.append(key)
            self.cache_data[key] = item

    def get(self, key):
        """ get value
        """
        if not key or key not in self.cache_data:
            return None
        return self.cache_data[key]
