__author__ = 'Marvin Laske'
__version__ = "0.1"

from distutils.core import setup
from setuptools import find_packages

setup(
    name='scrapyd_panel',
    version=__version__,
    packages=find_packages(),
    url='https://github.com/MarvinLaske/scrapyd-panel',
    license='MIT License',
    author=__author__,
    description='A lightweight web interface for managing scrapy cralwers deployed with scrapyd',
    requires=["cherrypy", "requests"]
)
