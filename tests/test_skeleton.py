#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest
from allo.skeleton import fib

__author__ = "Clement _dhwty_"
__copyright__ = "Clement _dhwty_"
__license__ = "none"


def test_fib():
    assert fib(1) == 1
    assert fib(2) == 1
    assert fib(7) == 13
    with pytest.raises(AssertionError):
        fib(-10)
