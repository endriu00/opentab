from opentab.utility.constants import GROUP_COLOR, LAST, OPENTAB, OPENTAB_COLOR, TEE

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