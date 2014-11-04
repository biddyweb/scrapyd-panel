__author__ = 'Marvin Laske'

import sqlite3
import model
from contextlib import closing


class DatabaseSqlite:
    def __init__(self, connection_string):
        self.connection_string = connection_string

    def connect(self):
        """
        connects to the default sqlite file

        :rtype : sqlite3.connection
        :return: an active sqlite connection
        """
        return sqlite3.connect(self.connection_string)

    def create_schema(self):
        """
        creates the default database schema

        """
        with self.connect() as con:
            con.execute('CREATE TABLE "server" ("name" TEXT NOT NULL , "url" TEXT NOT NULL )')

    def get_server(self, server_id):
        """
        gets a server by its id

        :type server_id: int
        :param server_id: servers id
        :rtype: model.Server
        """
        with self.connect() as con:
            with closing(con.cursor()) as curs:
                curs.execute('SELECT "name", "url" FROM "server" WHERE "rowid"=?',
                             [server_id])

                result = curs.fetchone()
                return model.Server(result[0], result[1])

    def add_server(self, name, url):
        """
        adds a server into the db

        :param name: how the server shall be named
        :param url: url under which the server is reachable
        :return: returns the id of the created server
        """
        with self.connect() as con:
            with closing(con.cursor()) as curs:
                curs.execute('INSERT INTO "server" ("name", "url") VALUES (?, ?)',
                             [name, url])
                curs.execute('select last_insert_rowid()')
                result = curs.fetchone()[0]

                con.commit()
                return result

    def get_all_servers(self):
        """
        gets all servers

        :rtype: list
        """
        with self.connect() as con:
            with closing(con.cursor()) as curs:
                curs.execute('SELECT "name", "url" FROM "server"')
                results = []
                for result in curs:
                    results.append(model.Server(result[0], result[1]))

                return results