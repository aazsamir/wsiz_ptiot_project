from lib.engine.source import Source


class Resolver:
    def resolve(
            self,
            source: Source
    ) -> bool:
        raise NotImplementedError
