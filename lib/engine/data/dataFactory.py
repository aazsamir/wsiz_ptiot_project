from lib.engine.config import DataConfig
from lib.engine.data.fileData import FileData
from lib.engine.data.sqliteData import SqliteData
from lib.engine.data.stdoutData import StdoutData
from lib.engine.data.data import Data


class DataFactory:
    def make(
        self,
        data: DataConfig
    ) -> Data:
        if data.type() == 'file':
            return FileData(data.path())
        
        if data.type() == 'sqlite':
            return SqliteData(data.path())
        
        if data.type() == 'stdout':
            return StdoutData()

        raise Exception('Unknown data type: ' + data.type())
