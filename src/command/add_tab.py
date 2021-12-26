from src.utility.constants import OPENTAB
from src.utility.get_right_urls import get_right_urls

# add_tab adds the URLs contained in urls to the group group_name
# in the dictionary dic, representing the parsed tabs.yml file.
# It returns the modified dictionary.
def add_tab(group_name, dic, urls):
    #urls_to_add = get_right_urls(group_name, urls, dic)
    #print(urls_to_add)

    # if there is no such group, create it
    if group_name not in dic[OPENTAB]:
        dic[OPENTAB][group_name] = []

    for url in urls: #urls_to_add:
        dic[OPENTAB][group_name].append(url)

    return dic