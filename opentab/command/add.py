from opentab.utility.constants import OPENTAB
from opentab.utility.get_right_urls import get_right_urls
from opentab.exception.GroupExists import GroupExists

# add_tab adds the URLs contained in urls to the group group_name
# in the dictionary dic, representing the parsed tabs.yml file.
# It returns the modified dictionary.
def add_tab(group_name, dic, urls):
    if group_name in dic[OPENTAB] and urls == []:
        raise GroupExists

    # if there is no such group, create it
    if group_name not in dic[OPENTAB]:
        dic[OPENTAB][group_name] = []

    right_urls = get_right_urls(group_name, urls, dic)

    for url in right_urls:
        dic[OPENTAB][group_name].append(url)

    return dic