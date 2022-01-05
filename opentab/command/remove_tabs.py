from opentab.utility.constants import OPENTAB, ERROR_COLOR

# remove_tabs removes the URLs specified in urls for the group group_name
# from dic, a dictionary resulting from the tabs.yaml parsing operation.
# It returns the modified dictionary.
def remove_tabs(group_name, dic, urls):
    print('Removing tabs for group: ' + group_name)
    for url in urls:
        try:
            if url in dic[OPENTAB][group_name]:
                dic[OPENTAB][group_name].remove(url)
            else:
                exit(ERROR_COLOR + "URL: " + url + " is not present")
        except KeyError:
            raise KeyError
    return dic