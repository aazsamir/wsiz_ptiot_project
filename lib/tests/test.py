import unittest
import os

from lib.engine.fileConfigParser import FileConfigParser
from lib.engine.config import DataType
from lib.engine.source import Type, Method
from lib.engine.service import Service


class Test(unittest.TestCase):
    def test_file_config(self):
        path = self._path("/mocks/test_file_config.json")
        config = FileConfigParser(path).parse()
        self.assertTrue(config.name() == "Test")
        self.assertTrue(config.data().level() == 0)
        self.assertTrue(config.data().type() == DataType.STDOUT)
        self.assertTrue(config.data().path() == "./data/test.txt")

        source = config.sources()[0]
        self.assertTrue(source.name() == "Source1")
        self.assertTrue(source.source() == "192.168.0.1/status")
        self.assertTrue(source.type() == Type.CURL)
        self.assertTrue(source.method() == Method.GET)

        self.assertTrue(len(config.sources()) == 2)

    def test_ping(self):
        path = self._path("/mocks/test_ping_config.json")
        test_file_output = self._path("/mocks/test_ping_output.txt")
        # clear test file
        open(test_file_output, "w").close()
        service = Service(path, False)
        service.run()

        # get file content
        with open(test_file_output, "r") as f:
            content = f.read()

        self.assertTrue(content.find("Localhost True") != -1)

        # clear test file
        open(test_file_output, "w").close()

    def _path(self, path):
        return os.path.dirname(os.path.abspath(__file__)) + path
