from lib.engine.config import Config, DataType
from lib.api.fileRepository import FileRepository
from lib.api.sqliteRepository import SqliteRepository
from lib.api.repository import Repository


class RepositoryFactory:
    def make(self, config: Config) -> Repository:
        repository = None

        if config.data().type() == DataType.FILE:
            repository = FileRepository(config.data().path())
        elif config.data().type() == DataType.SQLITE:
            repository = SqliteRepository(config.data().path())

        if repository is None:
            raise Exception("Repository is not defined")

        return repository
