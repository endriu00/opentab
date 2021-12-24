from parsing.parse_cli_args import parse_cli_args

# TODO HANDLE WINDOWS PATHS
# TABS_FILE_PATH is the path of the yml file containing the tabs
# for the groups inserted by the user.
TABS_FILE_PATH = '~/.opentab/tabs.yml'

def main():

    # TODO
    # check whether the tabs.yml file exists in the home directory.
    # Otherwise create it.
    
    # parse arguments provided by the user
    parse_cli_args()

    # 


if __name__ == '__main__':
    main()