# is_url_correct checks whether the given URLs respect the format: http(s)://
def is_url_correct(url):
    if url[0:4] == 'http' or url[0:5] == 'https':
        print('heretrue')
        return True
    return False