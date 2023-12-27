#!/usr/bin/python3


def raise_exception_msg(message=""):
    """ a function that raises a name exception with a message """

    try:
        raise exception(message)
    except Exception:
        print(message)
