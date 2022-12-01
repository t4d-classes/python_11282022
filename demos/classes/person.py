

class Person:

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def display_fullname(self):
        print(f"{self.first_name} {self.last_name}")

    def display_recordheader(self):
        print(f"{self.last_name}, {self.first_name}")


# person1 = Person('Bob', 'Smith')
# person1.display_fullname()
#
# person2 = Person('Jane', 'Smith')
# person2.display_fullname()
#
# print(person1.display_fullname)
#
# # curry
# func add(a,b) {
#     return a+b
# }
#
# add2 = add.bind(2)
#
# func add2(b) {
#     return add(2, b)
# }
#
# add2(6) => 8