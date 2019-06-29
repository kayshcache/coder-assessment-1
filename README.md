# Lacerater - Terminal Application
## Statement of Purpose & Scope
###### 300 - 500 words:
###### Describe - what the app will do.
This app, dubbed Lacerater, will use HTTP Request methods to acquire data and information from any website. It runs only in the terminal, in that the only interface is the command line arguments, flags, and options. It will produce output to the terminal window that can be piped to other apps or methods in the terminal as well as produce an output file if the user includes that option when the command is run. 
It is designed to be simple and in future branches extensible.
##### Identify - the problem it will solve
It will automate some of the most rudimentary browser-based inspection and information gathering techniques of ethical hackers during their initial analysis of a web application.
##### Identify - the target audience
Cyber security analysts who are working in the Unix terminal, grepping, vimming, and bashing data for reports with the intent of later performing deeper analysis of client web services.
##### Explain - how a user will use it
## Features
100 words each
- feature 1: User can provide URL with the lacerate command as an argument, making it possible to use this utility on any available HTTP asset.
- feature 2: User can specify whether to output results to a file with an option flag.
- feature 3: User can choose what they want to 'lacerate' from the website. For example, all links including the anchor and 
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
![Figure 1.1 Control Flow Diagram](diagram.png)
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
#### Steps to install
#### Dependencies
#### System/hardware requirements
#### Explanation of features
### Testing

<!--stackedit_data:
eyJoaXN0b3J5IjpbLTExMDM2MjMwMDQsMTc3NjkzODQyNCwtMT
kyOTEyNzQ0OCwtMjg5NTA5ODk1LC04Njk4ODc1MzYsLTE4MDkw
MjY1MTEsLTI1MzM0OTY3NiwxMTM4NjQ1MTExLDE1NzY5NzEyNT
csLTExNjYxMjQ3NTFdfQ==
-->