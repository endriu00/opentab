from ruamel.yaml import YAML
from opentab.yaml_utility.read_yaml import read_yaml
from opentab.write_group import OPENTAB
from utilityV2.get_right_urls import get_right_urls

def add_tab(group, *urls):
    yaml = YAML()
    urls_to_add = get_right_urls(group, *urls)
    dic = read_yaml()
    if dic[OPENTAB][group] is None:
        dic[OPENTAB][group] = []

    for url in urls_to_add:
        dic[OPENTAB][group].append(url)

    with open('result.yml', 'w') as writing_file:
        yaml.dump(dic, writing_file)