""" class methods """

from __future__ import annotations


class Person:
    """ person """

    def __init__(self, first_name: str, last_name: str) -> None:
        print("person __init__")
        self.first_name = first_name
        self.last_name = last_name

    def full_name(self) -> str:
        """ full name person """
        return f"{self.first_name} {self.last_name}"

    def copy(self) -> Person:
        """ copy person """
        return Person(self.first_name, self.last_name)

    @classmethod
    def create(cls, full_name: str) -> Person:
        """ create person """
        name_parts = full_name.split(" ")
        return Person(name_parts[0], name_parts[1])


person = Person.create("Bob Smith")

person.copy()
