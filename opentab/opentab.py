from opentab.exception.GroupExists import GroupExists
from opentab.command.list_tree import list_tree
from opentab.command.reset_opentab import reset_opentab
from opentab.parsing.parse_cli_args import parse_cli_args

from opentab.command.add_tab import add_tab
from opentab.command.remove_group import remove_group
from opentab.command.remove_tabs import remove_tabs
from opentab.command.list_group_tabs import list_group_tabs
from opentab.command.list_groups import list_groups
from opentab.command.open_tabs import open_tabs
from opentab.command.init_opentab import init_opentab

from opentab.utility.constants import TABS_FILE_PATH, ERROR_COLOR, OPENTAB_COLOR, OPENTAB

from opentab.utility.get_group_urls import get_group_urls

from opentab.yaml.read_yaml import read_yaml
from opentab.yaml.write_yaml import write_yaml

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
            print(ERROR_COLOR + 'The opentab folder already exists!\n')
            print('If you want to reset, '
                  + 'for any reason, the folder, run:\n')
            print(OPENTAB_COLOR + 'opentab reset\n')
            print('However, you should be careful with it as it would lead to a'
                  ' permanent loss of your saved groups and tabs.')

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

    # read the tabs.yml file
    try:
        dic = read_yaml()
    except FileNotFoundError:
        exit(ERROR_COLOR + "File not found!!\nYou need to opentab reset")
        
    # the user has issued an ADD command.
    if command == ADD:
        group_name = args.group_name
        urls = args.urls
        try:
            dic = add_tab(group_name=group_name, dic=dic, urls=urls)
        except GroupExists:
            exit(ERROR_COLOR + "The group already exists")
        write_yaml(dic, 'w')

    # the user has issued a RM command.
    if command == RM:
        group_name = args.group_name
        urls = args.urls
        if not urls:
            try:
                dic = remove_group(group_name=group_name, dic=dic)
            except KeyError:
                exit(ERROR_COLOR + "The Group does not exists")

            write_yaml(dic, 'w')
        else:
            try:
                remove_tabs(group_name=group_name, dic=dic, urls=urls)
            except KeyError:
                exit(ERROR_COLOR + "The Group does not exists")
            write_yaml(dic, 'w')

    # the user has issued a LS command.
    if command == LS:
        group_name = args.group_name

        if group_name == '' and not args.all:
            list_groups(dic)
        elif group_name != '' and not args.all:
            try:
                list_group_tabs(group_name, dic)
            except KeyError:
                exit(ERROR_COLOR + "The Group does not exists")
        elif group_name == '' and args.all:
            list_tree(dic)

    # the user has issued an OPEN command.
    if command == OPEN:
        group_name = args.group_name

        try:
            urls_to_open = get_group_urls(group_name, dic)
        except KeyError:
            exit(ERROR_COLOR + "THE GROUP DOES NOT EXIST")

        if not urls_to_open:
            exit(ERROR_COLOR + "THERE ARE NOT URLS TO OPEN")

        if args.new_session:
            session_type = 1
        else:
            session_type = 0

        open_tabs(group_name=group_name, session_type=session_type, urls=urls_to_open)