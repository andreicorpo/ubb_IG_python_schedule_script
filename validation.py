def check_day(day):
    if type(day) is str:
        if day.lower() == 'monday' or day.lower() == 'luni':
            return 'Luni'
        elif day.lower() == 'tuesday' or day.lower() == 'marti':
            return 'Marti'
        elif day.lower() == 'wendsday' or day.lower() == 'miercuri':
            return 'Miercui'
        elif day.lower() == 'thursday' or day.lower() == 'joi':
            return 'Joi'
        elif day.lower() == 'friday' or day.lower() == 'vineri':
            return 'Vineri'
    elif type(day) is int:
        if day == 0:
            return 'Luni'
        if day == 1:
            return 'Marti'
        if day == 2:
            return 'Miercui'
        if day == 3:
            return 'Joi'
        if day == 4:
            return 'Vineri'
    else:
        raise ValueError


def check_subgroup(subgroup):
    if subgroup not in (1, 2):
        raise ValueError
    else:
        return subgroup
