__author__ = 'Marvin Laske'

import unittest
from scrapyd_api.scrapi import ScrapydApi


class ScrapydApiTests(unittest.TestCase):
    def test_if_clean_install(self):
        api = ScrapydApi("http://localhost:6800/")
        projects = api.list_projects()
        print projects