import argparse

# parse_cli_args parses the CLI arguments inserted by the user.
def parse_cli_args():
    parser = argparse.ArgumentParser(prog='opentab', description='Parse opentab arguments')
    # Subparsers is a subparser constructor. 
    # dest parameter is necessary to know the name of the subparser invoked by CLI.
    subparsers = parser.add_subparsers(dest='subparser')

    # Create the init subparser.
    # It is intended to be a command without arguments for initializing 
    # the .opentab folder when it is first called.
    subparsers.add_parser('init')

    # Create the reset subparser.
    # It is intended to be a command without arguments for resetting 
    # the .opentab folder whenever it is called.
    subparsers.add_parser('reset')

    # Create the add subparser with its arguments.
    # It can be specified either a group_name with no URLs
    # or a group_name and a list of one or more URLs.
    add_parser = subparsers.add_parser('add')
    add_parser.add_argument('group_name', help='Name of the group where the URL will be '
                                               + 'added to. If the group does not exist, it creates it.')
    add_parser.add_argument('urls', nargs='*', help='URL to be added to the '
                                                    + 'specified group.')

    # Create the remove subparser with its arguments
    # It can be specified either a group_name with no URLs
    # or a group_name and a list of one or more URLs.
    remove_parser = subparsers.add_parser('rm')
    remove_parser.add_argument('group_name', help='Name of the group '
                                                  + 'where the URL will be added to.')
    remove_parser.add_argument('urls', nargs='*', help='URL to be removed from the '
                                                       + 'specified group.')

    # Create the list subparser with its arguments
    # It can be issued just an 'ls' command or an 'ls' command followed by a group_name.
    list_parser = subparsers.add_parser('ls')
    list_parser.add_argument('group_name', nargs='?', default='', help='Name of the '
                                                                       + 'group to show the URLs list of.')
    list_parser.add_argument('-a', '--all', action='store_true', help='Print every group '
                                                                      + 'each with the URLs in it.')

    # Create the open subparser with its arguments.
    # It must be passed a group name for taking the corresponding URL(s).
    open_parser = subparsers.add_parser('open')
    open_parser.add_argument('group_name', help='Name of the group from which '
                                                + 'the URL will be opened.')
    open_parser.add_argument('--new-session', '-n', action='store_true',
                             help='Open a new browser session instead of opening the tabs'
                                  + 'in the same existing session.')

    # Parse the arguments.
    return parser.parse_args()