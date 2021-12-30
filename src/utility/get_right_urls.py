from src.utility.get_group_urls import get_group_urls
from src.utility.is_url_correct import is_url_correct

# Ritorna le urls corrette oppure null
def get_right_urls(group, urls, dic):
    # prende le urls che appartengono ad un gruppo
    group_urls = get_group_urls(group, dic)
    print(group_urls)

    for url in urls:
        # if the inserting url does not match an established pattern
        # or it is already in the group, do not insert it.
        if is_url_correct(url) and url not in group_urls:
            group_urls.append(url)
        else:
            print(url + ' has not been recognized as a correct URL '
                + 'or it is already in the group.')

    print(group_urls)
    return group_urls