""" test using a built-in fixture """


def test_temp_folder(tmp_path: str) -> None:
    """ get a temp folder using a built-in fixture """

    print(f"temp folder: {tmp_path}")

    assert True
