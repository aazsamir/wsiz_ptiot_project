#!/usr/bin/env python

import sys

from lib.engine.service import Service


def parseArgs(args: list):
    args = args[1:]

    parseHelp(args)

    filepath = parseFilepath(args)
    verbose = parseVerbose(args)

    return {
        'filepath': filepath,
        'verbose': verbose
    }


def parseHelp(args: list) -> None:
    for arg in args:
        if arg == '--help' or arg == '-h':
            printHelp()
            break


def parseFilepath(args: list) -> str:
    filepath = "config.json"

    for arg in args:
        if arg.startswith('--config='):
            filepath = arg.split('=')[1]
            break

        if arg.startswith('-c'):
            filepath = sys.argv[sys.argv.index(arg) + 1]
            break

        if not arg.startswith('-'):
            filepath = arg
            break

    if filepath is None:
        printHelp()
        sys.exit(1)

    return filepath


def parseVerbose(args: list) -> bool:
    for arg in args:
        if arg == '--verbose' or arg == '-v' or arg == '-vv' or arg == '-vvv':
            return True

    return False


def printHelp() -> None:
    print("Usage: ./run.py [config_file]")
    print("Options:")
    print("  -c, --config=FILE     Specify config file. Default: config.json")
    print("  -h, --help            Show this help message and exit")
    print("  -v, --verbose         Show verbose output")
    sys.exit(1)


def run(sys_args: list):
    args = parseArgs(sys_args)
    service = Service(args["filepath"], args["verbose"])
    service.run()


if __name__ == '__main__':
    run(sys.argv)
