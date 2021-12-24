from src.utility.constants import OPENTAB

# list_group_tabs lists the tabs inside the group group_name.
# To accomplish the task, it takes the dictionary dic, 
# that represents the parsed tabs.yml file.
def list_group_tabs(group_name, dic):
    print('Tabs in ' + group_name + ' are:')
    for url in dic[OPENTAB][group_name]:
        print(url)