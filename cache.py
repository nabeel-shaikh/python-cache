import datetime
import json
import copy
from collections import OrderedDict


class MyCache:
    """Cache implementation"""

    def __init__(self):
        """Constructor"""
        self.cache = {}
        self.max_cache_size = 20

    def __contains__(self, key):
        """
        Returns True or False depending on whether or not the key is in the
        cache
        """
        return key in self.cache

    def update(self, key, value):
        """
        Update the cache dictionary and optionally remove the least accessed item
        """
        if key not in self.cache and len(self.cache) >= self.max_cache_size:
            self.remove_least_accessed()

        self.cache[key] = value
        self.cache[key]['date_accessed'] = datetime.datetime.now()
        self.cache[key]['access_count'] = 0

    def access_key(self, key):
        """
        Access key from cache
        """
        if key in self.cache:
            self.cache[key]['date_accessed'] = datetime.datetime.now()
            self.cache[key]['access_count'] += 1
            return self.cache[key]['access_count']
        else:
            return 0

    def cache_dict(self):
        """
        Store the items in an ordered dict fashion.
        """
        if len(self.cache) == 0:
            return self.cache
        else:
            return OrderedDict(sorted(self.cache.items(), key=lambda x: x[1]['total'], reverse=True))

    def save_to_file(self):
        """
        Save the cached items to JSON file
        """
        cache_data = self.cache_dict()
        data = copy.deepcopy(cache_data)
        for key, value in data.items():
            value.pop('date_accessed')
            value.pop('access_count')
        with open('test_1.json', 'w') as outfile:
            json.dump(data, outfile)
        return data

    def remove_least_accessed(self):
        """
        Remove the entry that has the least access count
        """
        least_accessed_entry = None
        for key in self.cache:
            if least_accessed_entry is None:
                least_accessed_entry = key
            elif self.cache[key]['access_count'] < self.cache[least_accessed_entry][
                    'access_count']:
                least_accessed_entry = key
        self.cache.pop(least_accessed_entry)

    def shut_down(self):
        """
        Save cache data to file then truncate it.
        """
        self.save_to_file()
        self.cache = dict()

    @property
    def size(self):
        """
        Return the size of the cache
        """
        return len(self.cache)
