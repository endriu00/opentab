# TABS_FILE_PATH is the path of the yml file containing the tabs
# for the groups inserted by the user.
from os.path import expanduser, exists
HOME = expanduser("~")
OPENTAB_DIR_PATH = HOME + '/.opentab'
if exists(OPENTAB_DIR_PATH+'/devel'):
    TABS_FILE_PATH = OPENTAB_DIR_PATH+'/devel/tabs.yml' 
else: 
    TABS_FILE_PATH = OPENTAB_DIR_PATH+'/tabs.yml' 

# OPENTAB is the name of the first level key of the tabs.yaml file.
OPENTAB = 'opentab'

###### COLORS ######

# Define opentab, group and tabs colors.
from colorama import Fore, Style
OPENTAB_COLOR = Style.BRIGHT + Fore.YELLOW
GROUP_COLOR = Style.BRIGHT + Fore.CYAN
URL_COLOR = Style.BRIGHT + Fore.GREEN
ERROR_COLOR = Style.BRIGHT + Fore.RED
WARNING_COLOR = Style.BRIGHT + Fore.LIGHTWHITE_EX
RESET_COLOR = Style.RESET_ALL

###### URL LISTING CHAR ######

# Define chars for tabs listing.
# prefix components:
SPACE =  '    '
BRANCH = '│   '
# pointers:
TEE =    '├── '
LAST =   '└── '