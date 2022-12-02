""" test monkey patch environment variables """

from typing import Any
from pathlib import Path
import pytest


from demos.hello import WebServerConfig, read_web_server_config
import demos.hello

YAML_CONFIG = """server:
  host: localhost
  port: 8080"""


@pytest.fixture
def print_path_mock(monkeypatch: Any, mocker: Any) -> None:
    """ create a mocks for testing print_path """
    monkeypatch.setenv("PATH", "/some/fake/path")
    mocker.patch('demos.hello.print')
    return mocker.spy(demos.hello, 'print')


def test_print_path(print_path_mock: Any) -> None:
    """ test the print path function """
    demos.hello.print_path()
    assert print_path_mock.call_count == 1
    print_path_mock.assert_called_once_with("/some/fake/path")


@pytest.fixture
def demos_hello_open_mock(monkeypatch: Any, mocker: Any) -> Any:
    hello_open_mock = mocker.mock_open(read_data=YAML_CONFIG)
    return mocker.patch("demos.hello.open", hello_open_mock)


def test_read_web_server_config(demos_hello_open_mock):

    web_server_config = read_web_server_config(
        Path("/some/fake/path/fake_file.yml"))

    demos_hello_open_mock.assert_called_once_with(
        Path("/some/fake/path/fake_file.yml"), "r", encoding="UTF-8"
    )
    assert web_server_config.server_name == "localhost:8080"
