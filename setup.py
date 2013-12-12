import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, 'README.txt')) as f:
    README = f.read()
with open(os.path.join(here, 'CHANGES.txt')) as f:
    CHANGES = f.read()

requires = [
    'pyramid==1.5a3',
    'pyramid_chameleon',
    'pyramid_debugtoolbar',
    'pyramid_mako',
    'pyramid_tm',
    'SQLAlchemy',
    'transaction',
    'zope.sqlalchemy',
    'waitress',
    'webhelpers',
    'behave',
    ]

setup(name='pyramid_behave',
      version='0.0',
      description='pyramid_behave',
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
      test_suite='pyramid_behave',
      install_requires=requires,
      entry_points="""\
      [paste.app_factory]
      main = pyramid_behave:main
      [console_scripts]
      initialize_pyramid_behave_db = pyramid_behave.scripts.initializedb:main
      """,
      )
