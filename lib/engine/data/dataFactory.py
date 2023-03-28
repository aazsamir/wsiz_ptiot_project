from lib.engine.config import DataConfig, DataType
from lib.engine.data.fileData import FileData
from lib.engine.data.sqliteData import SqliteData
from lib.engine.data.stdoutData import StdoutData
from lib.engine.data.data import Data


class DataFactory:
    def make(
        self,
        data: DataConfig
    ) -> Data:
        if data.type() == DataType.FILE:
            return FileData(data.path())

        if data.type() == DataType.SQLITE:
            return SqliteData(data.path())

        if data.type() == DataType.STDOUT:
            return StdoutData()

        raise Exception('Not implemented data type: ' + data.type().value)
