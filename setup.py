from distutils.core import setup
setup(
  name = 'flask_voluptuous',
  packages = ['flask_voluptuous'], # this must be the same as the name above
  version = '0.1',
  description = 'A simple flask extension for data validation with Voluptuous',
  author = 'Ludovico O. Russo',
  author_email = 'ludus.russo@gmail.com',
  url = 'https://github.com/ludusrusso/flask_voluptuous/tree/develop', # use the URL to the github repo
  download_url = 'https://github.com/ludusrusso/flask_voluptuous/tree/develop/archive/0.1.tar.gz', # I'll explain this in a second
  keywords = ['voluptous', 'flask', 'validation'], # arbitrary keywords
  classifiers = [],
  install_requires=[
        'Flask', 'Voluptuous'
    ],
)
