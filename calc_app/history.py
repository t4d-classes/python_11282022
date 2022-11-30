""" history module """

from calc_app.history_entry import HistoryEntry
from calc_app.utils import gen_entry_id


class History:
    """ history class """

    def __init__(self) -> None:
        self.__entry_id = gen_entry_id()
        self.__history_entries: list[HistoryEntry] = []

    def get_history_entries(self) -> list[HistoryEntry]:
        """ get history entries """
        # return [HistoryEntry(**entry.__dict__) for entry in
        # self.__history_entries]
        return self.__history_entries.copy()

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
