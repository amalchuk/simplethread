# -*- coding: utf-8 -*-

from threading import Event
from threading import BoundedSemaphore
from time import sleep

from simplethread import synchronized
from simplethread import threaded


def test_synchronized() -> None:
    @synchronized
    def multiply(a: float, b: float) -> float:
        """
        Same as a × b.
        """
        return a * b

    assert multiply(0, 2) == 0
    assert multiply(2, 4) == 8
    assert multiply(4, 8) == 32

    # Create a new lock object:
    lock = BoundedSemaphore()

    @synchronized(lock=lock)
    def add(a: float, b: float) -> float:
        """
        Same as a + b.
        """
        return a + b

    assert add(3, 6) == 9
    assert add(4, 7) == 11
    assert add(5, 8) == 13


def test_threaded() -> None:
    initial_value: int = 3
    event: Event = Event()

    @threaded
    def slow_method(a: float) -> None:
        nonlocal initial_value, event
        sleep(0.25)
        initial_value = a * initial_value
        return event.set()

    # Start the separate thread to multiply initial_value by 5:
    slow_method(5)
    # Wait until the thread is finished:
    event.wait(timeout=1.0)
    assert initial_value == 15

    # Repeat again:
    event.clear()

    # Start the separate thread to multiply initial_value by 2:
    slow_method(2)
    # Wait until the thread is finished:
    event.wait(timeout=1.0)
    assert initial_value == 30
