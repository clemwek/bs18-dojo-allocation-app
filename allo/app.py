#!/usr/bin/env python
"""

Usage:
    dojo create_room (living|office) <room_name>...
    dojo add_person <person_name> ([<accommodation>])
    dojo print_room <room_name>
    dojo print_allocations [<filename>]
    dojo print_unallocated [<filename>]
    dojo reallocate_person <first_name> <last_name> <room_name>
    dojo load_people <file_name>
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
    def fn(self, arg):
        try:
            opt = docopt(fn.__doc__, arg)

        except DocoptExit as e:

            print('Invalid Command!')
            print(e)
            return

        except SystemExit:

            return

        return func(self, opt)

    fn.__name__ = func.__name__
    fn.__doc__ = func.__doc__
    fn.__dict__.update(func.__dict__)
    return fn


class App(cmd.Cmd):
    def intro():
        """This contains introductory message"""
        cprint(figlet_format("A11o", font="univers"), "blue")
        cprint(__doc__)

    intro = intro()
    prompt = '(A11o)'
    file = None

    @docopt_cmd
    def do_create_room(self, args):
        """
        Usage: 
             create_room <room_type> <room_name>...
        """
        room_info = args
        for room_name in room_info['<room_name>']:
            status = dojo.create_room(room_info['<room_type>'], room_name)
            print(status)

    @docopt_cmd
    def do_add_person(self, args):
        """
        Usage:
            add_person <first_name> <last_name> (fellow|staff) [<accommodation>]
        """
        person_info = args
        person_name = person_info['<first_name>'] + ' ' + person_info['<last_name>']
        if person_info['fellow']:
            person_type = 'fellow'
        if person_info['staff']:
            person_type = 'staff'
        if person_info['<accommodation>'] and person_info['<accommodation>'].lower() == 'y':
            accommodation = 'y'
        else:
            accommodation = None

        status = dojo.add_person(person_name, person_type, accommodation)
        print(status)

    @docopt_cmd
    def do_print_room(self, args):
        """
        Usage:
            add_person <room_name>
        """
        room_name = args['<room_name>'].lower()
        status = dojo.print_room(room_name)
        print(status)

    @docopt_cmd
    def do_print_allocations(self, args):
        """
        Usage: 
            print_allocations [<filename>]
        """
        filename = args['<filename>']
        status = dojo.print_allocations(filename)
        if status is not None:
            print(status)

    @docopt_cmd
    def do_print_unallocated(self, args):
        """
        Usage:
            print_unallocated [<filename>]
        """
        filename = args['<filename>']
        status = dojo.print_unallocated(filename)
        if status is not None:
            print(status)

    @docopt_cmd
    def do_reallocate_person(self, args):
        """
        :param args:
        Usage:
            reallocate_person <first_name> <last_name> <room_name>
        """
        persons_name = args['<first_name>'] + ' ' + args['<last_name>']
        room_name = args['<room_name>']
        status = dojo.reallocate_person(persons_name, room_name)
        if status is not None:
            print(status)

    @docopt_cmd
    def do_load_people(self, args):
        """
        Usage:
            load_people <file_name>
        """
        file_name = args['<file_name>']
        status = dojo.load_people(file_name)
        if status is not None:
            print(status)

    def do_quit(self, arg):
        """Quits out of Interactive Mode."""

        print('A11o : Good Bye!')

        exit()


opt = docopt(__doc__, sys.argv[1:])

if opt['--interactive']:
    App().cmdloop()

print(opt)
