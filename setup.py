import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.md')).read()
CHANGES = open(os.path.join(here, 'CHANGES.txt')).read()

requires = [
    'pyramid',
    'SQLAlchemy',
    'transaction',
    'pyramid_tm',
    'pyramid_debugtoolbar',
    'zope.sqlalchemy',
    'waitress',
    'WebTest',
    'logbook',
    'pyyaml',
    'WTForms',
    'pyyaml',
    'zope.dottedname',
    'colander',
    'psycopg2',
    'GeoAlchemy'
]

setup(name='cyclee_server',
      version='0.0',
      description='cyclee_server',
      long_description=README + '\n\n' + CHANGES,
      classifiers=[
          "Programming Language :: Python",
          "Framework :: Pyramid",
          "Topic :: Internet :: WWW/HTTP",
          "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
      ],
      author='',
      author_email='',
      url='',
      keywords='web wsgi bfg pylons pyramid',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      test_suite='cyclee_server',
      install_requires=requires,
      entry_points="""\
      [paste.app_factory]
      main = cyclee_server:main
      [console_scripts]
      load-fixtures = cyclee_server.scripts:fixture_command
      clear-db = cyclee_server.scripts:clear_command
      """,
      )
