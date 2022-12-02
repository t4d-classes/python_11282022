""" calc module """
from typing import Callable
import math

from calc_app.history import History
from calc_app.history_storage import HistoryTextStorage
from calc_app.input_output import (
    input_operand, output_result
)


class Calculator:
    """ calculator class """

    def __init__(self, title: str):
        self.title = title

        history_text_storage = HistoryTextStorage("history.txt")

        self.__history = History(storage=history_text_storage)

        self.calc_ops: dict[str, Callable[[float, float], float]] = {
            "add": lambda a, b: a + b,
            "sub": lambda a, b: a - b,
            "mul": lambda a, b: a * b,
            "div": lambda a, b: a / b,
            "exp": math.pow
        }

    def command_calc(self, op_name: str) -> None:
        """ calc command """
        operand = input_operand()
        self.__history.append_entry(op_name, operand)
        output_result(self.result)

    def command_history(self) -> None:
        """ command history """
        for history_entry in self.__history:
            print((
                f"{history_entry.entry_id}, "
                f"{history_entry.op_name}, "
                f"{history_entry.op_value}"
            ))

    def command_clear(self) -> None:
        """ command clear"""
        self.__history.clear_entries()

    def command_remove_entry(self) -> None:
        """ command remove entry """
        entry_id = int(input("Please enter a history entry id: "))
        self.__history.remove_entry(entry_id)

    async def command_load_history(self) -> None:
        """ command load history """
        await self.__history.load_history()

    async def command_save_history(self) -> None:
        """ command save history """
        await self.__history.save_history()

    @staticmethod
    def command_invalid() -> None:
        """ command invalid """
        print("Invalid command. Please try again.")

    @property
    def result(self) -> float:
        """ calc result """
        result = 0.0
        for entry in self.__history:
            result = self.calc_ops[entry.op_name](result, entry.op_value)
        return result

    async def run(self) -> None:
        """ run """

        print(self.title)

        command = input("Enter a command > ")

        while True:
            match command:
                case "add" | "sub" | "mul" | "div" | "exp":
                    self.command_calc(command)
                case "history":
                    self.command_history()
                case "remove":
                    self.command_remove_entry()
                case "load":
                    await self.command_load_history()
                case "save":
                    await self.command_save_history()
                case "clear":
                    self.command_clear()
                case "exit":
                    break
                case _:
                    self.command_invalid()

            command = input("Enter a command > ")
