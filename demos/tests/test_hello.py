""" demo of standalone tests"""

import pytest

from demos.hello import hello, EmptyStringError


def test_hello_with_subject() -> None:
    """ test hello with a subject """
    assert hello("world") == "hello, world"


def test_hello_with_empty_subject() -> None:
    """ test hello with an empty subject """
    with pytest.raises(EmptyStringError):
        hello("")
