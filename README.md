# Meet `opentab`

Tired of having hundreds of tabs open in your browser?
Tired of saying: I'll keep this tab open so that tomorrow I can study this thing better? 
Tired of being sad when closing them all after forgetting why you opened them lately?

### Then `opentab` is the bash utility made for you!

`opentab` is a CLI tool that lets you save your browser tabs in a structured way 
so that you can relax and read or work on them later. 

Think of it like a tab organizer: most of the time, you need to open again 
and again the same group of tabs, like your job's email webpage, your company's 
internal websites you have to login into everyday, your job's `Slack` account. 
Sometimes, you are working on something and you start opening pages over pages 
in your browser. This leads to tens or more tabs per argument that you are not 
willing to close. The automatic instinct you have is to bookmark them all and 
put them inside a folder in your browser. Now the fact is: you could use any 
add-on your browser is provided of, but you will soon lose track of the tabs you
saved. And, worst, you need to search for them everytime and this is so unfriendly.
Moreover, if you decide to change your default browser, you would need to export 
them all in some ways. `opentab` resolves all these issues, and it does letting 
you organize your tabs in **groups** that you can directly consult in your shell.

Exactly, if you are a shell lover, you can *save* all your tabs and *open* them
using your shell only. These are just some of the features of `opentab`!


# Features

## Add tabs

`opentab` is useless if you cannot populate it with your favourite tabs!
The `add` command is the command you will probably use the most along with
the `open` command (check it out at [open](#open-a-group-of-tabs)).

The available commands are:
- Add one empty group.
  The command is:
  [x] opentab add cool_group_name
  
- Add one *URL* to a specific group.
  The command is:
  [x] opentab add cool_group_name single_url

- Add more than one *URL* to a specific group.
  The command is:
  [x] opentab add cool_group_name first_url second_url [...] nth_url


# Remove tabs

What if your job on some tabs or some group of tabs is done? You don't want 
them to ruin your clean `opentab` workspace. You can simply delete them and
do not worry about them anymore!

The available commands are:
- Remove one group **and** the tabs in it.
  **Danger**: this will delete the tabs in the group along with it.
  The command is:
  [x] opentab rm never_coming_back_group

- Remove one URL from a group.
  The command is:
  [x] opentab rm still_existing_group deleting_url

- Remove more than one URL from a group.
  The command is:
  [x] opentab rm still_existing_group deleting_url_1 [...] deleting_url_n 


# Open a group of tabs

Now you have a good amount of groups and tabs. Let's see what `opentab` is 
capable of! Open a group of tabs specified by the group name.
The tabs will be opened in your default browser.

The available commands are:
- Open the tabs in the group in an existing browser session.
  The command is:
  [x] opentab open cool_group_name

- Open the tabs in the group in a new browser session.
  The commands are:
  [x] opentab open --new-session cool_group_name
  [x] opentab open -n cool_group_name
  

# List the tabs

You have added so many tabs to `opentab` that you have lost the number. 
Or the name of your groups. No problem, `opentab` is here to help you.
You can list:
- The groups.
- The tabs in a group.
- The tabs in every group.

The available commands are:
- List the groups you have saved.
  The command is:
  [x] opentab ls 

- List the tabs in a group.
  The command is:
  [x] opentab ls cool_group_name

- List the tabs in each group along with the groups.
  The command is:
  [x] opentab ls -a



## Usage example: 
 
- opentab add *groupname* [URL]...
  - if no URL is provided, only a group with name *groupname* is added
  - if one or more URLs are provided, a group *groupname* and the corresponding
    URLs are added to the tabs.yaml file.

- opentab rm *groupname* [URL]...
  - if no URL is provided, the group is deleted along with each URL in it.
  - if one or more URLs are provided, their are removed from the group *groupname*

- opentab *groupname* --browser firefox --keep-alive
  where:
    devops is the name of the group of tabs containing a related subject
    --browser firefox is the chosen browser for opening the tabs
    --keep-alive is the flag for telling opentab to not close the tabs when the browser session is closed

- opentab ls [*groupname*]
  - if no group is provided, it shows the list of the saved groups.
  - if the group name is provided, it shows the URL(s) in that group. 

## DEFAULT VALUES AND CONFIG FILE

A config file should be created. 
In the config file, the user should insert:
- the preferred browser
- the preferred way to handle multiple calls to opentab:
  open multiple sessions of the same browser or open every new tab in the same session?


Config file structure (should be yaml):

config:
  browser: 
  #keep-alive: 
  launch-multiple-sessions: 


## USE CASE

devops has 10 tabs

opentab devops 

options:
1. opentab removes entirely devops group from its DB
2. user has to remove manually the URLs
3. if user provides the -k/--keep-alive flag, opentab does not remove anything from the group
4. CHECK IF THERE EXIST A WAY TO DETERMINE THE TABS USER CLOSES. 
   IF YES: opentab removes every page the user closes and puts it into an internal recycle bin 

firefox opens 10 tabs

## GROUP FILE

One of the most important file for both the user and `opentab` is
`tabs.yaml` file. It stores the groups the user adds, and the URLs inside of each group.
`tabs.yaml` can be found in the home directory under `.opentab` folder for Linux systems.
**It is recommended to not delete it in any case, as it would compromize the whole stability of the tool.** 





## REFERENCES

open browser sessions: https://docs.python.org/3/library/webbrowser.html