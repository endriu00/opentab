from src.command.list_tree import list_tree
from src.command.reset_opentab import reset_opentab
from src.parsing.parse_cli_args import parse_cli_args

from src.command.add_tab import add_tab
from src.command.remove_group import remove_group
from src.command.remove_tabs import remove_tabs
from src.command.list_group_tabs import list_group_tabs
from src.command.list_groups import list_groups
from src.command.open_tabs import open_tabs
from src.command.init_opentab import init_opentab

from src.utility.constants import TABS_FILE_PATH, ERROR_COLOR, OPENTAB_COLOR

from src.utility.get_group_urls import get_group_urls

from src.yaml.read_yaml import read_yaml
from src.yaml.write_yaml import write_yaml

from colorama import init 

from os.path import exists

# Command names definition.
ADD = 'add'
RM = 'rm'
LS = 'ls'
OPEN = 'open'
CONFIG = 'config'
INIT = 'init'
RESET = 'reset'

def opentab():    
    # set colorama to autoreset the colors after each print
    init(autoreset=True)

    # parse arguments provided by the user
    args = parse_cli_args()

    # get the command the user has provided
    command = args.subparser

    # the user has issued an INIT command.
    if command == INIT:
        # check whether the tabs.yml file exists in the home directory.
        # Otherwise create it. Even though the command should be issued 
        # only when initializing the opentab workspace, it is necessary
        # to anticipate any usage of the command itself.
        if not exists(TABS_FILE_PATH):
            init_opentab()
        else:
            print(ERROR_COLOR+'The opentab folder already exists!\n')
            print('If you want to reset, ' 
                + 'for any reason, the folder, run:\n')
            print(OPENTAB_COLOR+'opentab reset\n')
            print('However, you should be careful with it as it would lead to a'
                ' permanent loss of your saved groups and tabs.')

    # read the tabs.yml file 
    dic = read_yaml()

    # the user has issued an ADD command.
    if command == ADD:
        group_name = args.group_name
        urls = args.urls  

        dic = add_tab(group_name=group_name, dic=dic, urls=urls)
        write_yaml(dic, 'w')

    # the user has issued a RM command.
    if command == RM:
        group_name = args.group_name
        urls = args.urls  
        
        if urls == []:
            dic = remove_group(group_name=group_name, dic=dic)
            write_yaml(dic, 'w')
        else:
            remove_tabs(group_name=group_name, dic=dic, urls=urls)
            write_yaml(dic, 'w')

    # the user has issued a LS command.
    if command == LS:
        group_name = args.group_name
        
        if group_name == '' and not args.all:
            list_groups(dic)
        elif group_name != '' and not args.all:
            list_group_tabs(group_name, dic)
        elif group_name == '' and args.all:
            list_tree(dic)

    # the user has issued an OPEN command.
    if command == OPEN:
        group_name = args.group_name
        
        urls_to_open = get_group_urls(group_name, dic)
        if args.new_session:
            session_type = 1
        else:
            session_type = 0
        open_tabs(group_name=group_name, session_type=session_type, urls=urls_to_open)
                
    # the user has issued a RESET command.
    if command == RESET:
        print('Are you sure you want to reset your tabs.yml file? [yes/n]\n')
        print(ERROR_COLOR+'Please note that this would delete ' 
            +'your saved groups and urls.')
        if input().lower() == 'yes':
            reset_opentab()
            print('Resetting...')
        else:
            print('Reset procedure canceled.')