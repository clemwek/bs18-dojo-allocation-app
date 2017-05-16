#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
the Room class and its children are contained here
"""


class Room(object):
    def __init__(self, capacity=0):
        self.capacity = capacity


class Office(Room):
    pass


class LivingSpace(Room):
    pass
