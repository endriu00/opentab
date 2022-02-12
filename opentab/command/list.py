from opentab.utility.constants import GROUP_COLOR, LAST, OPENTAB, OPENTAB_COLOR, TEE, RESET_COLOR, URL_COLOR, BRANCH, SPACE
from opentab.utility.get_group_urls import get_group_urls

##############################
#         list_groups        #
##############################

# list_groups prints the groups stored in opentab.
def list_groups(dic):
    size = len(dic[OPENTAB])
    i = 0
    char = TEE

    print('Groups saved in ' + OPENTAB_COLOR + 'opentab:')
    print()
    print(OPENTAB_COLOR + OPENTAB)
    for group in dic[OPENTAB]:
        if i == (size-1):
            char = LAST    
        i += 1
        print(char + GROUP_COLOR + group)


##############################
#      list_group_tabs       #
##############################

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


##############################
#          list_tree         #
##############################

# list_tree prints the groups, along with the inner URLs, in a treeish format.
def list_tree(dic):
    group_size = len(dic[OPENTAB])
    group_i = 0
    group_char = TEE
    
    print(OPENTAB_COLOR + OPENTAB)

    # First-level elements scope.
    # Print each element along with its subelement.
    for group in dic[OPENTAB]:
        tabs_size = len(dic[OPENTAB][group])
        tabs_i = 0
        tabs_char = TEE
        branch_char = BRANCH

        # determine whether it is the last element
        if group_i == (group_size-1):
            group_char = LAST    
        print(group_char + GROUP_COLOR + group)

        # Second-level elements scope.
        # Print each subelement.
        for url in dic[OPENTAB][group]:

            # determine whether it is the last subelement
            if tabs_i == (tabs_size-1):
                tabs_char = LAST

            # if it is the last element, do not print the BRANCH symbol
            if group_char == LAST:
                branch_char = SPACE

            print(branch_char + tabs_char + URL_COLOR + url)
            tabs_i += 1

        group_i += 1