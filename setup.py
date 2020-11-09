from distutils.core import setup

setup(
  name = 'flask_voluptuous',
  py_modules = ['flask_voluptuous'], # this must be the same as the name above
  description = 'A simple flask extension for data validation with Voluptuous',
  author = 'Ludovico O. Russo',
  author_email = 'ludus.russo@gmail.com',
  url = 'https://github.com/ludusrusso/flask_voluptuous/tree/develop', # use the URL to the github repo
  keywords = ['voluptous', 'flask', 'validation'], # arbitrary keywords
  classifiers = [],
  install_requires=[
        'Flask', 'Voluptuous'
    ],
)
