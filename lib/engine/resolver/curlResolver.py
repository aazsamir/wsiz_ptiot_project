import pycurl
from io import BytesIO
from urllib.parse import urlencode
import re

from lib.engine.resolver import resolver
from lib.engine.source import Source, Method


class CurlResolver(resolver.Resolver):
    def resolve(
            self,
            source: Source
    ) -> bool:
        buffer = BytesIO()
        curl = pycurl.Curl()
        curl.setopt(pycurl.URL, source.source())
        curl.setopt(pycurl.WRITEDATA, buffer)

        if source.method() == Method.POST:
            postfields = urlencode({})
            curl.setopt(pycurl.POSTFIELDS, postfields)

        curl.perform()
        curl.close()

        if source.regex() is not None:
            body = buffer.getvalue()

            return re.search(source.regex(), body.decode('utf-8')) is not None

        return True
