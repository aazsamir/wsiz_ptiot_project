from lib.engine import fileConfigParser as fileConfigParser
from lib.engine import runner

parser = fileConfigParser.FileConfigParser(file="config.json")

cfg = parser.parse()

runner = runner.Runner(cfg, True)
runner.run()
