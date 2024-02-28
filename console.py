#!/usr/bin/python3

import cmd
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        print()
        return True

    def emptyline(self):
        """Do nothing on empty input"""
        pass

    def do_create(self, arg):
        """Create a new instance of BaseModel"""
        if not arg:
            print("** class name missing **")
        elif arg not in "BaseModel":
            print("** class doesn't exist **")
        else:
            new_instance = BaseModel()
            new_instance.save()
            print(new_instance.id)

    def do_show(self, arg):
        """Prints the string representation of an instance"""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        elif args[0] not in ["BaseModel"]:
            print("** class doesn't exist **")
            return
        elif len(args) == 1:
            print("** instance id missing **")
            return

        key = "{}.{}".format(args[0], args[1])
        all_objects = storage.all()
        if key in all_objects:
            print(all_objects[key])
        else:
            print("** no instance found **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        elif args[0] not in ["BaseModel"]:
            print("** class doesn't exist **")
            return
        elif len(args) == 1:
            print("** instance id missing **")
            return
        else:
            key = "{}.{}".format(args[0], args[1])
            all_objects = storage.all()
            if key in all_objects:
                del all_objects[key]
                storage.save()
            else:
                print("** no instance found **")

    def do_all(self, arg):
        """Prints all string representations of all instances"""
        objects_list = []

        if arg:
            if arg not in ["BaseModel"]:
                print("** class doesn't exist **")
                return

        for key, value in storage.all().items():
            if arg is None or value.__class__.__name__ == arg:
                objects_list.append(str(value))

        print(objects_list)

    def do_update(self, arg):
        """Updates an instance based on the class name and id"""
        args = arg.split()
        all_objects = storage.all()

        if len(args) == 0:
            print("** class name missing **")
            return
        elif args[0] not in ["BaseModel"]:
            print("** class doesn't exist **")
            return
        elif len(args) == 1:
            print("** instance id missing **")
            return
        elif len(args) == 2:
            print("** attribute name missing **")
            return
        elif len(args) == 3:
            print("** value missing **")
            return
        else:

            key = "{}.{}".format(args[0], args[1])
            if key not in all_objects:
                print("** no instance found **")
                return

            instance = all_objects[key]
            attribute_name = args[2]
            attribute_value = args[3]

            if hasattr(instance, attribute_name):
                setattr(instance, attribute_name, eval(attribute_value))
                instance.save()
            else:
                print("** attribute doesn't exist **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
