from datetime import datetime

from lib.engine.data.data import Data
from lib.engine.source import Source


class FileData(Data):
    def __init__(self, path: str):
        self._path = path

    def save(self, source: Source, result: bool):
        with open(self._path, 'a') as f:
            line = ""
            line += datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            line += " "
            line += source.name()
            line += " "
            line += str(result)
            line += "\n"
            f.write(line)
