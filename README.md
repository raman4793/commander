# Commander

## Basic usage

main.py

```python
from commander import CommandBuilder

command = CommandBuilder.build()


@command
class Calculator:

    def add(self, *, a: int, b: int = 5):
        print(f"{a} + {b} = {a + b}")

    def subtract(self, *, a: int, b: int):
        print(f"{a} - {b} = {a - b}")

    def multiply(self, *, a: int, b: int):
        print(f"{a} * {b} = {a * b}")

    def divide(self, *, a: int, b: int):
        print(f"{a} / {b} = {a / b}")


@command
def test(*, a: int, b: int):
    print(f"{a} + {b} = {a + b}")
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
## TODO : Autogenerate help from docstring
