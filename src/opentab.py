from src.parsing.parse_cli_args import parse_cli_args

from src.command.add_tab import add_tab
from src.command.remove_group import remove_group
from src.command.remove_tabs import remove_tabs
from src.command.list_group_tabs import list_group_tabs
from src.command.list_groups import list_groups

from src.yaml.read_yaml import read_yaml
from src.yaml.write_yaml import write_yaml

# Command names definition.
ADD = 'add'
RM = 'rm'
LS = 'ls'
OPEN = 'open'

def opentab():

    # TODO
    # check whether the tabs.yml file exists in the home directory.
    # Otherwise create it.
    
    

    # parse arguments provided by the user
    args = parse_cli_args()
    print(args)

    # store the variables in a more readable way
    command = args.subparser
    group_name = args.group_name
    if command != LS and command != OPEN: 
        urls = args.urls  

    # read the tabs.yml file 
    dic = read_yaml()

    if command == ADD:
        dic = add_tab(group_name=group_name, dic=dic, urls=urls)
        print(dic)
        write_yaml(dic, 'w')
    if command == RM:
        if urls is []:
            remove_group(group_name=group_name, dic=dic)
        else:
            remove_tabs(group_name=group_name, dic=dic, urls=urls)
    if command == LS:
        if group_name == '':
            list_groups(dic)