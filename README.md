# Meet `opentab`

Tired of having hundreds of tabs open in your browser?  
Tired of saying: I'll keep this tab open so that tomorrow I can study this thing better?  
Tired of being sad when closing them all after forgetting why you opened them lately?  

### Then `opentab` is the bash utility made for you!

`opentab` is a CLI tool that lets you save your browser tabs in a structured way 
so that you can relax and read or work on them later. 

###### INSERT VIDEO HERE ########

# Index

- [Why opentab](#why-opentab)
- [Features](#features)
  - [Add tabs](#add-tabs)
  - [Remove tabs](#remove-tabs)
  - [Open tabs](#open-tabs)
  - [List tabs](#list-tabs)
  - [Init opentab](#init-opentab)
  - [Reset opentab](#reset-opentab)
- [Low-Level Details](#low-level-details)
  - [tabs.yaml](#tabsyaml)
- [Contribute](#contribute)
  - [Devel Environment](#devel-environment)


# Why `opentab`

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
  :heavy_check_mark: opentab add cool_group_name

- Add one *URL* to a specific group.  
  The command is:  
  :heavy_check_mark: opentab add cool_group_name single_url

- Add more than one *URL* to a specific group.  
  The command is:  
  :heavy_check_mark: opentab add cool_group_name first_url second_url [...] nth_url


## Remove tabs

What if your job on some tabs or some group of tabs is done? You don't want 
them to ruin your clean `opentab` workspace. You can simply delete them and
do not worry about them anymore!  

The available commands are:  
- Remove one group **and** the tabs in it.  
  :warning: **Danger**: this will delete the tabs in the group along with it. :warning:  
  The command is:  
  :heavy_check_mark: opentab rm never_coming_back_group

- Remove one URL from a group.  
  The command is:  
  :heavy_check_mark: opentab rm still_existing_group deleting_url

- Remove more than one URL from a group.  
  The command is:  
  :heavy_check_mark: opentab rm still_existing_group deleting_url_1 [...] deleting_url_n 


## Open tabs

Now you have a good amount of groups and tabs. Let's see what `opentab` is 
capable of! Open a group of tabs specified by the group name.  
The tabs will be opened in your default browser.  

The available commands are:  
- Open the tabs in the group in an existing browser session.  
  The command is:  
  :heavy_check_mark: opentab open cool_group_name

- Open the tabs in the group in a new browser session.  
  The commands are:  
  :heavy_check_mark: opentab open --new-session cool_group_name  
  :heavy_check_mark: opentab open -n cool_group_name
  

## List tabs

You have added so many tabs to `opentab` that you have lost the number. 
Or the name of your groups. No problem, `opentab` is here to help you.
You can list:
- The groups.
- The tabs in a group.
- The tabs in every group.

The available commands are:
- List the groups you have saved.  
  The command is:  
  :heavy_check_mark: opentab ls 
- List the tabs in a group.  
  The command is:  
  :heavy_check_mark: opentab ls cool_group_name
- List the tabs in each group along with the groups.  
  The command is:  
  :heavy_check_mark: opentab ls -a


## Init `opentab`

Like most known tools, `opentab` needs to be initialized. It is not that hard
though. It is just a matter of a command. This is the very first thing you 
should do after installing `opentab`, if you do not want to get a really
unfriendly error message.

The available command is:  
- Initialize the workspace.  
  The command is:  
  :heavy_check_mark: opentab init


## Reset `opentab`

You have probably messed around with `opentab` and its `tabs.yaml` file  if you
need to read this. No worries! While you could have lost your saved tabs, you 
can still get back to a fully working environment with a single command.

The available command is:  
- Reset the workspace.  
  :warning: **Danger**: this will delete **every** group and tabs in it. :warning:  
  The command is:  
  :heavy_check_mark: opentab reset


# Low-Level Details

`opentab` does well its job. Let's see how it works.

## tabs.yaml 

One of the most important file for both the user and `opentab` is the `tabs.yaml`
file. It stores the groups the user adds, and the URLs inside of each group.
`tabs.yaml` can be found in the home directory under `.opentab` folder for Linux
systems. **It is recommended to not delete it in any case, as it would compromise** 
**the whole stability of the tool**. 


# Contribute

You really like `opentab` but you see something that is not working or you want
to add some cool features? You could do two things:
- Submit an issue.
- Submit an issue, open a pull request, work on the changes.

We prefer you to do the second, as it would be a great opportunity to dirt your
own hands and contribute to an open source project, but we appreciate the first
option too, as it sounds like someone is enjoying `opentab` and he finds it 
useful, or at least pretty. 
Below there are a few headlines to let you get started in case you want to 
contribute the hard way.

## Devel Environment

What if you have collected hundreds of tabs in several groups, you start working
on `opentab` to add new features or to fix existing ones, and suddenly your 
`tabs.yaml` file gets corrupted?  
This is too bad.  
And this happened to us.  
This is why we have developed a "development environment" for `opentab`. This 
is how it works:
- There is a `Makefile` in the root of the repo.
- You can simply head to the root of the repo and type:
  ```
  make devel-up
  ```
  This way, it will setup a devel environment where you can do whatever you 
  want to the workspace. You can even destroy it! Your precious `tabs.yaml`
  original file will **not** be touched.  
  You may wonder how it works. It is really simple: what the command does is:
  - It will check for the existence of a directory: `~/.opentab/devel`.
  - If the directory exists:
    - Devel environment is up.
  - Else:
    - Create the directory.
    - Initialize a `tabs.yaml` devel file.  
  Now, every time you will launch an opentab command, it will refer to that 
  `tabs.yaml` file instead of the original one. This is done by dynamically 
  locating the `tabs.yaml` file when calling `opentab`:  
  it will check whether the `~/.opentab/devel` directory exists. If it exists,
  the variable that is used to determine the `tabs.yaml` location refers to 
  that file.
- When you are done developing, remember to switch back to the normal file.
  You can do this by simply going to the root of the repo and type:
  ```
  make devel-down
  ```
  This will switch your `opentab` configuration back to the original `tabs.yaml`
  file.