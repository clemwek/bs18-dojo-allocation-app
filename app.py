#!/usr/bin/env python
"""

Usage:
    dojo create_room (living|office) <room_name>...
    dojo add_person <person_name> ([accommodation])
    dojo print_room <room_name>
    dojo (-i | --interactive)
    dojo (-h | --help | --version)
Options:
    -i, --interactive  Interactive Mode
    -h, --help  Show this screen and exit.
"""

import cmd

import sys
from docopt import DocoptExit, docopt
from pyfiglet import figlet_format
from termcolor import cprint

from allo.allo import Dojo

dojo = Dojo()



def docopt_cmd(func):
    """
    This decorator is used to simplify the try/except block and pass the result
    of the docopt parsing to the called action.
    """
    def fn(self, arg):
        try:
            opt = docopt(fn.__doc__, arg)

        except DocoptExit as e:
            # The DocoptExit is thrown when the args do not match.
            # We print a message to the user and the usage block.

            print('Invalid Command!')
            print(e)
            return

        except SystemExit:
            # The SystemExit exception prints the usage for --help
            # We do not need to do the print here.

            return

        return func(self, opt)

    fn.__name__ = func.__name__
    fn.__doc__ = func.__doc__
    fn.__dict__.update(func.__dict__)
    return fn


class App(cmd.Cmd):
    def intro():
        """This contains introductory message"""
        cprint(figlet_format("dojo", font="univers"), "blue")
        cprint(__doc__)

    intro = intro()
    prompt = '(dojo)'
    file = None

    @docopt_cmd
    def do_create_room(self, args):
        """
        Usage: 
             create_room <room_type> <room_name>...
        """
        # try:
        #     room_info = docopt(self.do_create_room.__doc__, args)
        #     print(room_info)
        # except DocoptExit as e:
        #     print(e)


        print(args)
        for room_name in room_info['<room_name>']:
            status = self.dojo.create_room(room_info['<room_type>'], room_name)
            print(status)

    @docopt_cmd
    def do_add_person(self, args):
        """
        Usage:
            add_person <person_name> (fellow|staff) [accomodation]
        """
        # try:
        #     persons_info = docopt(self.do_add_person.__doc__, args)
        #     print(persons_info)
        # except DocoptExit as e:
        #     print(e)
        # print(args)
        # self.dojo.add_person()

    def do_quit(self, arg):
        """Quits out of Interactive Mode."""

        print('Good Bye!')

        exit()


opt = docopt(__doc__, sys.argv[1:])

if opt['--interactive']:
    App().cmdloop()

print(opt)