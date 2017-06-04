import os
import json
from flask import (
    Flask,
    render_template,
    request,
    redirect,
    url_for,
    current_app
)
from cache import MyCache
app = Flask(__name__)
app.config['SECRET_KEY'] = 'jknasjknaejjajnasaskjnsa'
cache = MyCache()
app.config['CACHE'] = cache


@app.route('/')
def index():
    data_file_path = os.path.abspath('student_data.json')
    data = dict()
    cache = current_app.config.get('CACHE')
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


@app.route('/add_new_record', methods=['POST'])
def insert_new_record():
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='localhost', port=3000, debug=True)
