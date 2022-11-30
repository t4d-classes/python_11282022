""" history entry module """


class HistoryEntry:
    """ history entry class """

    def __init__(self, entry_id: int, op_name: str, op_value: float):
        self.entry_id = entry_id
        self.op_name = op_name
        self.op_value = op_value
