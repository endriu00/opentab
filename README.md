# OPENTAB

**Tired of having hundreds of tabs open in your browser?** 
**Tired of saying: I'll keep this tab open so that tomorrow I can study this thing better?**
**Tired of being sad when closing them all after forgetting why you opened them lately?**

## Then Opentab is the bash utility made for you!

Opentab should:

### Open a group of tabs
- open a group *groupname* of tabs specified by the group name *groupname*

### Be smart 
- automatically collect a group of tabs based on a common pattern name (?????)

### Add/remove tabs to/from a group
- add a tab *URL* to a specific group *groupname*
- remove a tab *URL* from a specific group *groupname*
- remove an entire group specifying the group name

### Group listing
- list the groups registered
- list the groups registered with their URLs
- list a specific group with every URL in it



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

If the file has been mistakenly deleted, you can call:

  opentab restore 


- It should be a YAML file
  opentab:
    devops:
      - 
      - 
      - 
    


- Every group is a directory
--- .opentab
    |_______
            | devops
            |________
                     | devops.txt -> URLs

            | restaurants
            | devel



## REFERENCES

open browser sessions: https://docs.python.org/3/library/webbrowser.html