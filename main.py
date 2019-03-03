from pprint import pprint

from repository import Repository

from controller import Controller

from validation import check_day, check_subgroup

import sys
import getopt
import datetime as dt


def main(argv):

    help_info = '''
    This is a script to show the university schedule for the
    students at Babes Bolyai University majoring in Computer Science
    in german.
    
    Help:
    Use -h(--help) options to see how the scripdayt works
    Use -t(--today) to see the schedule for today
    Use -g(--group) to see the schedule for a specific group
    Use -d(--day) to see the schedule for a specific day
        Accepted values are:
            Monday/Luni
            Tuesday/Marti
            Wendsday/Miercuri
            Thursday/Joi
            Friday/Vineri

    Possible options combinations:
    - group and today
    - group and day 
                '''

    correct = False

    try:
        opts, args = getopt.getopt(
            argv, 'thg:d:', ['help', 'today', 'group=', 'day='])
    except getopt.GetoptError:
        print(help_info)
        sys.exit(2)
    day = None
    group = None
    today = False
    today_day = None
    help = False
    for opt, arg in opts:
        if opt in ('-h', '--help'):
            print(help_info)
            help = True
        elif opt in ('-t', '--today'):
            today = True
            today_day = dt.datetime.today().weekday()
        elif opt in ('-d', '--day'):
            day = arg
        elif opt in ('-g', '--group'):
            group = arg
    if help is False:
        while not correct:
            try:
                print('\n')
                year = int(input('Enter your current university year: '))
                semester = int(input('Enter your current semester: '))
                correct = True
                print('\nLoading data...')
            except ValueError:
                print('Given values are not correct. Please enter them again.')
                sys.exit(2)
        r = Repository(semester, year)
        ctrl = Controller(r)
        print('\nDone.')
        if day is None and group is None and today is False:
            print('\n')
            ctrl.get_all()
        elif day is None and group is not None and today is True:
            print('\n')
            if len(group) == 3:
                try:
                    subgroup = check_subgroup(int(input('Enter subgroup: ')))
                    print('\n')
                    print(f'{group}/{subgroup}')
                    ctrl.get_by_group_and_day(
                        day=check_day(today_day), group=f'{group}/{subgroup}')
                except ValueError:
                    print('Given values are not correct. Please rerun the script.')
            else:
                ctrl.get_by_group_and_day(
                    day=check_day(today_day), group=group)

        elif day is not None and group is not None and today is False:
            print('\n')
            if len(group) == 3:
                try:
                    subgroup = check_subgroup(int(input('Enter subgroup: ')))
                    print('\n')
                    ctrl.get_by_group_and_day(day=check_day(
                        day), group=f'{group}/{subgroup}')
                except ValueError:
                    print('Given values are not correct. Please rerun the script.')
            else:
                ctrl.get_by_group_and_day(day=check_day(day), group=group)

        elif day is not None:
            print('\n')
            ctrl.get_by_day(check_day(day))
        elif today is True:
            print('here\n')
            ctrl.get_by_day(check_day(today_day))
        elif group is not None:
            print('\n')
            if len(group) == 3:
                try:
                    subgroup = check_subgroup(int(input('Enter subgroup: ')))
                    print('\n')
                    ctrl.get_by_group(f'{group}/{subgroup}')
                except ValueError:
                    print('Given values are not correct. Please rerun the script.')
            else:
                ctrl.get_by_group(group)

        else:
            print('No such combination of arguments possible.')


if __name__ == "__main__":
    main(sys.argv[1:])
