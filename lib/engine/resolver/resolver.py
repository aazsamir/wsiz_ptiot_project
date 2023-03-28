from lib.engine import source


class Resolver:
    def resolve(
            self,
            source: source.Source
    ) -> bool:
        raise NotImplementedError
