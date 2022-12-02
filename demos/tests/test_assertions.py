""" test assertion demos"""

# autopep8: off
# https://pylint.pycqa.org/en/latest/user_guide/checkers/features.html
# pylint: disable=unused-variable,comparison-with-itself,comparison-of-constants
# pylint: disable=too-few-public-methods,singleton-comparison
# autopep8: on

from demos.hello import WebServerConfig


class TestBooleanTypes:
    """ assert demos for boolean types """

    def test_assert_boolean(self) -> None:
        """ assert demo for boolean """
        # autopep8: off
        assert True == True
        # assert True == False
        # autopep8: on


class TestNumericTypes:
    """ assert demos for numeric types """

    def test_assert_int(self) -> None:
        """ assert demo for int """
        assert 1 == 1
        # assert 1 == 2

    def test_assert_float(self) -> None:
        """ assert demo for float """
        assert 1.0 == 1.0
        # assert 1.0 == 2.0

    def test_assert_int_and_float(self) -> None:
        """ assert demo for int and float """
        assert 1 == 1.0
        # assert 1 == 2.0


class TestTextSequenceTypes:
    """ assert demos for text sequence types """

    def test_assert_string(self) -> None:
        """ assert demo for string """

        assert "bob" == "bob"
        # assert "bob" == "BOB"


class TestSequenceTypes:
    """ assert demos for sequence types """

    def test_assert_tuple_contents(self) -> None:
        """ assert the contents of tuples """

        tuple_1 = (1, True, "bob")
        tuple_2 = (1, True, "bob")
        tuple_3 = (1, True, "sally")

        assert tuple_1 == tuple_2
        # assert tuple_1 == tuple_3

    def test_assert_tuple_identity(self) -> None:
        """ assert the identity of tuples """

        tuple_1 = (1, True, "bob")
        tuple_2 = (1, True, "bob")
        tuple_3 = (1, True, "sally")

        assert id(tuple_1) == id(tuple_1)
        # assert id(tuple_1) == id(tuple_2)

    def test_assert_list_contents(self) -> None:
        """ assert the contents of lists """

        list_1 = [1, 2, 3, 4]
        list_2 = [1, 2, 3, 4]
        list_3 = [5, 6, 7, 8]

        assert list_1 == list_2
        # assert list_1 == list_3

    def test_assert_list_identity(self) -> None:
        """ assert the identity of lists """

        list_1 = [1, 2, 3, 4]
        list_2 = [1, 2, 3, 4]
        list_3 = [5, 6, 7, 8]

        # assert id(list_1) == id(list_1)
        assert id(list_1) == id(list_2)


class TestMappingTypes:
    """ assert demos for mapping types """

    def test_assert_dict_contents(self) -> None:
        """ assert the contents of dictionaries """

        dict_1 = {"first_name": "Bob", "last_name": "Smith"}
        dict_2 = {"first_name": "Bob", "last_name": "Smith"}
        dict_3 = {"first_name": "Sally", "last_name": "Smith"}

        assert dict_1 == dict_2
        # assert dict_1 == dict_3

    def test_assert_dict_identity(self) -> None:
        """ assert the identities of dictionaries """

        dict_1 = {"first_name": "Bob", "last_name": "Smith"}
        dict_2 = {"first_name": "Bob", "last_name": "Smith"}
        dict_3 = {"first_name": "Sally", "last_name": "Smith"}

        assert id(dict_1) == id(dict_1)
        # assert id(dict_1) == id(dict_2)


class TestCustomClass:
    """ assert demos for a custom class """

    def test_assert_custom_class_contents(self) -> None:
        """ assert custom class contents """

        web_server_config_1 = WebServerConfig("localhost", 8080)
        web_server_config_2 = WebServerConfig("localhost", 8080)

        assert web_server_config_1 == web_server_config_2
        # assert web_server_config_1.__dict__ == web_server_config_2.__dict__
