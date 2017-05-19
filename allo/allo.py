#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This file serve as a starting point for a Python console script.
"""
import random
import os

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
        self.room_allocation = {}
        self.pending_room_allocation = {}

    def create_room(self, room_type, room_name):
        """
        Creates a room when room type is specified to living space of office and the room name
        :param room_type: string
        :param room_name: string
        :return: string
        """
        try:
            room_type = room_type.lower()
            room_name = room_name.lower()
            if room_name in self.all_rooms.keys():
                return "Sorry, {} room name has been taken.".format(room_name)
            if room_type == 'office':
                new_office = Office(room_name)
                self.all_offices[room_name] = new_office
                self.all_rooms[room_name] = new_office
                return "{} - office added successfully".format(room_name)
            elif room_type == 'living':
                new_living = LivingSpace(room_name)
                self.all_living_space[room_name] = new_living
                self.all_rooms[room_name] = new_living
                return "{} - living space added successfully".format(room_name)
            else:
                return "A room can only be office or living space"
        except ValueError as e:
            return "The value passed is not a string"

    def rand_room_gen(self, room_type):
        """
        This takes in a room type and randomly chooses a room that is filled less to capacity
        :param room_type: string
        :return: room name if found else false
        """
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

    def add_person(self, person_name, person_kind, accommodation=None):
        """
        this takes in a person name, the role of the person and if he wants accommodation
        :param person_name: string
        :param person_kind: string
        :param accommodation: string
        :return: string
        """
        try:
            person_name = person_name.lower()
            person_kind = person_kind.lower()

            if accommodation is None:
                accommodation = 'n'
            else:
                accommodation = accommodation.lower()

            if person_name in self.all_persons.keys():
                return "Sorry, {} person name has been added.".format(person_name)

            if person_kind == 'fellow':
                new_fellow = Fellow(person_name)
                self.all_fellows[person_name] = new_fellow
                self.all_persons[person_name] = new_fellow

                # this randomly allocate an office to a fellow
                office_allocation = False
                if len(self.all_offices) > 0:
                    if self.rand_room_gen('office'):
                        rand_room = (self.rand_room_gen('office'))
                        if not self.allocate_person_room(person_name, rand_room):
                            print('room allocation failed')

                if accommodation == 'y' and len(self.all_living_space) > 0:
                    rand_room = (self.rand_room_gen('living_space'))
                    if not self.allocate_person_room(person_name, rand_room):
                        print('room allocation failed')
                    print('{} room was allocated'.format(rand_room))
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
                    if accommodation == 'y':
                        print('Staff cannot be allocated living space')
                return "{} - staff space added successfully".format(person_name)
            else:
                return "A person can only be staff or fellow"
        except ValueError as e:
            return "The value passed is not a string"

    def allocate_person_room(self, person_name, room_name):
        """
        this takes in person name and room name ana allocate the person to the room
        :param person_name: string
        :param room_name: string
        :return: returns True if allocated False otherwise
        """
        self.all_rooms[room_name].members.append(person_name)
        if room_name in self.room_allocation:
            self.room_allocation[room_name].append(person_name)
            self.all_persons[person_name].accommodation = True
        else:
            self.room_allocation[room_name] = []
            self.room_allocation[room_name].append(person_name)
            self.all_persons[person_name].accommodation = True
        return True

    def print_room(self, room_name):
        """
        This function prints all the people that are allocated to that room
        :param room_name: string
        :return: string
        """
        room_name = room_name.lower()
        print('---------------------------------------------------')
        print('              {}'.format(room_name.upper()))
        print('---------------------------------------------------')
        if room_name not in self.all_rooms:
            return '{} room is not added yet'.format(room_name)

        if len(self.all_rooms[room_name].members) > 0:
            print_text = ''
            for name in self.all_rooms[room_name].members:
                print_text += name + ', '
            return print_text
        return 'There are no entries in the room'

    def print_allocations(self, filename=None):
        """
        This prints out all the people that are allocated to a room, if given a filename 
        if writes that data in text file
        :param filename: string
        :return: string
        """
        if len(self.room_allocation) > 0:
            for room in self.room_allocation:
                print(room.upper() + '\n')
                print('--------------------------------------------------\n')
                print((', '.join(self.room_allocation[room])))
                print('\n')
        else:
            print("There are no rooms and allocations made yet!")
        if filename is not None:
            if len(self.room_allocation) > 0:
                print_text = ''
                for room in self.room_allocation:
                    print_text += room.upper() + '\n'
                    print_text += '--------------------------------------------------\n'
                    print_text += (', '.join(self.room_allocation[room]))
                    print_text += '\n'

            else:
                print_text = "There are no rooms and allocations made yet!"
            filename = filename + '.txt'
            f = open(filename, 'w')
            f.write(print_text)
            f.close()
            return 'Files where written successful!'

    def print_unallocated(self, filename=None):
        unallocated_list = []
        for person in self.all_persons:
            if not self.all_persons[person].accommodation:
                unallocated_list.append(person)
        print('List of Unallocated people')
        print('--------------------------------------------------------------------')
        if len(unallocated_list) > 0:
            print(', '.join(unallocated_list))
        else:
            print("Unallocated list is currently empty")

        if filename is not None:
            print_file = ''
            print_file += 'List of Unallocated people\n'
            print_file += '--------------------------------------------------------------------\n'
            if len(unallocated_list) > 0:
                print_file += ', '.join(unallocated_list) + '\n'
            else:
                print_file += "Unallocated list is currently empty"

            filename = filename + '.txt'
            f = open(filename, 'w')
            f.write(print_file)
            f.close()
            return 'Files where written successful!'
