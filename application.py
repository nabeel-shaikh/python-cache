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
from config import set_app_config
app = Flask(__name__)
app.config['SECRET_KEY'] = 'jknasjknaejjajnasaskjnsa'
set_app_config(app)


@app.route('/')
def index():
    data_file_path = os.path.abspath('student_data.json')
    cache = current_app.config.get('CACHE')
    return render_template(
        'homepage.html',
        data_file_path=data_file_path,
        cache=cache
    )


@app.route('/add_new_record', methods=['POST'])
def insert_new_record():
    key = str(request.form.get('student'))
    value = dict()
    value['maths'] = int(request.form.get('maths'))
    value['science'] = int(request.form.get('science'))
    value['english'] = int(request.form.get('english'))
    value['total'] = value['maths'] + value['science'] + value['english']
    cache = current_app.config.get('CACHE')
    cache.update(key, value)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='localhost', port=3000, debug=True)
