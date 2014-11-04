__author__ = 'Marvin Laske'

import unittest
import os
from scrapyd_api.scrapi import ScrapydApi


class ScrapydApiTests(unittest.TestCase):
    def start_scrapyd(self):
        os.system("scrapyd")

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_if_clean_install(self):
        api = ScrapydApi("http://localhost:6800/")
        projects = api.list_projects()
        print projects