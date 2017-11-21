"""
This is a setup.py script generated by py2applet

Usage:
    python setup.py py2app
"""

from setuptools import setup

APP = ['plotter2.py']
DATA_FILES = []
OPTIONS = {'packages':['backports', "matplotlib"],
           'iconfile':'ui/icons/appicon.png.icns',
           "includes":["sip", 'backports.functools_lru_cache'],
           'excludes':['pexpect']}


setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)

#Execute also cp /usr/local/lib/python2.7/site-packages/backports/functools_lru_cache.py ./dist/plotter2.app/Contents/Resources/lib/python2.7/backports/