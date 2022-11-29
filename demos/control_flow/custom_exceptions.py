import inspect


class CalcError(Exception):

    def __init__(self, op_name: str, op_value: float):
        self.op_name = op_name
        self.op_value = op_value

    # def __str__(self) -> str:
    #     return (
    #         f"Could not perform operation {self.op_name} "
    #         f"with value {self.op_value}"
    #     )

    def __repr__(self) -> str:
        return (
            f"Could not perform operation {self.op_name} "
            f"with value {self.op_value}"
        )


try:

    raise CalcError('add', 3)

except CalcError as calc_error:

    print(f"{calc_error}")
