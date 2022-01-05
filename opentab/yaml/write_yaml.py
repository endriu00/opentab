from ruamel.yaml import YAML
from opentab.utility.constants import TABS_FILE_PATH

# write_yaml writes a dictionary, dic, inside the tabs.yml file 
# respecting the YAML format specification.
# The opening mode for the file can be specified in mode parameter. 
def write_yaml(dic, mode):
    yaml = YAML()
    # mapping is the number of spaces between two YAML keys.
    # sequence is the number of spaces between the dash and the YAML value. 
    # offset is the number of spaces between the key and the dash.
    yaml.indent(mapping=2, sequence=1, offset=2)
    with open(TABS_FILE_PATH, mode) as writing_file:
        yaml.dump(dic, writing_file)
