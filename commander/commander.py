import sys

from patterns import Singleton


class CommandParser:
    def __init__(self, leading="--"):
        self.leading = leading

    def parse_arguments(self):
        command_name = self.get_command_name()
        subcommand_name = self.get_subcommand_name()
        arguments = self.get_arguments()
        return command_name, subcommand_name, arguments

    def get_command_name(self):
        command_name = sys.argv[1]
        if self.is_argument(command_name):
            raise Exception("Please provide command name before arguments")
        else:
            return command_name

    def get_subcommand_name(self):
        subcommand_name = sys.argv[2]
        if self.is_argument(subcommand_name):
            return None
        return subcommand_name

    def get_arguments(self):
        if self.is_argument(name=sys.argv[2]):
            arguments = sys.argv[2:]
        else:
            arguments = sys.argv[3:]
        return {arguments[i].strip(self.leading): arguments[i + 1] for i in range(0, len(arguments), 2)}

    def is_argument(self, name):
        return name.startswith(self.leading)


class Command(Singleton):
    def __init__(self, command_parser):
        self.callable_store = {}
        self.class_store = {}
        self.command_parser = command_parser

    def __call__(self, reference):
        name = self._command_name_from_reference(reference)
        if type(reference) is not type:
            if name not in self.callable_store.keys():
                self.callable_store[name] = reference
            else:
                raise Exception("Found duplicate command.")
        else:
            if name not in self.class_store.keys():
                self.class_store[name] = reference()
            else:
                raise Exception("Found duplicate command.")

    @staticmethod
    def _command_name_from_reference(reference):
        return reference.__name__.lower()

    def execute(self):
        command_name, subcommand_name, arguments = self.command_parser.parse_arguments()
        try:
            result = self._execute(command_name, subcommand_name, **arguments)
        except TypeError:
            result = None
            print(self.get_command_reference_from_store(command_name, subcommand_name).__doc__)
        return result

    def _execute(self, command, subcommand, **kwargs):
        command_reference = self.get_command_reference_from_store(command, subcommand)
        return command_reference(**kwargs)

    def get_command_reference_from_store(self, command_name, subcommand):
        if command_name in self.callable_store.keys():
            reference = self.callable_store[command_name]
        elif command_name in self.class_store.keys():
            reference = getattr(self.class_store[command_name], subcommand)
        else:
            raise Exception("Invalid command")
        return reference
