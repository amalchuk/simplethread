# -*- coding: utf-8 -*-

from simplethread.decorators import synchronized
from simplethread.decorators import threaded


def multiply(a: float, b: float) -> float:
    return a * b


def test_synchronized() -> None:
    initial_value: int = 5
    decorated = synchronized(multiply)
    assert decorated(initial_value, 3) == 15


def test_threaded() -> None:
    initial_value: int = 3
    decorated = threaded(multiply)
    assert decorated(initial_value, 5).result() == 15
