from enum import Enum


class Method(Enum):
    GET = "GET"
    POST = "POST"


class Type(Enum):
    CURL = "CURL"
    PING = "PING"


class Source:
    def __init__(
        self,
        name: str = "",
        source: str = "",
        type: Type = Type.PING,
        method: Method|None = Method.GET,
    ):
        self._name = name
        self._source = source
        self._type = type
        self._method = method

    def name(self) -> str:
        return self._name

    def type(self) -> Type:
        return self._type

    def method(self) -> Method|None:
        return self._method

    def source(self) -> str:
        return self._source
    
    def __str__(self) -> str:
        return f"Source(\n\tname={self.name()},\n\tsource={self.source()},\n\ttype={self.type()},\n\tmethod={self.method()}\n )"
