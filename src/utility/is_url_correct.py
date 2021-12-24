from re import compile

# is_url_correct checks whether the given URLs respect the format: http(s)://
def is_url_correct(urls):
    urls_correct = ''
    format = compile('http[s]{0,1}:\/\/.*')
    for url in urls:
        if format.match(url):
            return True
        return False