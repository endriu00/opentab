import argparse

# parse_cli_args parses the CLI arguments inserted by the user.
def parse_cli_args():
    parser = argparse.ArgumentParser(prog='opentab', description='Parse opentab arguments')

    # Subparsers is a subparser constructor.
    subparsers = parser.add_subparsers()

    # Create the add subparser with its arguments.
    # It can be specified either a groupname with no URLs
    # or a groupname and a list of one or more URLs.
    add_parser = subparsers.add_parser('add')
    add_parser.add_argument('groupname', help='Name of the group where the URL will be '
                            + 'added to. If the group does not exist, it creates it.')
    add_parser.add_argument('urls', nargs='*', help='URL to be added to the ' 
                            + 'specified group.')

    # Create the remove subparser with its arguments
    # It can be specified either a groupname with no URLs
    # or a groupname and a list of one or more URLs.
    remove_parser = subparsers.add_parser('rm')
    remove_parser.add_argument('groupname', help='Name of the group '
                            + 'where the URL will be added to.')
    remove_parser.add_argument('urls', nargs='*', help='URL to be removed from the ' 
                            + 'specified group.')
    
    # Create the list subparser with its arguments
    # It can be issued just an 'ls' command or an 'ls' command followed by a groupname.
    list_parser = subparsers.add_parser('ls')
    list_parser.add_argument('groupname', nargs='?', default='', help='Name of the '
                            + 'group to show the URLs list of.')

    # Create the open subparser with its arguments.
    # It must be passed a group name for taking the corresponding URL(s).
    open_parser = subparsers.add_parser('open')
    open_parser.add_argument('groupname', help='Name of the group from which '
                            + 'the URL will be opened.')

    # Parse the arguments.
    return parser.parse_args()


def main():
    parse_cli_args()

if __name__ == "__main__":
    main()