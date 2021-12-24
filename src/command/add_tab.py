from src.utility.constants import OPENTAB
from src.utility.get_right_urls import get_right_urls

# add_tab adds the URLs contained in urls to the group group_name
# in the dictionary dic, representing the parsed tabs.yml file.
# It returns the modified dictionary.
def add_tab(group_name, dic, urls):
    urls_to_add = get_right_urls(group_name, urls)
    if group_name in dic[OPENTAB] and dic[OPENTAB][group_name] is None:
        dic[OPENTAB][group_name] = []

    for url in urls_to_add:
        dic[OPENTAB][group_name].append(url)

    return dic