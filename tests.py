import pytest
from flask import Flask
from flask_voluptuous import expect, Schema, Required
import json
from werkzeug.exceptions import NotAcceptable

@pytest.fixture
def app():
    app = Flask(__name__)
    app.debug = True
    app.testing = True
    ctx = app.app_context()
    ctx.push()
    yield app
    ctx.pop()

def test_bad_location(app):
    bad_location = 'bad_location'
    with pytest.raises(AttributeError) as excinfo:
        @expect(Schema({}), bad_location)
        def func(bad_location):
            pass
    assert '{} location not admitted'.format(bad_location) == str(excinfo.value)


def test_expected_decorator_form_location(app):
    schema = Schema({
        Required('text'): str,
        Required('per_page', default=5): int
    })

    @expect(schema, 'form')
    def func(form):
        assert form['text'] == 'testo'
        assert form['per_page'] == 5

    with app.test_request_context('/',method='POST', data={'text': 'testo'}):
        ret = func()

def test_expected_args_decorator(app):

    schema = Schema({
        Required('text'): str,
        Required('per_page', default=5): int
    })

    @expect(schema, 'args')
    def func(args):
        assert args['text'] == 'testo'
        assert args['per_page'] == 5

    with app.test_request_context('/?text=testo'):
        ret = func()

def test_expect_json_location(app):
    schema = Schema({
        Required('text'): str,
        Required('per_page', default=5): int
    })

    @expect(schema, 'json')
    def func(json):
        assert json['text'] == 'testo'
        assert json['per_page'] == 5

    with app.test_request_context(data=json.dumps({'text': 'testo'}), headers={'content-type': 'application/json'}):
        ret = func()

def test_expect_bad_request(app):
    schema = Schema({
        Required('text'): str,
        Required('per_page'): int
    })

    @expect(schema, 'json')
    def func(json):
        assert json['text'] == 'testo'
        assert json['per_page'] == 5

    with app.test_request_context(data=json.dumps({'text': 'testo'}), headers={'content-type': 'application/json'}):
        with pytest.raises(NotAcceptable) as excinfo:
            ret = func()
        assert '406 Not Acceptable: required key not provided @ data[\'per_page\']' == str(excinfo.value)
