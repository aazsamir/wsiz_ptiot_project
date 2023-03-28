from lib.engine.resolver.resolver import Resolver
from lib.engine.source import Source
import os


class PingResolver(Resolver):
    def resolve(
            self,
            source: Source
    ) -> bool:
        result = False

        ping_param = '-n 1' if os.name == 'nt' else '-c 1'

        ping = os.popen('ping ' + ping_param + ' ' + source.source()).read()

        if 'ttl' in ping.lower():
            result = True

        return result
