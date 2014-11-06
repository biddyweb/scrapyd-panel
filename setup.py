__author__ = 'Marvin Laske'
__version__ = "0.1"
__name__ = "scrapyd_panel"

from distutils.core import setup
from setuptools import find_packages

setup(
    name=__name__,
    version=__version__,
    packages=find_packages(),
    url='https://github.com/MarvinLaske/scrapyd-panel',
    license='MIT License',
    author=__author__,
    description='A lightweight web interface for managing scrapy cralwers deployed with scrapyd',
    requires=["cherrypy", "requests"]
)
