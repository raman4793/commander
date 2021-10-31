import inspect
from typing import Sequence


class SignatureReader:

    @classmethod
    def parameters(cls, method):
        return {**cls.required_parameters(method), **cls.optional_parameters(method)}

    @classmethod
    def _required_parameters(cls, method):
        parameters = cls.get_parameters(method)
        parameters = [parameter for parameter in parameters if parameter.default is inspect._empty]
        return parameters

    @classmethod
    def _optional_parameters(cls, method):
        parameters = cls.get_parameters(method)
        parameters = [parameter for parameter in parameters if parameter.default is not inspect._empty]
        return parameters

    @classmethod
    def _signature_map(cls, parameters: Sequence[inspect.Parameter]):
        parameters_type = {
            parameter.name: parameter.annotation.__name__ for parameter in parameters
        }
        return parameters_type

    @classmethod
    def required_parameters(cls, method):
        parameters = cls._required_parameters(method)
        parameters = cls._signature_map(parameters)
        return parameters

    @classmethod
    def optional_parameters(cls, method):
        parameters = cls._optional_parameters(method)
        parameters = cls._signature_map(parameters)
        return parameters

    @classmethod
    def get_parameters(cls, method):
        return inspect.signature(method).parameters.values()


class TypeMap:

    @staticmethod
    def get_type_object(type_name: str):
        return eval(type_name)
