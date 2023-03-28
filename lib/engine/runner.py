from lib.engine import config
from lib.engine.resolver import resolverFactory
from lib.engine.data.dataFactory import DataFactory


class Runner:
    def __init__(
            self,
            config: config.Config,
            verbose: bool = False
    ):
        self._config = config
        self._verbose = verbose
        self._resolverFactory = resolverFactory.ResolverFactory()
        self._data = DataFactory().make(config.data())

    def run(self):
        if self.verbose():
            print("Running with config: {}".format(self._config))

        for source in self._config.sources():
            if self.verbose():
                print("Running source: {}".format(source))

            resolver = self._resolverFactory.make(source)
            result = resolver.resolve(source=source)

            if self.verbose():
                print("Result: {}".format(result))

            if self.shouldSave(result):
                if self.verbose():
                    print("Saving source: {}".format(source))
                self._data.save(source, result)

    def shouldSave(self, result: bool) -> bool:
        # on level 0, we always save
        if self._config.data().level() == 0:
            return True

        # on level 1, we save if the result is False
        if self._config.data().level() == 1:
            return not result

        # on level 2, we save if the result is True
        if self._config.data().level() == 2:
            return result

        raise Exception("Invalid data level: {}".format(
            self._config.data().level()))

    def verbose(self) -> bool:
        return self._verbose
