from urllib import parse
from bullish.objects.base import Base
from bullish.schema.paging import PageLinksSchema


class PageLink(Base):
    def __init__(self, **kwargs):
        super(PageLink, self).__init__(PageLinksSchema(), kwargs)
        # parse params for next and previous
        self.next = self._parse_params(self.next, '_nextPage')
        self.previous = self._parse_params(self.previous, '_previousPage')

    def _parse_params(self, url: str, query_str: str) -> str:
        parsed_url = parse.urlparse(url)
        parsed_query = parse.parse_qs(parsed_url.query)
        if query_str in parsed_query:
            return parsed_query[query_str][0]
        return ''