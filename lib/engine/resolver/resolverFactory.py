from lib.engine import source as engineSource
from lib.engine.resolver import resolver, pingResolver, curlResolver


class ResolverFactory:
    def make(
            self,
            source: engineSource.Source,
    ) -> resolver.Resolver:
        if source.type() == engineSource.Type.CURL:
            return curlResolver.CurlResolver()

        if source.type() == engineSource.Type.PING:
            return pingResolver.PingResolver()

        return resolver.Resolver()
