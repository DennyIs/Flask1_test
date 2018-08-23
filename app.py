import os

from flask import Flask


app = Flask(__name__)


@app.route('/hello/<user>')
def hello_world(user):
    return 'Hello user: ' + user


@app.route('/hello/<int:num1>/<int:num2>')
def konk_nums(num1, num2):
    return 'Sum = {}'.format(num1 + num2)


@app.route('/long/<s1>/<s2>/<s3>')
def long_string(s1, s2, s3):
    mylist = [s1, s2, s3]
    return max(mylist, key=len)


@app.route('/<path:filename>')
def show_file(filename):
    if not os.path.exists('./files/' + filename):
        return 'No'
    else:
        return 'Yes'


if __name__ == '__main__':
    app.run()
