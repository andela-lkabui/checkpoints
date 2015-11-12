import room
from custom.overflow import OverflowException
from people.person import Person


class Office(room.Room):
    
    def __init__(self):
        self.occupants = []
        self.max = 6
        
    def addPeople(self, person):
        """ Adds people (either Staff or Fellow) to an office. Rejects all other instance types. """
        if isinstance(person, Person):
            if (len(self.occupants) < self.max):
                self.occupants.append(person)
            else:
                raise OverflowException('This office space is full!')
        else:

            raise TypeError('Office spaces are meant to be allocated to people (Staff & Fellows)')
