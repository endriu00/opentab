from os import makedirs

from opentab.yaml.write_yaml import write_yaml
from opentab.utility.constants import TABS_FILE_PATH, OPENTAB_DIR_PATH, OPENTAB, ERROR_COLOR

# init_opentab inits the opentab workspace.
# It creates the .opentab directory and initializes the tabs.yml file
# with a first level key.
def init_opentab():
    try:
        makedirs(OPENTAB_DIR_PATH)
    except FileExistsError as fileExistsError:
        exit(ERROR_COLOR+"\nDirectory already exists, you need to opentab Reset\n")
    open(TABS_FILE_PATH, 'x')
    init_dic = {}       
    init_dic[OPENTAB] = {}
    write_yaml(init_dic, 'w')