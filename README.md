# flask_voluptuous
A simple flask extension for data validation with Voluptuous

## Usage

```python
from flask import Flask
from flask_voluptuous import expect, Schema, Required

app = Flask(__name__)

@app.route('/')
@expect(Schema(
  {
    Required('name'): str
  }
  ), 'args')
def index(args):
    return 'name: {}'.format(args['name'])

if __name__ == '__main__':
    app.run(debug=True)
```
