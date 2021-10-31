from commander.commander import Command, CommandParser, CommandValidator, ArgumentCaster
from commander.signature_reader import SignatureReader, TypeMap


class CommandBuilder:
    @staticmethod
    def build(leading="--"):
        command_parser = CommandParser(leading=leading)
        signature_reader_object = SignatureReader()
        type_map = TypeMap()

        argument_caster = ArgumentCaster(signature_reader=signature_reader_object, type_map=type_map)

        command_validator = CommandValidator(signature_reader=signature_reader_object)

        command = Command(command_parser=command_parser, command_validator=command_validator,
                          argument_caster=argument_caster)

        return command
        
