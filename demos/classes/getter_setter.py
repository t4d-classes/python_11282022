class Person:

    def __init__(self, first_name):
        self.__first_name = first_name

    # def get_first_name(self):
    #     return self.__first_name
    #
    # def set_first_name(self, first_name):
    #     if (len(first_name) > 0):
    #         self.__first_name = first_name

    @property
    def first_name_upper(self):
        print("called get first_name property")
        return self.__first_name.upper()

    @property
    def first_name(self):
        print("called get first_name property")
        return self.__first_name

    @first_name.setter
    def first_name(self, first_name):
        print("called set first_name property")
        if (len(first_name) > 0):
            self.__first_name = first_name
        else:
            raise Exception("")


person = Person('Bob')
print(person.first_name)
person.first_name = ""
