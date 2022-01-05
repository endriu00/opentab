from webbrowser import open as web_open

from opentab.utility.constants import GROUP_COLOR, URL_COLOR

OPEN_IN_SAME_SESSION = 2

# open_tabs opens a group of tabs taken from group_name.
# If session_type is 0, the tabs are opened in any existing browser session. 
# If session_type is 1, a new browser session is opened. 
# If session_type is 2, new tabs will be opened next to the existing ones.
# urls are the URLs for the group group_name. 
def open_tabs(group_name, session_type, urls):
    in_session = False
    print('Opening tabs group: ' + GROUP_COLOR + group_name)
    for url in urls:
        web_open(url, new=session_type, autoraise=True)
        print('Successfully opened: ' + URL_COLOR + url)
        if not in_session:
            session_type = OPEN_IN_SAME_SESSION
            in_session = True