#!/usr/bin/env python3

import sys
import time
import json

from run import run


def getTimeout() -> int:
    with open("config.json", 'r') as file:
        timeout = json.load(file)["timeout"]

    return int(timeout) if timeout else 60


def main() -> None:
    timeout = getTimeout()

    while True:
        run(sys.argv)
        time.sleep(timeout)


if __name__ == '__main__':
    main()
