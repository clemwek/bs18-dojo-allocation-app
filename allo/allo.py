# -*- coding: utf-8 -*-
"""
This file serve as a starting point for a Python console script.
"""
import random

from allo.room.room import Office, LivingSpace
from allo.person.person import Fellow, Staff


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
        self.pending_room_allocation = {'office': {}, 'living_space': {}}

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
        except ValueError:
            return "The value passed is not a string"

    def rand_room_gen(self, room_type):
        """
        This takes in a room type and randomly chooses a room that is filled less to capacity
        :param room_type: string
        :return: room name if found else false
        """
        if room_type == 'office':
            return self.rand_office_gen()
        else:
            return self.rand_living_space_gen()

    def rand_living_space_gen(self):
        """
        This loops through all the living space and return a random living space room with
        space for a person
        :return: string
        """
        rooms_not_full = []
        for living_space in self.all_living_space:
            if len(self.all_living_space[living_space].members) < self.all_living_space[living_space].capacity:
                rooms_not_full.append(self.all_living_space[living_space].room_name)
        if len(rooms_not_full) < 1:
            return False
        random_room = random.choice(rooms_not_full)
        return random_room

    def rand_office_gen(self):
        """
        This loops through all the offices and return a random office room with space for a person
        :return:
        """
        rooms_not_full = []
        for office in self.all_offices:
            if len(self.all_offices[office].members) < self.all_offices[office].capacity:
                rooms_not_full.append(self.all_offices[office].room_name)
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
                return self.create_fellow(person_name, accommodation)

            elif person_kind == 'staff':
                return self.create_staff(person_name, accommodation)
            else:
                return "A person can only be staff or fellow"
        except ValueError:
            return "The value passed is not a string"

    def create_fellow(self, person_name, accommodation):
        """
        This takes in a person name and accommodation
        :param person_name:string
        :param accommodation: string
        :return: string
        """
        new_fellow = Fellow(person_name)
        self.all_fellows[person_name] = new_fellow
        self.all_persons[person_name] = new_fellow

        if len(self.all_offices) > 0:
            if self.rand_room_gen('office'):
                rand_room = (self.rand_room_gen('office'))
                if not self.allocate_person_room(person_name, rand_room):
                    print('room allocation failed')
                else:
                    print('{} office was allocated to {} - fellow'.format(rand_room, person_name))
                    self.all_persons[person_name].office = True
                    self.all_fellows[person_name].office = True
        else:
            self.pending_room_allocation['office'][person_name] = True

        if accommodation == 'y' and len(self.all_living_space) > 0:
            rand_room = (self.rand_room_gen('living_space'))
            if rand_room:
                if self.allocate_person_room(person_name, rand_room):
                    self.all_persons[person_name].accommodation = True
                    self.all_fellows[person_name].accommodation = True
                    print('{} living space was allocated to {} - fellow.'.format(rand_room, person_name))
            else:
                print('No living space is available for allocation')
        elif accommodation == 'y' and len(self.all_living_space) == 0:
            self.pending_room_allocation['living_space'][person_name] = True

        return "{} - fellow has been added successfully".format(person_name)

    def create_staff(self, person_name, accommodation):
        """
        Takes in a person name and accommodation,creates a staff and allocates an office
        if there is space
        :param person_name: String
        :param accommodation: String
        :return: string
        """
        new_staff = Staff(person_name)
        self.all_staff[person_name] = new_staff
        self.all_persons[person_name] = new_staff

        if len(self.all_offices) > 0:
            if self.rand_room_gen('office'):
                rand_room = (self.rand_room_gen('office'))
                if not self.allocate_person_room(person_name, rand_room):
                    print('room allocation failed')
                else:
                    self.all_persons[person_name].office = True
                    self.all_staff[person_name].office = True
                    print('{} - office was allocated to {} - staff'.format(rand_room, person_name))

            if accommodation == 'y':
                print('Staff cannot be allocated living space')

        return "{} - staff has been added successfully".format(person_name)

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
        else:
            self.room_allocation[room_name] = []
            self.room_allocation[room_name].append(person_name)
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
            return "There are no rooms and no allocations made yet!"

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
        unallocated_list = {'office': [], 'living_space': []}
        for person in self.all_persons:
            if not self.all_persons[person].accommodation:
                unallocated_list['living_space'].append(person)

            if not self.all_persons[person].office:
                unallocated_list['office'].append(person)

        print('--------------------------------------------------------------------\n')
        print('List of Unallocated people to offices\n')
        print('--------------------------------------------------------------------\n')
        if len(unallocated_list['office']) > 0:
            print(', '.join(unallocated_list['office']))
        else:
            print("Unallocated offices list is currently empty")

        print('--------------------------------------------------------------------\n')
        print('List of Unallocated people to living space\n')
        print('--------------------------------------------------------------------\n')
        if len(unallocated_list['living_space']) > 0:
            print(', '.join(unallocated_list['living_space']))
        else:
            print("Unallocated living space list is currently empty")

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

    def list_rooms(self):
        return list(self.all_rooms.keys())

    def reallocate_person(self, person_name, room_name):
        if room_name in self.all_rooms.keys() and person_name in self.all_persons.keys():
            if type(self.all_persons[person_name]) is Fellow:
                if type(self.all_rooms[room_name]) is LivingSpace:
                    if self.allocate_person_room(person_name, room_name):
                        return '{} - staff is allocated to {} living space'.format(person_name, room_name)
                else:
                    if self.allocate_person_room(person_name, room_name):
                        return '{} - staff is allocated to {} office'.format(person_name, room_name)
            elif type(self.all_persons[person_name]) is Staff:
                if type(self.all_rooms[room_name]) is LivingSpace:
                    return '{} is staff and cannot be allocated living space {}'.format(person_name, room_name)
                else:
                    if self.allocate_person_room(person_name, room_name):
                        return '{} - staff is allocated to {} office'.format(person_name, room_name)

    def load_people(self, file_name):
        try:
            with open(file_name) as f:
                for line in f:
                    words = line.split()
                    name = words[0] + ' ' + words[1]
                    person_kind = words[2]
                    if len(words) == 4:
                        accommodation = words[3]
                    else:
                        accommodation = None
                    self.add_person(name, person_kind, accommodation)
        except (OSError, IOError) as e:
            return 'Something went wrong while opening the file!!!'
