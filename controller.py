from repository import Repository


class Controller:

    def __init__(self, repository):
        self.repository = repository

    def get_all(self):
        for uni_class in self.repository.data:
            print(uni_class)

    def get_by_day(self, day):
        for uni_class in self.repository.data:
            if uni_class.day == day:
                print(uni_class.__str__(day=False))

    def get_by_group(self, group):
        for uni_class in self.repository.data:
            if uni_class.group == group or uni_class.group == group[:-2] or uni_class.group == f'IG{self.repository.uni_year}':
                print(uni_class.__str__(group=False))

    def get_by_group_and_day(self, group, day):
        for uni_class in self.repository.data:
            if (uni_class.group == group or uni_class.group == group[:-2] or uni_class.group == f'IG{self.repository.uni_year}') and uni_class.day == day:
                print(uni_class.__str__(day=False, group=False))
