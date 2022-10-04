from urllib import parse
def parse_url(url):
    result = dict(parse.parse_qsl(parse.urlsplit(url).query))
    return result


if __name__ == '__main__':
    assert parse_url('https://example.com/path/to/page?name=ferret&color=purple') == {'name': 'ferret', 'color': 'purple'}
    assert parse_url('https://example.com/path/to/page?name=ferret&color=purple&') == {'name': 'ferret', 'color': 'purple'}
    assert parse_url('http://example.com/') == {}
    assert parse_url('http://example.com/?') == {}
    assert parse_url('http://example.com/?name=Dima') == {'name': 'Dima'}

    assert parse_url('https://example.com/path/to/page?') == {}
    assert parse_url('http://example.com?sid=1234567') == {'sid': '1234567'}
    assert parse_url('https://example.tracker.com/?cid=9999&lp={escapedlpurl}') == {'cid': '9999', 'lp': '{escapedlpurl}'}
    assert parse_url('http://example.com?sid=1234567&src=google') == {'sid': '1234567', 'src': 'google'}
    assert parse_url('https://hostiq.ua/blog/what-is-url/') == {}
    assert parse_url('https://www.google.com/search?q=cinema&uact=5&sclient=gws-wiz') == {'q': 'cinema', 'uact': '5', 'sclient': 'gws-wiz'}
    assert parse_url('http://example.com/?continent=3&country=15&city=54') == {'continent': '3', 'country': '15', 'city': '54'}
    assert parse_url('https://www.google.com/search?q=python') == {'q': 'python'}
    assert parse_url('https://www.youtube.com/results?search_query=lessons') == {'search_query': 'lessons'}
    assert parse_url('https://www.youtube.com/') == {}