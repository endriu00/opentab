from src.utility.constants import OPENTAB

def list_groups(dic):
    print('Groups saved in opentab:')
    print('opentab')
    for group in dic[OPENTAB]:
        print('|________' + group)
