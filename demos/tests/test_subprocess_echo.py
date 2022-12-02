import subprocess
import pathlib
import os


def test_echo_return_code() -> None:
    print(os.path.dirname(__file__))

    working_folder = pathlib.Path(
        os.path.dirname(__file__), "..", "subprocesses")
    result = subprocess.run(
        ["python", "echo.py", "some message"], cwd=working_folder)

    assert result.returncode == 0


def test_echo_stdout() -> None:

    message = "some message"

    working_folder = pathlib.Path(
        os.path.dirname(__file__), "..", "subprocesses")
    result = subprocess.run(
        ["python", "echo.py", message], cwd=working_folder, capture_output=True)

    assert result.returncode == 0

    assert result.stdout.decode("UTF-8").strip() == message


def test_echo_stderr() -> None:

    working_folder = pathlib.Path(
        os.path.dirname(__file__), "..", "subprocesses")
    result = subprocess.run(
        ["python", "echo.py"], cwd=working_folder, capture_output=True)

    assert result.returncode == 1

    assert result.stderr.decode(
        "UTF-8").strip().find("IndexError: list index out of range") > -1
