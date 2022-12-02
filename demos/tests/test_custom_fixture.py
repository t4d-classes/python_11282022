""" test custom fixtures demos"""

# https://pylint.pycqa.org/en/latest/user_guide/checkers/features.html
# pylint: disable=unused-variable,redefined-outer-name

from typing import TypedDict
import pytest


class Person(TypedDict):
    """ person dictionary type hint """
    first_name: str
    last_name: str


TupleSamples = list[tuple[int, bool, str]]
ListSamples = list[list[int]]
DictSamples = list[Person]


@pytest.fixture
def tuple_samples() -> TupleSamples:
    """ tuple sample data for tests """
    return [
        (1, True, "bob"),
        (1, True, "bob"),
        (1, True, "sally")
    ]


@pytest.fixture
def list_samples() -> ListSamples:
    """ list sample data for tests """
    return [
        [1, 2, 3, 4],
        [1, 2, 3, 4],
        [5, 6, 7, 8]
    ]


@pytest.fixture
def dict_samples() -> DictSamples:
    """ dictionary sample data for tests """
    return [
        {"first_name": "Bob", "last_name": "Smith"},
        {"first_name": "Bob", "last_name": "Smith"},
        {"first_name": "Sally", "last_name": "Smith"}
    ]


class TestSequenceTypes:
    """ test suite for sequence types """

    def test_assert_tuple_contents(self, tuple_samples: TupleSamples) -> None:
        """ assert the contents of tuples """

        tuple_1, tuple_2, tuple_3 = tuple_samples

        assert tuple_1 == tuple_2
        # assert tuple_1 == tuple_3

    def test_assert_tuple_identity(self, tuple_samples: TupleSamples) -> None:
        """ assert the identity of tuples """

        tuple_1, tuple_2, tuple_3 = tuple_samples

        assert id(tuple_1) == id(tuple_1)
        # assert id(tuple_1) == id(tuple_2)

    def test_assert_list_contents(self, list_samples: TupleSamples) -> None:
        """ assert the contents of lists """

        list_1, list_2, list_3 = list_samples

        assert list_1 == list_2
        # assert list_1 == list_3

    def test_assert_list_identity(self, list_samples: TupleSamples) -> None:
        """ assert the identity of lists """

        list_1, list_2, list_3 = list_samples

        assert id(list_1) == id(list_1)
        # assert id(list_1) == id(list_2)


class TestMappingTypes:
    """ test suite for mapping types """

    def test_assert_dict_contents(self, dict_samples: DictSamples) -> None:
        """ assert the contents of dictionaries """

        dict_1, dict_2, dict_3 = dict_samples

        assert dict_1 == dict_2
        # assert dict_1 == dict_3

    def test_assert_dict_identity(self, dict_samples: DictSamples) -> None:
        """ assert the identities of dictionaries """

        dict_1, dict_2, dict_3 = dict_samples

        assert id(dict_1) == id(dict_1)
        # assert id(dict_1) == id(dict_2)
