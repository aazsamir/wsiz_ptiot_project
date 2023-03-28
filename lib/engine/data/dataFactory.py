from lib.engine.config import DataConfig
from lib.engine.data.fileData import FileData
from lib.engine.data.data import Data


class DataFactory:
    def make(
        self,
        data: DataConfig
    ) -> Data:
        if data.type() == 'file':
            return FileData(data.path())

        raise Exception('Unknown data type: ' + data.type())
