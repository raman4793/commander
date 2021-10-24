# Commander

## Basic usage

main.py

```python
from commander.commander import Command, CommandParser

command_parser = CommandParser(leading="--")
command = Command(command_parser=command_parser)


@command
class Calculator:

    def add(self, *, a, b):
        print(f"{a} + {b} = {a + b}")

    def subtract(self, *, a, b):
        print(f"{a} - {b} = {a - b}")

    def multiply(self, *, a, b):
        print(f"{a} * {b} = {a * b}")

    def divide(self, *, a, b):
        print(f"{a} / {b} = {a / b}")


@command
def say_hi(*, name):
    print(f"Hi, {name}")
    print("done")


if __name__ == '__main__':
    command.execute()
```

```shell
$ python main.py say_hi --name World!
$ python main.py calculator add --a 5 --b 6
$ python main.py calculator subtract --a 5 --b 6
$ python main.py calculator multiply --a 5 --b 6
$ python main.py calculator divide --a 5 --b 6
```