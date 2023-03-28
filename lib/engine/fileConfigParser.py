import json

from lib.engine.config import Config
from lib.engine.source import Source, Method, Type
from lib.engine.config import DataConfig


class FileConfigParser:
    def __init__(
            self,
            file: str
    ):
        self._file = file

    def parse(self) -> Config:
        with open(self._file, 'r') as file:
            config_dict = json.load(file)

        data = DataConfig(
            type=config_dict['data']['type'],
            level=config_dict['data']['level'],
            path=config_dict['data']['path'])

        sources = []
        for source_dict in config_dict['sources']:
            method = Method[source_dict['method'].upper(
            )] if 'method' in source_dict else None

            sources.append(Source(
                name=source_dict['name'],
                source=source_dict['source'],
                type=Type[source_dict['type'].upper()],
                method=method,
                regex=source_dict['regex'] if 'regex' in source_dict else None,
            ))

        return Config(
            name=config_dict['name'],
            data=data,
            sources=sources)
