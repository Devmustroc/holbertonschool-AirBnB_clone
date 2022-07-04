#!/usr/bin/python3
"""This is the Air bnb clone Console. It works to navigate the
    Airbnb environmet.
    Much like a shell.
"""
import cmd
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from models.engine.file_storage import FileStorage
from models import storage


class HBNBCommand(cmd.Cmd):
    """Base Command file class"""

    prompt = "(hbnb) "
    classes = {"BaseModel": BaseModel, "User": User, "City": City,
               "Place": Place, "Amenity": Amenity, "Review": Review,
               "State": State}

    def do_EOF(self, line):
        """
        EOF force closes the console.
        """
        exit()

    def do_quit(self, line):
        """Quit command to exit the program"""
        exit()

    def emptyline(self):
        """ Does nothing on (empty line + "Enter") """
        pass

    def do_create(self, arg):
        """ Method to print instance """
        if len(arg) == 0:
            print("** class name missing **")
            return
        new = None
        if arg:
            arg_list = arg.split()
            if len(arg_list) == 1:
                if arg in self.classes.keys():
                    new = self.classes[arg]()
                    new.save()
                    print(new.id)
                else:
                    print("** class doesn't exist **")

    def do_show(self, arg):
        """ Method to print instance """
        if len(arg) == 0:
            print("** class name missing **")
            return
        elif arg.split()[0] not in self.classes:
            print("** class doesn't exist **")
            return
        elif len(arg.split()) > 1:
            key = arg.split()[0] + "." + arg.split()[1]
            if key in storage.all():
                pri = storage.all()
                print(pri[key])
            else:
                print("** no instance found **")
        else:
            print("** instance id missing **")

    def do_destroy(self, arg):
        """ Method to delete instance with class and id """
        arg_list = arg.split()
        if len(arg_list) == 0:
            print("** class name missing **")
        elif arg_list[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        if len(arg_list) == 1:
            print("** instance id missing **")
            return
        if len(arg_list) > 1:
            key = arg_list[0] + '.' + arg_list[1]
            if key in storage.all():
                storage.all().pop(key)
                storage.save()
            else:
                print("** no instance found **")
                return

    def do_all(self, arg):
        """Method to Prints string represention
            of all instances of a given class
        """
        if not arg:
            print("** class name missing **")
            return
        arg_list = arg.split()
        if arg_list not in HBNBCommand.classes:
            print("** class doesn't exist **")
        else:
            all_obj = storage.all()
            new_List = []

            for key, value in all_obj.items():
                obj_name = value.__class__.__name__
                if obj_name == arg_list[0]:
                    new_List = new_List + [value.__str__()]
            print(new_List)

    def do_update(self, arg):
        """ Method to update JSON file"""
        arg = arg.split()
        if len(arg) == 0:
            print('** class name missing **')
            return
        elif arg[0] not in self.classes:
            print("** class doesn't exist **")
            return
        elif len(arg) == 1:
            print('** instance id missing **')
            return
        else:
            key = arg[0] + '.' + arg[1]
            if key in storage.all():
                if len(arg) > 2:
                    if len(arg) == 3:
                        print('** value missing **')
                    else:
                        setattr(
                            storage.all()[key],
                            arg[2],
                            arg[3][1:-1])
                        storage.all()[key].save()
                else:
                    print('** attribute name missing **')
            else:
                print('** no instance found **')


if __name__ == "__main__":
    HBNBCommand().cmdloop()
