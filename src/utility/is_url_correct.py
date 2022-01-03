# is_url_correct checks whether the given URLs respect the format: http(s)://
def is_url_correct(url):
    if url[0:7] == 'http://' or url[0:8] == 'https://':
        return True
    return False