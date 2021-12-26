from src.command.list_tree import list_tree
from src.parsing.parse_cli_args import parse_cli_args

from src.command.add_tab import add_tab
from src.command.remove_group import remove_group
from src.command.remove_tabs import remove_tabs
from src.command.list_group_tabs import list_group_tabs
from src.command.list_groups import list_groups
from src.command.open_tabs import open_tabs

from src.utility.get_group_urls import get_group_urls

from src.yaml.read_yaml import read_yaml
from src.yaml.write_yaml import write_yaml

from colorama import init 

# Command names definition.
ADD = 'add'
RM = 'rm'
LS = 'ls'
OPEN = 'open'

def opentab():

    # TODO
    # check whether the tabs.yml file exists in the home directory.
    # Otherwise create it.
    
    
    # set colorama to autoreset the colors after each print
    init(autoreset=True)

    # parse arguments provided by the user
    args = parse_cli_args()

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
        if urls == []:
            dic = remove_group(group_name=group_name, dic=dic)
            write_yaml(dic, 'w')
        else:
            remove_tabs(group_name=group_name, dic=dic, urls=urls)
            write_yaml(dic, 'w')
    if command == LS:
        if group_name == '' and not args.all:
            list_groups(dic)
        elif group_name != '' and not args.all:
            list_group_tabs(group_name, dic)
        elif group_name == '' and args.all:
            list_tree(dic)

    if command == OPEN:
        urls_to_open = get_group_urls(group_name, dic)
        open_tabs(group_name=group_name, session_type=2, urls=urls_to_open)