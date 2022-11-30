""" utils module """

from typing import Generator


def gen_entry_id() -> Generator[int, None, None]:
    """ gen entry id """
    counter = 0
    while True:
        counter = counter + 1
        yield counter
