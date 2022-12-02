""" history module """
from typing import Iterator
from calc_app.history_entry import HistoryEntry
from calc_app.utils import gen_entry_id
from calc_app.history_storage import HistoryStorage


class History:
    """ history class """

    def __init__(self, storage: HistoryStorage) -> None:
        self.__entry_id = gen_entry_id()
        self.__history_entries: list[HistoryEntry] = []
        self.__storage = storage

    def __iter__(self) -> Iterator[HistoryEntry]:
        self.__current_iter = iter(self.__history_entries)
        return self.__current_iter

    def __next__(self) -> HistoryEntry:
        return next(self.__current_iter)

    # @property
    # def history_entries(self) -> list[HistoryEntry]:
    #     """ get history entries """
    #     # return [HistoryEntry(**entry.__dict__) for entry in
    #     # self.__history_entries]
    #     return self.__history_entries.copy()

    def append_entry(
            self,
            op_name: str, op_value: float) -> None:
        """ append entry """
        self.__history_entries.append(
            HistoryEntry(next(self.__entry_id), op_name, op_value))

    def remove_entry(self, entry_id: int) -> None:
        """ remove entry """
        for history_entry in self.__history_entries:
            if history_entry.entry_id == entry_id:
                self.__history_entries.remove(history_entry)

    def clear_entries(self) -> None:
        """ clear entries """
        self.__history_entries = []

    async def load_history(self) -> None:
        self.__history_entries = await self.__storage.load()

    async def save_history(self) -> None:
        await self.__storage.save(self.__history_entries)
