from opentab.utility.constants import OPENTAB
from opentab.yaml.read_yaml import read_yaml

# get_group_urls gets the URLs for a group group_name. If group does not exist 
# it returns an empty list, otherwise it returns the URLs in that group.
def get_group_urls(group_name, dic):
    group_urls = []
    try:
        group_urls = dic[OPENTAB][group_name]
    except KeyError:
        raise KeyError
    return group_urls