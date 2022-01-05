from opentab.utility.constants import GROUP_COLOR, LAST, OPENTAB, RESET_COLOR, TEE, URL_COLOR
from opentab.utility.get_group_urls import get_group_urls

# list_group_tabs lists the tabs inside the group group_name.
# To accomplish the task, it takes the dictionary dic, 
# that represents the parsed tabs.yml file.
def list_group_tabs(group_name, dic):
    try:
        size = len(dic[OPENTAB][group_name])
    except KeyError:
        raise KeyError
    i = 0
    char = TEE

    print('Tabs in ' + GROUP_COLOR + group_name + RESET_COLOR + ' are:')
    print()
    urls = get_group_urls(group_name=group_name, dic=dic)
    if urls == []:
        print('There is no tabs for the group ' + GROUP_COLOR + group_name)
        return
    print(GROUP_COLOR + group_name)
    for url in urls:
        if i == (size-1):
            char = LAST
        i += 1
        print(char + URL_COLOR + url)