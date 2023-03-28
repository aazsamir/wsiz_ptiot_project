from lib.engine.source import Source, Type
from lib.engine.resolver.resolver import Resolver
from lib.engine.resolver.pingResolver import PingResolver
from lib.engine.resolver.curlResolver import CurlResolver


class ResolverFactory:
    def make(
            self,
            source: Source,
    ) -> Resolver:
        if source.type() == Type.CURL:
            return CurlResolver()

        if source.type() == Type.PING:
            return PingResolver()

        return Resolver()
