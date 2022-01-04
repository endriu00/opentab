from src.utility.constants import TABS_FILE_PATH, OPENTAB
from src.command.init_opentab import init_opentab
from src.yaml.write_yaml import write_yaml

# reset_opentab resets the .opentab directory.
def reset_opentab():
    try:
        open(TABS_FILE_PATH, 'w')
    except:
        init_opentab()
    init_dic = {}
    init_dic[OPENTAB] = {}
    write_yaml(init_dic, 'w')