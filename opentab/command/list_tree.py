from opentab.utility.constants import BRANCH, LAST, OPENTAB, OPENTAB_COLOR, GROUP_COLOR, SPACE, TEE, URL_COLOR

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