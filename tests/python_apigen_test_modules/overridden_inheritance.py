class A:
    """Class A docstring."""

    def foo(self) -> int:
        "Method foo docstring."
        pass


class _A(A):
    def bar(self) -> int:
        "Method bar docstring."
        pass


_A.__doc__ = A.__doc__
A = _A
