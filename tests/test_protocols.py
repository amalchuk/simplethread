# -*- coding: utf-8 -*-

from threading import BoundedSemaphore
from threading import Event
from threading import Lock
from threading import RLock
from threading import Semaphore

from simplethread.protocols import LockType


def test_lock_type() -> None:
    assert isinstance(BoundedSemaphore(), LockType)
    assert isinstance(Lock(), LockType)
    assert isinstance(RLock(), LockType)
    assert isinstance(Semaphore(), LockType)

    assert not isinstance(None, LockType)
    assert not isinstance(Event(), LockType)
