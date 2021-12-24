from src.utility.constants import OPENTAB

# remove_tabs removes the URLs specified in urls for the group group_name
# from dic, a dictionary resulting from the tabs.yaml parsing operation.
# It returns the modified dictionary.
def remove_tabs(group_name, dic, urls):
    print('Removing tabs for group: ' + group_name)
    for url in urls:
        if url in dic[OPENTAB][group_name]:
            dic[OPENTAB][group_name].remove(url)
    return dic