""" json pickle module """

import jsonpickle
import json


class Address:

    def __init__(self, street, city, state, zip, country):
        self.street = street
        self.city = city
        self.state = state
        self.zip = zip
        self.country = country

    # def __repr__(self) -> str:
    #     return str(self.__dict__)


class Person:
    """ person class """

    def __init__(self, first_name: str, last_name: str):
        self.first_name = first_name
        self.last_name = last_name
        self.address = Address('123 Oak Lane', 'Austin', 'TX', '12345', 'USA')

    def full_name(self):
        """ full name """
        return f"{self.first_name} {self.last_name}"

    def __repr__(self) -> str:
        return str(self.__dict__)


person = Person("Bob", "Smith")

# json.dumps(person)

person_json = jsonpickle.dumps(person)
print(person_json)

person2 = jsonpickle.loads(person_json)
print(person2)
#
# # Cannot be parsed into a Person object
# print(jsonpickle.dumps(person, unpicklable=False))
