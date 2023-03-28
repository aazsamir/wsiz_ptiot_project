from lib.engine import fileConfigParser as fileConfigParser

parser = fileConfigParser.FileConfigParser(file="config.json")

cfg = parser.parse()

print(cfg)