""" calc """

from typing import Any, Generator


def input_operand() -> float:
    return float(input("Enter a number > "))


def output_result(result: float) -> None:
    print(f"Result: {result}")


def gen_entry_id():
    counter = 0
    while True:
        counter = counter + 1
        yield counter


calc_ops = {
    "add": lambda a, b: a + b,
    "sub": lambda a, b: a - b,
    "mul": lambda a, b: a * b,
    "div": lambda a, b: a / b,
    "exp": lambda a, b: a ** b
}


def calc_result(history: list[Any]) -> float:
    """ calc result """
    result = 0
    for entry in history:
        # op_name = entry["name"]
        # op_func = calc_ops[op_name]
        # result = op_func(result, entry["value"])
        result = calc_ops[entry["name"]](result, entry["value"])
    return result


def append_history(
        history: list[Any],
        entry_id: Generator[int, None, None],
        op_name: str,
        op_value: float) -> None:
    """ append history """
    history_entry = {
        "id": next(entry_id),
        "name": op_name,
        "value": op_value
    }
    history.append(history_entry)


def calc_command(history, entry_id, op_name) -> None:
    """ calc command """
    operand = input_operand()
    append_history(history, entry_id, op_name, operand)
    output_result(calc_result(history))


def calc_app(title: str) -> None:
    """ calc app function """

    entry_id = gen_entry_id()
    history: list[Any] = []

    print(title)

    command = input("Enter a command > ")

    while True:

        match command:
            case "add":
                calc_command(history, entry_id, "add")
            case "subtract":
                calc_command(history, entry_id, "sub")
            case "multiply":
                calc_command(history, entry_id, "mul")
            case "divide":
                calc_command(history, entry_id, "div")
            case "exponent":
                calc_command(history, entry_id, "exp")
            case "history":
                for history_entry in history:
                    print((
                        f"{history_entry['id']}, "
                        f"{history_entry['name']}, "
                        f"{history_entry['value']}"
                    ))
            case "remove":
                entry_id = int(input("Please enter a history entry id: "))
                for history_entry in history:
                    if history_entry["id"] == entry_id:
                        history.remove(history_entry)
            case "exit":
                break
            case "clear":
                result = 0
                history = []
                print(f"Result: {result}")
            case _:
                print("Invalid command. Please try again.")

        command = input("Enter a command > ")


print(f"calc.py __name__: {__name__}")

if __name__ == "__main__":

    calc_app("Ran Calc App from calc.py")
