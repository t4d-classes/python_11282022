
def do_it() -> None:
    try:
        print("all is good")
        # raise Exception("some error occurred")

    except Exception as exc:

        print(f"exception: {exc}")
        return

    else:

        print("all worked out well")
        return

    finally:

        print("runs no matter what")


do_it()
