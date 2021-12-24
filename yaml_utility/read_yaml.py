from ruamel.yaml import YAML

def read_yaml():
    yaml = YAML()
    with open('result.yml', 'r') as groups:
        dic = yaml.load(groups)

    return dic