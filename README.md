python-cache
==============

Demonstration of cache implementation in Python  

How to run
------------------

It is always a good idea using a virtual environment to run your
application. That will avoid interference from your hosting
environment. That can be done using [virtualenv](https://virtualenv.pypa.io/en/stable/):

    $ virtualenv venv
    $ source venv/bin/activate
    $ pip install -r requirements.txt
    $ python application.py

Fire up your browser and type in localhost:3000.

The data file containing test student records is `student_data.json`.
```
    1. Click on load cache. This will load all 20 elements from the file.
    2. On successfull load, you'll note that the access count is 1 for all entries.
    3. Refresh the page and again click on load cache. The access count get incremented by 1.
    4. To add a new entry, click on the '+' button.
    5. Note that the cache size is restricted to 20. So for adding a new key, one will have to give way.
       The logic here is that the least accessed key from the cache will be replaced by the new one.
       We'll test this later. Hang on!
    6. A modal form appears. Fill in the details and click on submit.
    7. Because all keys have access count equal, one will be randomly selected and replaced.
    8. You'll see the replaced key name in the Flash message that just appeared.
    9. The new key added to the cache has an access count of 1 which means this should get replaced if we add
       another record.
   10. Repeat step 6 to find out. It works!
   11. If you try to add a new key with an already existing name, it's value would get updated and no record would be deleted.
   12. The `Shut down cache` button would save the current cached data back to the file i.e. `student_data.json`.
```

> :)
