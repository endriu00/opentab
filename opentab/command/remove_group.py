from opentab.utility.constants import OPENTAB, ERROR_COLOR

# remove_group removes the group group_name along with its tabs from
# the dictionary dic, that represents the parsed tabs.yaml file.
def remove_group(group_name, dic):
    # For check if group exists
    try:
        del dic[OPENTAB][group_name]
    except KeyError:
        raise KeyError

    return dic