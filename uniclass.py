class UniClass:
    def __init__(self, class_title, group, recurrence, start_time, end_time, room, class_type, day):
        self.class_name = class_title
        self.group = group
        self.recurrence = recurrence if type(
            recurrence) == str else 'Fiecare saptamana'
        self.start_time = start_time
        self.end_time = end_time
        self.room = room
        self.class_type = class_type
        self.day = day

    def __str__(self, class_name=True, group=True, recurrence=True, start_time=True, end_time=True, room=True, class_type=True, day=True):
        info = ''
        if class_name:
            info += 'Course name: ' + self.class_name + '\n'
        if group:
            info += 'Group: ' + self.group + '\n'
        if recurrence:
            info += 'Recurrence: ' + str(self.recurrence) + '\n'
        if start_time:
            info += 'Start time: ' + f'{self.start_time}:00' + '\n'
        if end_time:
            info += 'End time: ' + f'{self.end_time}:00' + '\n'
        if room:
            info += 'Room: ' + self.room + '\n'
        if class_type:
            info += 'Course type: ' + self.class_type + '\n'
        if day:
            info += 'Day: ' + self.day + '\n'
        return info

    def __eq__(self, value):
        if isinstance(value, self.__class__):
            return self.class_name == value.class_name and self.group == value.group
        return False
