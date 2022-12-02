""" calc app main """

import asyncio

from calc_app.calc import Calculator


if __name__ == "__main__":

    calculator = Calculator("My Calculator")
    asyncio.run(calculator.run())
