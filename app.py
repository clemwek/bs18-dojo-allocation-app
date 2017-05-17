import cmd
from docopt import DocoptExit, docopt
from allo.allo import Dojo


class App(cmd.Cmd):
    def __init__(self):
        self.dojo = Dojo()
        cmd.Cmd.__init__(self)

    def do_create_room(self, args):
        """
        Usage: 
             create_room <room_type> <room_name>...
        """
        try:
            room_info = docopt(self.do_create_room.__doc__, args)
            print(room_info)
        except DocoptExit as e:
            print(e)


        print(args)
        for room_name in room_info['<room_name>']:
            status = self.dojo.create_room(room_info['<room_type>'], room_name)
            print(status)


if __name__ == "__main__":
    app = App()
    app.cmdloop()
