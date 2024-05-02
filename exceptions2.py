
class ValueTooHighError(Exception):
    pass


class ValueTooSmallError(Exception):
    def __init__(self, message, value):
        self.message = message
        self.value = value


def test_value(x):
    if x > 100:
        raise ValueTooHighError("Value is too high.")
    if x < 5:
        raise ValueTooSmallError("value is too small.", x)


try:    # když použiju try, tak musím použít except
    test_value(2)
except ValueTooHighError as e:
    print(e)
except ValueTooSmallError as e:
    print(f"{e.value} {e.message}")
else:
    print("Everything is fine.")
