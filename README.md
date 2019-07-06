# Lacerater - Terminal Application
## Statement of Purpose & Scope
###### 300 - 500 words:
###### Describe - what the app will do.
Lacerater uses HTTP Request methods to acquire data and information from websites. It runs only in the terminal, in that the only interface is the command line arguments, flags, and options. It will produce output to the terminal window that can be piped to other apps or methods in the terminal as well as produce an output file if the user includes that option when the command is run. 
It is designed to be simple and in future versions extensible.
##### Identify - the problem it will solve
It will automate some of the most rudimentary browser-based inspection and information gathering techniques of ethical hackers during their initial analysis of a web application.
##### Identify - the target audience
Cyber security analysts who are working in the Unix terminal, grepping, 'vimming', and bashing data for reports with the intent of later performing deeper analysis of client web services. The most suitable audience for this app would be a filmmaker in need of things that are harmless to make hacking look cool in a dumb movie for an ignorant audience. LACERATE!
##### Explain - how a user will use it
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
Priority 1 tasks = P0, Priority 2 tasks = P1, Priority 3 tasks = P2
### Feature 1 - " "
Provide URL as Argument Feature
### Feature 2 - " "
Outline of how to implement
**5 minimum** Task breakdown (checklist)
Task priorities & deadlines
### Feature 3 - " "
Outline of how to implement
**5 minimum** Task breakdown (checklist)
Task priorities & deadlines
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
Specify what information to scrape from a web page using flags

### Testing
Test file included, run pytest from application directory.
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTE3MzIzMzYxMTAsMzU5MzU5NTMxLC0xNz
YxNzkyMDMzLDU4OTU3NDc4MSwyMDgyMzUwNzc2LDE3ODA3MTg5
NzYsLTQwODQ1NTcxMCwxNzc2OTM4NDI0LC0xOTI5MTI3NDQ4LC
0yODk1MDk4OTUsLTg2OTg4NzUzNiwtMTgwOTAyNjUxMSwtMjUz
MzQ5Njc2LDExMzg2NDUxMTEsMTU3Njk3MTI1NywtMTE2NjEyND
c1MV19
-->