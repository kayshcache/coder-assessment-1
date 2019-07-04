# Lacerater - Terminal Application
## Statement of Purpose & Scope
###### 300 - 500 words:
###### Describe - what the app will do.
This app, dubbed Lacerater, will use HTTP Request methods to acquire data and information from any website. It runs only in the terminal, in that the only interface is the command line arguments, flags, and options. It will produce output to the terminal window that can be piped to other apps or methods in the terminal as well as produce an output file if the user includes that option when the command is run. 
It is designed to be simple and in future versions extensible.
The thing to know about this app is that it is actually just a phony hacker tool and it is designed to look like it does something impressive.
##### Identify - the problem it will solve
It will automate some of the most rudimentary browser-based inspection and information gathering techniques of ethical hackers during their initial analysis of a web application.
##### Identify - the target audience
Cyber security analysts who are working in the Unix terminal, grepping, 'vimming', and bashing data for reports with the intent of later performing deeper analysis of client web services. This is the statement of a hollywood audience. The most suitable audience for this app would be a filmmaker in need of things that are harmless to make hacking look cool in a dumb movie for an ignorant audience. LACERATE!
##### Explain - how a user will use it
## Features
##### 100 words each
- F1: User can provide URL with the lacerate command as an argument, making it possible to use this utility on any available HTTP GETable asset.
- F2: User can specify whether to output results to a file with an option flag. The app will produce a CSV link file using a semi-colon to delimit any multiple instances of an HTML tag or attribute.
- F3: User can choose what they want to *lacerate* from the website. For example, all links including the anchor and link text together. If no resource is found of the specified type, meta-tags from the head of the HTML document will be returned as default. Multiple lacerations can be produced with a single execution.
- additional features: native-Unix like running; light-weight and extensible; has a man page
## User Interaction & Experience
### Outline:
##### How the user will get instructions and help from the app
The "-h" flag can be added to the command to get the full help. Otherwise, _argparse_ module will produce helpful responses when the commands given by the user don't match the requirements or can be expanded to specify more accurate output.
##### How the user will interact and access the features
The user will write a single line command including all options and flags to get the required operation from those specified in the help page.
##### How will errors be handled and displayed
Exception errors will only be displayed to the user specifically if resources aren't found at the URL given or the user is experiencing internet connection problems. If resources are found at the specified URL but 
## Control Flow Diagram
![Figure 0.0 Control Flow Diagram](https://github.com/kayshcache/coder-assessment-1/raw/master/lacerater.png)
Note:
- show the workflow/logic and/or integration of the features in your application for each feature.  
- utilise a recognised format or set of conventions for a control flow diagram, such as UML.
## Implementation Plan
### Feature 1 - " "
Outline of how to implement
**5 minimum** Task breakdown (checklist)
Task priorities & deadlines
### Feature 2 - " "
Outline of how to implement
**5 minimum** Task breakdown (checklist)
Task priorities & deadlines
### Feature 3 - " "
Outline of how to implement
**5 minimum** Task breakdown (checklist)
Task priorities & deadlines
## Developer Log
[Please see development_log.md](src/development_log.md)
Please send your log to your educator as a markdown file as you complete them. This is so we can provide you with feedback.
## Help File
###### Steps to install
Install from source for Unix systems only
###### Dependencies
Python 3+
Modules from PyPI: Requests, Beautiful Soup, Argparse
###### System/hardware requirements
Minimum requirements 2gb RAM x86_64
###### Explanation of features
Get data from websites
Specify what information to scrape from a web page using flags

### Testing
An **outline** of the testing procedure and cases should be included with the source code of the application and written in markdown.
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTExNDAzMjcxNzEsMjA4MjM1MDc3NiwxNz
gwNzE4OTc2LC00MDg0NTU3MTAsMTc3NjkzODQyNCwtMTkyOTEy
NzQ0OCwtMjg5NTA5ODk1LC04Njk4ODc1MzYsLTE4MDkwMjY1MT
EsLTI1MzM0OTY3NiwxMTM4NjQ1MTExLDE1NzY5NzEyNTcsLTEx
NjYxMjQ3NTFdfQ==
-->