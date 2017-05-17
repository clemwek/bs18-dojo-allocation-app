#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This file serve as a starting point for a Python console script.
"""
from random import randrange

from allo.room.room import Room, Office, LivingSpace
from allo.person.person import Person, Fellow, Staff


class Dojo(object):
    """
    Class Dojo the main entry point to a110-cli
    """
    def __init__(self):
        self.all_persons = {}
        self.all_fellows = {}
        self.all_staff = {}
        self.all_rooms = {}
        self.all_offices = {}
        self.all_living_space = {}

    def create_room(self, room_type, room_name):
        try:
            room_type = room_type.lower()
            room_name = room_name.lower()
            if room_name in self.all_rooms.keys():
                return "Sorry, {} room name has been taken.".format(room_name)
            if room_type == 'office':
                new_office = Office(room_name)
                self.all_offices[room_name] = new_office
                self.all_rooms[room_name] = new_office
                self.room_allocation['office'][room_name] = []
                return "{} - office added successfully".format(room_name)
            elif room_type == 'living':
                new_living = LivingSpace(room_name)
                self.all_living_space[room_name] = new_living
                self.all_rooms[room_name] = new_living
                self.room_allocation['living_space'][room_name] = []
                return "{} - living space added successfully".format(room_name)
            else:
                return "A room can only be office or living space"
        except ValueError as e:
            return "The value passed is not a string"

    def add_person(self, person_name, person_kind, accommodation='N'):
        try:
            person_name = person_name.lower()
            person_kind = person_kind.lower()
            accommodation = accommodation.lower()
            if person_name in self.all_persons.keys():
                return "Sorry, {} person name has been added.".format(person_name)
            if person_kind == 'fellow':
                new_fellow = Fellow(person_name)
                self.all_fellows[person_name] = new_fellow
                self.all_persons[person_name] = new_fellow
                if len(self.all_offices) > 0:
                    key = randrange(len(self.all_offices)+1)
                    rand_room = self.all_offices.keys[key]
                    self.allocate_person_room(person_name, rand_room)
                if accommodation == 'y' and len(self.all_living_space) > 0:
                    key = randrange(len(self.all_living_space) + 1)
                    rand_room = self.all_living_space.keys[key]
                    self.allocate_person_room(person_name, rand_room)
                return "{} - fellow added successfully".format(person_name)
            elif person_kind == 'staff':
                new_staff = Staff(person_name)
                self.all_staff[person_name] = new_staff
                self.all_persons[person_name] = new_staff
                if len(self.all_offices) > 0:
                    key = randrange(len(self.all_offices)+1)
                    rand_room = self.all_offices.keys[key]
                    self.allocate_person_room(person_name, rand_room)
                return "{} - staff space added successfully".format(person_name)
            else:
                return "A room can only be office or living space"
        except ValueError as e:
            return "The value passed is not a string"

    def allocate_person_room(self, person_name, room_name):
        if self.all_rooms[room_name].capacity < len(self.all_rooms[room_name].members):
            self.all_rooms[room_name].members.append(person_name)
            return True

