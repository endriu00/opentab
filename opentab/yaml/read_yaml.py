from ruamel.yaml import YAML
from opentab.utility.constants import TABS_FILE_PATH

# read_yaml reads the tabs.yml file and parses it.
# It returns a dictionary parsed from the file.
def read_yaml():
    yaml = YAML()
    try:
        with open(TABS_FILE_PATH, 'r') as groups:
            dic = yaml.load(groups)
    except FileNotFoundError:
        raise FileNotFoundError
    return dic