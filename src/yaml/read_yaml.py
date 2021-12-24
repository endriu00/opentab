from ruamel.yaml import YAML
from src.__main__ import TABS_FILE_PATH

# read_yaml reads the tabs.yml file and parses it.
# It returns a dictionary parsed from the file.
def read_yaml():
    yaml = YAML()
    with open(TABS_FILE_PATH, 'r') as groups:
        dic = yaml.load(groups)
        
    return dic