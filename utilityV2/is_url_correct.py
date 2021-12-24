from re import compile
def is_url_correct(*urls):
    # regex for check the link format
    urls_correct = ''
    format = compile('http[s]{0,1}:\/\/.*')
    for url in urls:

        if format.match(url):
            return True
        return False