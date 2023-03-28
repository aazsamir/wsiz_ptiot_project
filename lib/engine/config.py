from lib.engine import source

class Config:
    def __init__(
        self,
        name: str,
        sources: list[source.Source]
    ):
        self._name = name
        self._sources = sources

    def name(self) -> str:
        return self._name

    def sources(self) -> list[source.Source]:
        return self._sources

    def __str__(self) -> str:
        result = f"Config: {self._name}\n"
        for source in self._sources:
            result += f" {source}\n"

        return result