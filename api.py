#!/usr/bin/env python

import sys

from lib.engine.fileConfigParser import FileConfigParser
from lib.api.repositoryFactory import RepositoryFactory


def parseArgs(args: list):
    args = args[1:]
    name = None

    for arg in args:
        if arg.startswith("--name="):
            name = arg.split("=")[1]

        if arg.startswith("-n"):
            name = arg.split("=")[1]

        if not arg.startswith("-"):
            name = arg

    config = "config.json"

    for arg in args:
        if arg.startswith("--config"):
            config = arg.split("=")[1]
        if arg.startswith("-c"):
            config = arg.split("=")[1]

    for arg in args:
        if arg.startswith("--help"):
            printHelp()
            exit(0)
        if arg.startswith("-h"):
            printHelp()
            exit(0)

    return {
        "name": name,
        "config": config
    }


def printHelp():
    print("Usage: api.py [options] [name]")
    print("Options:")
    print("  -n, --name=NAME (name of service from config)")
    print("  -c, --config=CONFIG_FILE (default: config.json)")
    print("  -h, --help")


if __name__ == "__main__":
    args = parseArgs(args=sys.argv)
    config = FileConfigParser(args["config"]).parse()
    repository = RepositoryFactory().make(config)

    if args["name"] is None:
        results = repository.getAll()
    else:
        results = repository.getByName(name=args["name"])

    for result in results:
        print(result.name(), result.result(), result.date())
