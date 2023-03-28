import json

from lib.engine import config
from lib.engine import source
from lib.engine.config import DataConfig


class FileConfigParser:
    def __init__(
            self,
            file: str
    ):
        self._file = file

    def parse(self) -> config.Config:
        with open(self._file, 'r') as file:
            config_dict = json.load(file)

        data = DataConfig(
            type=config_dict['data']['type'],
            level=config_dict['data']['level'],
            path=config_dict['data']['path'])

        sources = []
        for source_dict in config_dict['sources']:
            method = source.Method[source_dict['method'].upper(
            )] if 'method' in source_dict else None

            sources.append(source.Source(
                name=source_dict['name'],
                source=source_dict['source'],
                type=source.Type[source_dict['type'].upper()],
                method=method,
                regex=source_dict['regex'] if 'regex' in source_dict else None,
            ))

        return config.Config(
            name=config_dict['name'],
            data=data,
            sources=sources)
