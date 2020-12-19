# -*- coding: utf-8 -*-

from operator import iadd
from threading import Event
from time import sleep
from typing import List

from simplethread.decorators import synchronized
from simplethread.decorators import threaded


def test_synchronized() -> None:
    initial_value: float = 0.0
    decorated = synchronized(iadd)
    assert decorated(initial_value, 1.0) == 1.0


def test_threaded() -> None:
    initial_value: float = 0.0
    event = Event()

    @threaded
    def slow_method() -> None:
        nonlocal initial_value, event
        sleep(1.0)
        event.set()
        initial_value = initial_value + 1.0

    slow_method()
    event.wait()
    assert initial_value == 1.0
