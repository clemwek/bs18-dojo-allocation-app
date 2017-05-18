#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This file serve as a starting point for a Python console script.
"""
import random

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
        self.room_allocation = {
            "office": {},
            "living_space": {}
        }

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

    def rand_room_gen(self, room_type):
        rooms_not_full = []
        if room_type == 'office':
            for office in self.all_offices:
                if len(self.all_offices[office].members) < self.all_offices[office].capacity:
                    rooms_not_full.append(self.all_offices[office].room_name)
            if len(rooms_not_full) < 1:
                return False
            random_room = random.choice(rooms_not_full)
            return random_room
        else:
            for living_space in self.all_living_space:
                if len(self.all_offices[living_space].members) < self.all_offices[living_space].capacity:
                    rooms_not_full.append(self.all_offices[living_space].room_name)
            if len(rooms_not_full) < 1:
                return False
            random_room = random.choice(rooms_not_full)
            return random_room

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
                if len(self.all_offices) > 0: #this randomly allocate an office to a fellow
                    if self.rand_room_gen('office'):
                        rand_room = (self.rand_room_gen('office'))
                        if not self.allocate_person_room(person_name, rand_room):
                            print('room allocation failed')
                if accommodation == 'y' and len(self.all_living_space) > 0:
                    rand_room = (self.rand_room_gen('living_space'))
                    if not self.allocate_person_room(person_name, rand_room):
                        print('room allocation failed')
                return "{} - staff space added successfully".format(person_name)

            elif person_kind == 'staff':
                new_staff = Staff(person_name)
                self.all_staff[person_name] = new_staff
                self.all_persons[person_name] = new_staff
                if len(self.all_offices) > 0:
                    if self.rand_room_gen('office'):
                        rand_room = (self.rand_room_gen('office'))
                        if not self.allocate_person_room(person_name, rand_room):
                            print('room allocation failed')

                return "{} - staff space added successfully".format(person_name)
            else:
                return "A person can only be staff or fellow"
        except ValueError as e:
            return "The value passed is not a string"

    def allocate_person_room(self, person_name, room_name):
        self.all_rooms[room_name].members.append(person_name)
        return True

    def print_room(self, room_name):
        room_name = room_name.lower()
        if room_name not in self.all_rooms:
            return '{} room is not added yet'.format(room_name)
        print()
        return self.all_rooms[room_name].members

    def print_allocations(self):
        pass

    def print_unallocated(self):
        pass

if __name__ == "__main__":
    dojo = Dojo()
    print(dojo.create_room('office', 'banana'))
    # print(dojo.all_offices)
    print(dojo.add_person('prim', 'fellow'))
    print('This is here')
    print(dojo.print_room('banana'))
    # dojo.rand_room_gen('office')
