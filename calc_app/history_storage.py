

from abc import ABC, abstractmethod
import asyncio
import aiofiles

from calc_app.history_entry import HistoryEntry


class HistoryStorage(ABC):
    """ history storage contract """

    @abstractmethod
    async def load(self) -> list[HistoryEntry]:
        """ load history """
        pass

    @abstractmethod
    async def save(self, history_entries: list[HistoryEntry]) -> None:
        """ save history """
        pass


class HistoryTextStorage(HistoryStorage):
    """ history text storage """

    def __init__(self, file_name: str) -> None:
        self.file_name = file_name

    async def load(self) -> list[HistoryEntry]:
        """ load history """

        def from_csv_string(history_entry_csv_text: str) -> HistoryEntry:
            """ from csv string """
            entry_id, op_name, op_value = history_entry_csv_text.split(",")
            return HistoryEntry(int(entry_id), op_name, float(op_value))

        history_entries: list[HistoryEntry] = []

        async with aiofiles.open(
                self.file_name, "r", encoding="UTF-8") as history_file:
            async for history_entry_text in history_file:
                history_entries.append(
                    from_csv_string(history_entry_text))

        return history_entries

    async def save(self, history_entries: list[HistoryEntry]) -> None:
        """ save history """
        async with aiofiles.open(
                self.file_name, "w", encoding="UTF-8") as history_file:
            for history_entry in history_entries:
                await history_file.write((
                    f"{history_entry.entry_id},"
                    f"{history_entry.op_name},"
                    f"{history_entry.op_value}\n"
                ))
