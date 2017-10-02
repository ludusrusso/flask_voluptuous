# flask_voluptuous
A simple flask extension for data validation with Voluptuous

## Usage

```python
from flask import Flask
from flask_voluptuous import expect, Schema, Required

app = Flask(__name__)

@app.route('/')
@expect(Schema({
    Required('name'): str
  }), 'args')
def index(args):
    return 'name: {}'.format(args['name'])

if __name__ == '__main__':
    app.run(debug=True)
```

The `/` route requires a `name` param in the request arguments.
This data are accesible throw the `args` arguments passed to the function.

If the data is not submitted, we get an 406 error:
```
$ http http://127.0.0.1:5000/?other=ludusrusso
HTTP/1.0 406 NOT ACCEPTABLE
Content-Length: 160
Content-Type: text/html
Date: Mon, 02 Oct 2017 10:44:33 GMT
Server: Werkzeug/0.12.2 Python/3.6.1

<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">
<title>406 Not Acceptable</title>
<h1>Not Acceptable</h1>
<p>extra keys not allowed @ data['other']</p>
```

```
$ http http://127.0.0.1:5000/?name=ludusrusso
HTTP/1.0 200 OK
Content-Length: 16
Content-Type: text/html; charset=utf-8
Date: Mon, 02 Oct 2017 10:42:18 GMT
Server: Werkzeug/0.12.2 Python/3.6.1

name: ludusrusso
```
