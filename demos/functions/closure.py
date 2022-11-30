
def do_something(fn):
    fn()


def do_it(x):
    print("do it: " + str(x))


def outer():

    t = 3

    # a_fn = lambda: do_it(t)
    def inner():
        do_it(t)

    def update(i: int) -> None:
        nonlocal t
        t = i

    return (inner, update)


inner_fn, update_fn = outer()

do_something(inner_fn)

update_fn(4)

do_something(inner_fn)
