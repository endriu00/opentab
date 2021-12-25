from src.utility.constants import OPENTAB, OPENTAB_COLOR, GROUP_COLOR, URL_COLOR

def list_tree(dic):
    print(OPENTAB_COLOR + OPENTAB)
    for group in dic[OPENTAB]:
        print('|_____ ' + GROUP_COLOR + group)
        for url in dic[OPENTAB][group]:
            print('       |______ ' + URL_COLOR + url)