__author__ = 'Marvin Laske'

import unittest
import os
import thread
from scrapyd_api.scrapi import ScrapydApi


class ScrapydApiTests(unittest.TestCase):
    def start_scrapyd(self):
        os.system("scrapyd")

    def setUp(self):
        os.system("sudo pip install scrapyd")
        self.scrapyd_thread = thread.start_new_thread(self.start_scrapyd, [])

    def tearDown(self):
        self.scrapyd_process.terminate()
        os.system("sudo pip uninstall scrapyd -y")

    def test_if_clean_install(self):
        api = ScrapydApi("http://localhost:6800/")
        projects = api.list_projects()
        print projects