from src.utility.constants import OPENTAB
from src.utility.get_group_urls import get_group_urls

# list_group_tabs lists the tabs inside the group group_name.
# To accomplish the task, it takes the dictionary dic, 
# that represents the parsed tabs.yml file.
def list_group_tabs(group_name, dic):
    print('Tabs in ' + group_name + ' are:')
    urls = get_group_urls(group_name=group_name, dic=dic)
    if urls == []:
        print('There is no tabs for the group ' + group_name)
        return
    print(group_name)
    for url in urls:
        print('|_______ ' + url)