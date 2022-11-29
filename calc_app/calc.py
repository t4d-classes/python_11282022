""" calc """

from typing import Any

# def get_next_id(history):
#     if not history:
#         return 1
#
#     return max([entry["id"] for entry in history]) + 1


def gen_entry_id():
    counter = 0
    while True:
        counter = counter + 1
        yield counter


def calc_app(title: str) -> None:
    """ calc app function """

    entry_id = gen_entry_id()
    result = 0.0
    history: list[Any] = []

    print(title)

    command = input("Enter a command > ")

    while True:

        match command:
            case "add":
                operand = float(input("Enter a number > "))
                result = result + operand
                print(f"Result: {result}")
                history_entry = {
                    "id": next(entry_id),
                    "name": "add",
                    "value": operand
                }
                history.append(history_entry)
            case "subtract":
                operand = float(input("Enter a number > "))
                result = result - operand
                print(f"Result: {result}")
                history_entry = {
                    "id": next(entry_id),
                    "name": "subtract",
                    "value": operand
                }
                history.append(history_entry)
            case "multiply":
                operand = float(input("Enter a number > "))
                result = result * operand
                print(f"Result: {result}")
                history_entry = {
                    "id": next(entry_id),
                    "name": "multiply",
                    "value": operand
                }
                history.append(history_entry)
            case "divide":
                operand = float(input("Enter a number > "))
                result = result / operand
                print(f"Result: {result}")
                history_entry = {
                    "id": next(entry_id),
                    "name": "divide",
                    "value": operand
                }
                history.append(history_entry)
            case "exponent":
                operand = float(input("Enter a number > "))
                result = result ** operand
                print(f"Result: {result}")
                history_entry = {
                    "id": next(entry_id),
                    "name": "exponent",
                    "value": operand
                }
                history.append(history_entry)
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
