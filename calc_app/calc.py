""" calc """

from typing import Any


def calc_app(title: str) -> None:
    """ calc app function """

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
                    "id": len(history) + 1,
                    "name": "add",
                    "value": operand
                }
                history.append(history_entry)
            case "subtract":
                operand = float(input("Enter a number > "))
                result = result - operand
                print(f"Result: {result}")
                history_entry = {
                    "id": len(history) + 1,
                    "name": "subtract",
                    "value": operand
                }
                history.append(history_entry)
            case "multiply":
                operand = float(input("Enter a number > "))
                result = result * operand
                print(f"Result: {result}")
                history_entry = {
                    "id": len(history) + 1,
                    "name": "multiply",
                    "value": operand
                }
                history.append(history_entry)
            case "divide":
                operand = float(input("Enter a number > "))
                result = result / operand
                print(f"Result: {result}")
                history_entry = {
                    "id": len(history) + 1,
                    "name": "divide",
                    "value": operand
                }
                history.append(history_entry)
            case "exponent":
                operand = float(input("Enter a number > "))
                result = result ** operand
                print(f"Result: {result}")
                history_entry = {
                    "id": len(history) + 1,
                    "name": "exponent",
                    "value": operand
                }
                history.append(history_entry)
            case "history":
                print(history)
            case "exit":
                break
            case "clear":
                result = 0
                print(f"Result: {result}")
            case _:
                print("Invalid command. Please try again.")

        command = input("Enter a command > ")


print(f"calc.py __name__: {__name__}")

if __name__ == "__main__":

    calc_app("Ran Calc App from calc.py")
