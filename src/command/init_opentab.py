from os import makedirs

from src.yaml.write_yaml import write_yaml
from src.utility.constants import TABS_FILE_PATH, OPENTAB_DIR_PATH, OPENTAB

# init_opentab inits the opentab workspace.
# It creates the .opentab directory and initializes the tabs.yml file
# with a first level key.
def init_opentab():
    makedirs(OPENTAB_DIR_PATH)
    open(TABS_FILE_PATH, 'x')
    init_dic = {}       
    init_dic[OPENTAB] = {}
    write_yaml(init_dic, 'w')