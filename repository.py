from uniclass import UniClass
from schedule import get_schedules, get_rooms
import datetime as dt
from pprint import pprint


class Repository:

    data = []

    def __init__(self, semester, uni_year):
        self.semester = semester
        self.uni_year = uni_year
        current_year = dt.datetime.now().year
        calendar_year = current_year if semester == 1 else current_year - 1
        schedules = get_schedules(
            f"http://www.cs.ubbcluj.ro/files/orar/{calendar_year}-{self.semester}/tabelar/IG{self.uni_year}.html")
        for schedule in schedules:
            for uni_class in schedule:
                uni_cls = UniClass(uni_class['Disciplina'], uni_class['Formatia'], uni_class['Frecventa'], uni_class['Orele'].split(
                    '-')[0], uni_class['Orele'].split('-')[1], get_rooms(uni_class['Sala']), uni_class['Tipul'], uni_class['Ziua'])
                if uni_cls not in self.data:
                    self.data.append(uni_cls)
