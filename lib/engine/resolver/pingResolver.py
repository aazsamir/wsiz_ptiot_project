from lib.engine.resolver import resolver
from lib.engine import source
import os


class PingResolver(resolver.Resolver):
    def resolve(
            self,
            source: source.Source
    ) -> bool:
        result = False

        ping_param = '-n 1' if os.name == 'nt' else '-c 1'

        ping = os.popen('ping ' + ping_param + ' ' + source.source()).read()

        if 'ttl' in ping.lower():
            result = True

        return result
