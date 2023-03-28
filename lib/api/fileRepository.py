from datetime import datetime

from lib.api.repository import Repository
from lib.api.result import Result


class FileRepository(Repository):
    def __init__(self, path):
        self._path = path

    def getAll(self) -> list[Result]:
        lines = open(self._path, 'r').readlines()

        results = [self.makeResultFromLine(line) for line in lines]

        return results

    def getByName(self, name: str) -> list[Result]:
        results = []

        with open(self._path, 'r') as file:
            for line in file:
                if name in line:
                    results.append(self.makeResultFromLine(line))

        return results

    def makeResultFromLine(self, line: str) -> Result:
        date = line[:19]
        date = datetime.strptime(date, '%Y-%m-%d %H:%M:%S')
        line = line.strip()
        result = line.endswith('True')
        name = line[20:]
        # delete last word
        name = name[:name.rfind(' ')]

        return Result(date, result, name)

    def path(self) -> str:
        return self._path
