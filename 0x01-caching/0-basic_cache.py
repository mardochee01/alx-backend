#!/usr/bin/env python3
""" BasicCache Class
"""


from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """ inherits from BaseCaching
    """

    def put(self, key, item):
        """ Must assign to the dictionary
        - self.cache_data: item and key
        - do anything If key or item is None
        """
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """ Must return the value
        - self.cache_data linked to key
        - retiurn NoneIf key is None or inexistant
        """
        if key not in self.cache_data or not key:
            return None
        return self.cache_data[key]
