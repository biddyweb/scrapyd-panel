__author__ = 'Marvin Laske'

import unittest
from scrapyd_api.scrapi import ScrapydApi
from time import sleep


class ScrapydApiTests(unittest.TestCase):
    def setUp(self):
        #waiting for scrapyd to start up
        #TODO: find a more reliable solution
        sleep(5)

    def test_if_clean_install(self):
        api = ScrapydApi("http://127.0.0.1:6800/")
        projects = api.list_projects()
        print projects