from datetime import datetime
import sqlite3

from lib.api.repository import Repository
from lib.api.result import Result


class SqliteRepository(Repository):
    def __init__(self, path):
        self._connection = sqlite3.connect(path)
        self._cursor = self._connection.cursor()

    def getAll(self) -> list[Result]:
        query = """
            SELECT
                name,
                date,
                result
            FROM
                logs
        """

        res = self._cursor.execute(query)

        return [self.makeResult(row) for row in res]

    def getByName(self, name: str) -> list[Result]:
        query = """
            SELECT
                name,
                date,
                result
            FROM
                logs
            WHERE
                name = "{}"
        """.format(name)

        res = self._cursor.execute(query)

        return [self.makeResult(row) for row in res]

    def makeResult(self, row: tuple) -> Result:
        date = datetime.strptime(row[1], "%Y-%m-%d %H:%M:%S")
        name = row[0]
        result = row[2] == True if row[2] == 1 else False

        return Result(date, result, name)
