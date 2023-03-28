from lib.engine.source import Source


class Data:
    def save(self, source: Source, result: bool):
        raise NotImplementedError
