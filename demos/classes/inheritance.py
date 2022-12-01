

class Person:

    def __init__(self, person_id, first_name, last_name):
        print("person __init__")
        self.first_name = first_name
        self.last_name = last_name

    def full_name(self):
        return f"{self.first_name} {self.last_name}"


class Shareholder(Person):

    def __init__(self, worker_id, first_name, last_name):
        print("shareholder __init__")
        super().__init__(worker_id, first_name, last_name)
        self.worker_id = worker_id

    def record_header(self):
        return f"{self.worker_id} {self.last_name}, {self.first_name}"


class Worker(Person):

    def __init__(self, worker_id, first_name, last_name):
        print("worker __init__")
        super().__init__(worker_id, first_name, last_name)
        self.worker_id = worker_id

    def record_header(self):
        return f"{self.worker_id} {self.last_name}, {self.first_name}"


class FullTime(Shareholder, Worker):

    def __init__(self, worker_id, first_name, last_name):
        print("fulltime __init__")
        super().__init__(worker_id, first_name, last_name)
        self.hours = 50

    def work_schedule(self):
        return f"{self.worker_id} {self.hours} hours"


# class PartTime(Worker):
#
#     def __init__(self, worker_id, first_name, last_name, hours):
#         print("parttime __init__")
#         super().__init__(worker_id, first_name, last_name)
#         self.hours = hours
#
#     def work_schedule(self):
#         return f"{self.worker_id} {self.hours} hours"


fulltime_worker = FullTime(1, "Bob", "Smith")
# parttime_worker.full_name()
# parttime_worker.record_header()
# parttime_worker.work_schedule()

print(FullTime.__mro__)
