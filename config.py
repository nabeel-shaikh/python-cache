import json
from cache import MyCache


def load_cache():
    """Initialize cache from the data file"""
    cache = MyCache()
    with open('student_data.json') as data_file:
        data = json.load(data_file)
        i = 0
        for key in data.keys():
            if key in cache:
                continue
            else:
                value = data.get(key)
                cache.update(key, value)
            print("#%s iterations, #%s cached entries" % (i + 1, cache.size))
            i += 1
    return cache
