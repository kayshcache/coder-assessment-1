# Lacerater - Terminal Application
## Statement of Purpose & Scope
###### 300 - 500 words:
###### Describe - what the app will do.
Lacerater uses HTTP Request methods to acquire data and information from websites. It runs only in the terminal, in that the only interface is the command line arguments, flags, and options. It will produce output to the terminal window that can be piped to other apps or methods in the terminal as well as produce an output file if the user includes that option when the command is run. 
It is designed to be simple and in future versions extensible.
##### Identify - the problem it will solve
It will automate some of the most rudimentary browser-based inspection and information gathering techniques of ethical hackers during their initial analysis of a web application. There are all together too few useless programs on github, this project will change the world and disrupt the industry in this way specifically.
##### Identify - the target audience
Cyber security analysts who are working in the Unix terminal, grepping, 'vimming', and bashing data for reports with the intent of later performing deeper analysis of client web services. The most suitable audience for this app would be a filmmaker in need of things that are harmless to make hacking look cool in a dumb movie for an ignorant audience. LACERATE!
##### Explain - how a user will use it
Type the command into the shell to see the basic help (eg. what arguments are required), then select your options and don't forget to include a URL to slice n dice.
## Features
##### 100 words each
- f1: User can provide URL with the `lacerate` command as an argument, making it possible to use this utility on any available HTTP GETable asset. This is a nice way to quickly acquire data from any server with a public address - users will be very enthralled by this feature, there will be joy jumping hackers across the globe.
- f2: User can specify whether to output results to a file with the option `--file`. The app will produce a generic binary file containing the data that was located at the specified URL. This state-of-the-art almost mystical level feature will be likely to excite even the most stoic web professional.
- f3: User can choose what they want to *lacerate* from the website. For example, all links including the anchor and link text together. If no resource is found of the specified type, meta-tags from the head of the HTML document will be returned as default. Multiple lacerations can be produced with a single execution.
- additional features: native-Unix like running; light-weight and extensible; has a man page
## User Interaction & Experience
### Outline:
##### How the user will get instructions and help from the app
The "-h" flag can be added to the command to get the full help. Otherwise, *argparse* and *requests* modules will produce helpful responses when the commands given by the user don't match the requirements or can be expanded to specify more accurate output.
##### How the user will interact and access the features
The user will write a single line command including all options and flags to get the required operation from those specified in the help page.
##### How will errors be handled and displayed
Exception errors will only be displayed to the user specifically if resources aren't found at the URL given or the user is experiencing internet connection problems. If resources are found at the specified URL but 
## Control Flow Diagram
![Figure 0.0 Control Flow Diagram](https://github.com/kayshcache/coder-assessment-1/raw/master/img/lacerater.png)
## Implementation Plan
Priority of tasks are marked with P0 - P2 with P0 to represent the highest priority being zero priority, in that it is indexed from zero (as all things should be by law). It may be that these task in fact have zero priority in the world as well.
Priority 1 tasks = P0, Priority 2 tasks = P1, Priority 3 tasks = P2
Time will take is written in square brackets
### Feature 1 - " Provide URL as Argument Feature"
- Task 1 (P1) write the argument into the main function [10 -30 minutes]
- Task 2 (P2) test it [10 -30 minutes]
- Task 3 (P0) try with funky URLs [10 -30 minutes]
- Task 4 (P2) think of additional tasks to describe here [1 minute]
- Task 5 (P0) describe those addition tasks such as aforementioned task ie. this task [10 -30 minutes]
### Feature 2 - " Output to file"
- Task 1 (P1) decide on what file type the user should create [10 -30 minutes]
- Task 2 (P1) write the argument into the main function [10 -30 minutes]
- Task 3 (P1) write the function to write binary files [1 hour]
- Task 4 (P0) hook function into argument flow control [10 -30 minutes]
- Task 5 (P2) dance a bit [all night]
### Feature 3 - " Choose from laceration options"
- Task 1 (P1) decide on total set of options [10 -30 minutes]
- Task 2 (P0) put those options into the control flow to be processed by argparse [1 hour]
- Task 3 (P2) think of cooler things to be doing than describing task breakdowns [10 -30 minutes]
- Task 4 (P0) get some sleep so to be able to do the graveyard shift at crappy hostel and not become homeless [countless hours]
- Task 5 (P2) feel shame about creating unprofessional documentation [lifetime]
### Spiffing Project Management
![See trello screen snip for fun](https://github.com/kayshcache/coder-assessment-1/raw/master/img/trello0.png)
![See trello screen snip for fun](https://github.com/kayshcache/coder-assessment-1/raw/master/img/trello1.png)
![See trello screen snip for fun](https://github.com/kayshcache/coder-assessment-1/raw/master/img/trello2.png)
## Developer Log
[Please see development_log.md](https://github.com/kayshcache/coder-assessment-1/raw/master/DEV_LOG.md)
## Help File
###### Steps to install
Install from source for Unix systems only
###### Dependencies
Python 3+
Modules from PyPI: Requests, Beautiful Soup, Argparse
###### System/hardware requirements
Minimum requirements: Python 3.4 128mb RAM x86_64, ARM, i386
###### Explanation of features
Get data from websites
Specify what information to get from a web page using flags

### Testing
Test file included, run pytest with shell from application directory.
<!--stackedit_data:
eyJoaXN0b3J5IjpbMjAyMzEyMDI3MywtMTY3OTIwMTU4OCwyMD
M5NDU2OTk5LDE3MzcyNDAzOTAsLTE3MzIzMzYxMTAsMzU5MzU5
NTMxLC0xNzYxNzkyMDMzLDU4OTU3NDc4MSwyMDgyMzUwNzc2LD
E3ODA3MTg5NzYsLTQwODQ1NTcxMCwxNzc2OTM4NDI0LC0xOTI5
MTI3NDQ4LC0yODk1MDk4OTUsLTg2OTg4NzUzNiwtMTgwOTAyNj
UxMSwtMjUzMzQ5Njc2LDExMzg2NDUxMTEsMTU3Njk3MTI1Nywt
MTE2NjEyNDc1MV19
-->