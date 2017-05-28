====
allo
====


This is a command line program in python, made for andela boot camp week 2 project


Description
===========


When a new Fellow joins Andela they are assigned an office space and an optional living space if they choose to opt in. When a new Staff joins they are assigned an office space only. In this exercise I am digitize and randomize a room allocation system for one of Andela Kenya’s facilities called The Dojo.

Getting Started
===============

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

Installing
----------

Make sure you have python installed in your system if not visit https://www.python.org/downloads/ and get a copy for your system

Clone the project 
    ``$ git clone https://github.com/clemwek/proja11o.git``

Change Directory into the project folder
    ``$ cd proja11o``

Create a virtual environment with Python
    ``$ virtualenv -p python3 <yourenvname>``

Activate the virtual environment
    ``$ source <yourenvname>/bin/activate``

Install the application's dependencies from requirements.txt to the virtual environment
    ``$ pip install -r requirements.txt``

Install the app in the virtual environment
    ``$ python setup.py install``

Run the tool in interactive mode
    ``$ a11o -i``

Usage:
::
    dojo create_room (living|office) <room_name>...
    dojo add_person <person_name> ([<accommodation>])
    dojo print_room <room_name>
    dojo print_allocations [<filename>]
    dojo print_unallocated [<filename>]
    dojo (-i | --interactive)
    dojo (-h | --help | --version)

Options:
    -i, --interactive  Interactive Mode
    -h, --help  Show this screen and exit.

    
    


Note
====

This project has been set up using PyScaffold 2.5.7. For details and usage
information on PyScaffold see http://pyscaffold.readthedocs.org/.
