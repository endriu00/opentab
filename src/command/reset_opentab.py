from src.utility.constants import TABS_FILE_PATH, OPENTAB

from src.yaml.write_yaml import write_yaml

# reset_opentab resets the .opentab directory.
def reset_opentab():
    open(TABS_FILE_PATH, 'w')
    init_dic = {}
    init_dic[OPENTAB] = {}
    write_yaml(init_dic, 'w')