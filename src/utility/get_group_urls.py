from src.write_group import OPENTAB
from src.yaml.read_yaml import read_yaml

# If group does not exist return FALSE.
# Else if group exists return that group.
def get_group_urls(group):
    dic = read_yaml()
    try:
        dic_urls = dic[OPENTAB][group]
    except KeyError:
        return False
    return dic_urls