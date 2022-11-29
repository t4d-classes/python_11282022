

def do_it(*args, **kwargs):

    for arg in args:
        print(arg)
    for key in kwargs:
        print(f"{key}={kwargs[key]}")


do_it("hello", 1, 2, 3, msg2="mars", msg3="a", msg4="b")
