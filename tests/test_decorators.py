# -*- coding: utf-8 -*-

from operator import add
from types import MethodType

from pytest import raises

from simplethread.decorators import threaded


def test_threaded() -> None:
    with raises(TypeError, match="None is not callable or a descriptor"):
        threaded(None)  # type: ignore

    decorated = threaded(add)
    assert decorated.user_function == add

    thread_identifier = decorated("a", "b")
    assert isinstance(thread_identifier, int)
    assert thread_identifier > 0

    class test_object(object):
        @threaded
        def test(self) -> bool:
            return True

    test = test_object()
    assert isinstance(test.test, MethodType)
