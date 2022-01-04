from os.path import expanduser
HOME = expanduser("~")
OPENTAB_DIR_PATH = HOME + '/.opentab'
TABS_FILE_PATH = OPENTAB_DIR_PATH+'/devel/tabs.yml' 

OPENTAB = 'opentab'

from ruamel.yaml import YAML

def write_yaml(dic, mode):
    yaml = YAML()
    yaml.indent(mapping=2, sequence=1, offset=2)
    with open(TABS_FILE_PATH, mode) as writing_file:
        yaml.dump(dic, writing_file)

def init_devel():
    open(TABS_FILE_PATH, 'x')
    init_dic = {}       
    init_dic[OPENTAB] = {}
    write_yaml(init_dic, 'w')

if __name__ == "__main__":
    init_devel()


