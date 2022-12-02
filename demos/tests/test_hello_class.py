""" demo of test suite """

import pytest

from demos.hello import hello, EmptyStringError


class TestHello:
    """ test suite for hello tests """

    def test_hello_with_subject(self) -> None:
        """ test hello with a subject """
        assert hello("world") == "hello, world"

    def test_hello_with_empty_subject(self) -> None:
        """ test hello with an empty subject """
        with pytest.raises(EmptyStringError):
            hello("")
