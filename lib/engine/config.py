from lib.engine.source import Source


class DataConfig:
    def __init__(
        self,
        type: str,
        level: int,
        path: str
    ):
        self._type = type
        self._level = level
        self._path = path

    def type(self) -> str:
        return self._type

    def level(self) -> int:
        return self._level

    def path(self) -> str:
        return self._path


class Config:
    def __init__(
        self,
        name: str,
        data: DataConfig,
        sources: list[Source]
    ):
        self._name = name
        self._data = data
        self._sources = sources

    def name(self) -> str:
        return self._name

    def data(self) -> DataConfig:
        return self._data

    def sources(self) -> list[Source]:
        return self._sources

    def __str__(self) -> str:
        result = f"Config: {self._name}\n"

        result += f" Data: {self._data.type()} {self._data.level()} {self._data.path()}\n"

        for source in self._sources:
            result += f" {source}\n"

        return result
