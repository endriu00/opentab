from src.utility.constants import OPENTAB

# remove_group removes the group group_name along with its tabs from
# the dictionary dic, that represents the parsed tabs.yaml file.
def remove_group(group_name, dic):
    del dic[OPENTAB][group_name]
    return dic