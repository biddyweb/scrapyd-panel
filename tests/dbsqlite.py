__author__ = 'Marvin Laske'

import unittest
import os
import uuid
from database.dbsqlite import DatabaseSqlite


class DatabaseSqliteTests(unittest.TestCase):
    def setUp(self):
        self.temp_file_name = str(uuid.uuid4())
        self.db = DatabaseSqlite(self.temp_file_name)
        self.db.create_schema()

    def tearDown(self):
        os.remove(self.temp_file_name)

    def test_server_add_single(self):
        expected_name = "test_name"
        expected_url = "test_url"

        server_id = self.db.add_server(expected_name, expected_url)
        self.assertIsNotNone(server_id)

        server = self.db.get_server(server_id)
        self.assertIsNotNone(server)
        self.assertEqual(expected_name, server.name)
        self.assertEqual(expected_url, server.url)

    def test_server_add_multiple(self):
        expected_name1 = "test_name1"
        expected_url1 = "test_url1"

        server_id1 = self.db.add_server(expected_name1, expected_url1)
        self.assertIsNotNone(server_id1)

        expected_name2 = "test_name2"
        expected_url2 = "test_url2"

        server_id2 = self.db.add_server(expected_name2, expected_url2)
        self.assertIsNotNone(server_id2)

        servers = self.db.get_all_servers()
        self.assertIsNotNone(servers)
        self.assertEqual(len(servers), 2)

        self.assertEqual(expected_name1, servers[0].name)
        self.assertEqual(expected_url1, servers[0].url)

        self.assertEqual(expected_name2, servers[1].name)
        self.assertEqual(expected_url2, servers[1].url)