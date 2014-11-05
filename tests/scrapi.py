__author__ = 'Marvin Laske'

import unittest
from scrapyd_api.scrapi import ScrapydApi
from time import sleep


class ScrapydApiTests(unittest.TestCase):
    def setUp(self):
        #waiting for scrapyd to start up
        #TODO: find a more reliable solution
        sleep(5)

    def initialize_api(self):
        return ScrapydApi("http://127.0.0.1:6800/")

    def test_if_clean_install(self):
        api = self.initialize_api()
        projects = api.list_projects()

        assert isinstance(projects, list)
        self.assertEqual(len(projects), 0)

    def test_add_version(self):
        expected_name = "myProject"
        expected_version = "0.1a"

        api = self.initialize_api()
        spiders = api.add_version(expected_name, expected_version, "TODO")
        self.assertEqual(spiders, 2)

        projects = api.list_projects()
        self.assertEqual(len(projects), 1)
        self.assertEqual(projects[0], expected_name)

        versions = api.list_versions(expected_name)
        self.assertEqual(len(versions), 1)
        self.assertEqual(versions[0], expected_version)

        #delete
        api.del_version(expected_name, expected_version)

        versions = api.list_versions(expected_name)
        self.assertEqual(len(versions), 0)