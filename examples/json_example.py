from flask import Flask
from flask_voluptuous import expect, Schema, Required, Coerce
from flask_json import as_json, FlaskJSON

app = Flask(__name__)
json = FlaskJSON(app)


@app.route('/')
@as_json
@expect(Schema({Required('name'): str}), 'args')
def index(args):
    return {'name': args['name']}

@app.route('/post', methods=['POST'])
@as_json
@expect(Schema({
    Required('name'): str,
    Required('per_page', default=10): Coerce(int),
    Required('page', default=1): Coerce(int),
}), 'args')
@expect(Schema({
    Required('min', default=0): Coerce(int),
    Required('max'): Coerce(int)
}), 'json')
def post_url(args, json):
    l = range(json['min'], json['max'])
    ret = {
        'data': l,
        'meta': args
    }
    return ret

if __name__ == '__main__':
    app.run(debug=True)

'''
$ http POST http://127.0.0.1:5000/post?"page=20&name=ludo" max=10
HTTP/1.0 200 OK
Content-Length: 191
Content-Type: application/json
Date: Mon, 02 Oct 2017 19:22:49 GMT
Server: Werkzeug/0.12.2 Python/3.6.1

{
    "data": [
        0,
        1,
        2,
        3,
        4,
        5,
        6,
        7,
        8,
        9
    ],
    "meta": {
        "name": "ludo",
        "page": 20,
        "per_page": 10
    },
    "status": 200
}
'''
