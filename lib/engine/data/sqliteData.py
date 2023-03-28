from datetime import datetime
import sqlite3

from lib.engine.data.data import Data
from lib.engine.source import Source


class SqliteData(Data):
    def __init__(
        self,
        path: str
    ):
        self._path = path
        self._connection = sqlite3.connect(self._path)
        self._cursor = self._connection.cursor()

    def __del__(self):
        self._connection.close()

    def cursor(self) -> sqlite3.Cursor:
        return self._cursor

    def save(self, source: Source, result: bool):
        cursor = self.cursor()

        query = """
                INSERT INTO logs (date, name, source, result)
                VALUES ("{0}", "{1}", "{2}", {3});
                """.format(
            datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            source.name(),
            source.source(),
            1 if result else 0
        )

        try:
            cursor.execute(query)
            self._connection.commit()
        except sqlite3.OperationalError:
            self._migrate()
            cursor.execute(query)
            self._connection.commit()

    def _migrate(self):
        query = """
            CREATE TABLE IF NOT EXISTS logs (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                date TEXT NOT NULL,
                name TEXT NOT NULL,
                source TEXT NOT NULL,
                result INTEGER NOT NULL
            );
            """

        cursor = self.cursor()
        cursor.execute(query)
        self._connection.commit()
