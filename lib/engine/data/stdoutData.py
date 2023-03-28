from datetime import datetime
import sys

from lib.engine.data.data import Data
from lib.engine.source import Source


class StdoutData(Data):
    def save(self, source: Source, result: bool):
        line = ""
        line += datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        line += " "
        line += source.name()
        line += " "
        line += str(result)
        line += "\n"

        sys.stdout.write(line)

