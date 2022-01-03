from src.utility.get_group_urls import get_group_urls
from src.utility.is_url_correct import is_url_correct

# get_right_urls takes the new URLs, urls, to be added to the group group_name.
# The URLs will be added to dic, the YAML file parsed dictionary.
# It returns a list of the new correct URLs.
def get_right_urls(group, urls, dic):
    # get the group urls.
    group_urls = get_group_urls(group, dic)
    new_urls = []

    for url in urls:
        # if the inserting url does not match an established pattern
        # or it is already in the group, do not insert it.
        if is_url_correct(url) and url not in group_urls:
            new_urls.append(url)
        else:
            print(url + ' has not been recognized as a correct URL '
                + 'or it is already in the group.')

    return new_urls