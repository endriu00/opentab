from ruamel.yaml import YAML
import pprint

yaml = YAML()
# mapping is the number of spaces between two YAML keys.
# sequence is the number of spaces between the dash and the YAML value. 
# offset is the number of spaces between the key and the dash.
yaml.indent(mapping=2, sequence=1, offset=2)
with open('result.yml', 'r') as groups:
  dic = yaml.load(groups)

dic['opentab']['devops'].append('ciao')
pprint.pprint(dic)

with open('result.yml', 'w') as writing_file:
  yaml.dump(dic, writing_file)
