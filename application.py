import os
import json
from flask import (
    Flask,
    render_template,
    session
)
from cache import MyCache
app = Flask(__name__)
app.config['SECRET_KEY'] = 'jknasjknaejjajnasaskjnsa'


@app.route('/')
def index():
    data_file_path = os.path.abspath('student_data.json')
    data = dict()
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
    return render_template(
        'homepage.html',
        data_file_path=data_file_path,
        cache=cache
    )

if __name__ == '__main__':
    app.run(host='localhost', port=3000, debug=True)
