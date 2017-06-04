import os
from flask import (
    Flask,
    render_template,
    request,
    redirect,
    url_for,
    current_app,
    flash
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
    message = 'Record for {0} inserted into cache. Click on Load cache to continue.'.format(str(key))
    flash(message=message, category='success')
    return redirect(url_for('index'))


@app.route('/shut_down')
def shut_down():
    cache = current_app.config.get('CACHE')
    cache.shut_down()
    message = 'Cache turned off successfully. Cached data saved to file.'
    flash(message=message, category='success')
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(host='localhost', port=3000, debug=True)
