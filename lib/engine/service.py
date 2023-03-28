from lib.engine.fileConfigParser import FileConfigParser
from lib.engine.runner import Runner


class Service:
    def __init__(
        self,
        config_path: str,
        verbose: bool = False
    ):
        self._config_path = config_path
        self._config = FileConfigParser(self._config_path).parse()
        self._runner = Runner(self._config, verbose=verbose)

    def run(self):
        self._runner.run()
