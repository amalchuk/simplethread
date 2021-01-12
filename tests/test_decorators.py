# -*- coding: utf-8 -*-

from threading import Event
from time import sleep

from simplethread import asynchronous
from simplethread import synchronized
from simplethread import threaded


def _multiply(a: float, b: float) -> float:
    """
    Same as a × b.
    """
    return a * b


def test_asynchronous() -> None:
    multiply = asynchronous(_multiply)
    assert multiply(0, 2) == 0
    assert multiply(2, 4) == 8
    assert multiply(4, 8) == 32


def test_synchronized() -> None:
    multiply = synchronized(_multiply)
    assert multiply(0, 2) == 0
    assert multiply(2, 4) == 8
    assert multiply(4, 8) == 32


def test_threaded() -> None:
    initial_value: int = 3
    event: Event = Event()

    @threaded
    def slow_method(a: float) -> None:
        nonlocal initial_value, event
        sleep(0.25)
        initial_value = _multiply(a, initial_value)
        return event.set()

    # Start the separate thread to multiply initial_value by 5:
    slow_method(5)
    # Wait until the thread is finished:
    event.wait()
    assert initial_value == 15

    # Repeat again:
    event.clear()

    # Start the separate thread to multiply initial_value by 2:
    slow_method(2)
    # Wait until the thread is finished:
    event.wait()
    assert initial_value == 30
