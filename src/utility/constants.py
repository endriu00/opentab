# TODO HANDLE WINDOWS PATHS
# TABS_FILE_PATH is the path of the yml file containing the tabs
# for the groups inserted by the user.
from os.path import expanduser
HOME = expanduser("~")
TABS_FILE_PATH = HOME+'/.opentab/tabs.yml'

# OPENTAB is the name of the first level key of the tabs.yaml file.
OPENTAB = 'opentab'

from colorama import Fore, Style
OPENTAB_COLOR = Style.BRIGHT + Fore.YELLOW
GROUP_COLOR = Style.BRIGHT + Fore.CYAN
URL_COLOR = Style.BRIGHT + Fore.GREEN
