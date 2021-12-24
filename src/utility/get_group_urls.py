from opentab.write_group import OPENTAB
from opentab.yaml_utility.read_yaml import read_yaml
# If group not exist return FALSE
# If group exist return that group
def get_group_urls(group):
    dic = read_yaml()
    try:
        dic_urls = dic[OPENTAB][group]
    except KeyError:
        return False
    return dic_urls