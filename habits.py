from habit import Habit
from datetime import date


class HabitsList:
    def __init__(self):
        self.habits = []

    def new_habit(self, name, spec, period, creation_date=date.today(), tracked=False, tracking=[], longest_streak=0):
        self.habits.append(
                Habit(name, period, creation_date, spec, tracked, tracking, longest_streak)
                )

    def _find_habit(self, habit_id):
        if self.habits:
            return self.habits[habit_id]
        return None

        #for habit in self.habits:
            #if str(habit.id) == str(habit_id):
                #return habit
        #return None

    def delete_habit(self, habit_id):
        habit = self._find_habit(habit_id)
        if self.habits:
            self.habits.remove(habit)


    def modify_name(self, habit_id, name):
        habit = self._find_habit(habit_id)
        if habit:
            habit.name = name
            return True
        return False

    def modify_period(self, habit_id, period):
        habit = self._find_habit(habit_id)
        if habit:
            habit.period = period
            return True
        return False

    def modify_spec(self, habit_id, spec):
        habit = self._find_habit(habit_id)
        if habit:
            habit.spec = spec
            return True
        return False

    def track_habit(self, habit_id, tracked=True):
        habit = self._find_habit(habit_id)
        habit.tracked = tracked

    def check_off(self, habit_id):
        habit = self._find_habit(habit_id)
        return habit.tracking.append(date.today()) #datetime.datetime.now().timestamp())

    def search(self, filter):
        return [habit for habit in self.habits if habit.match(filter)]

    def analyze_tracking(self, habit_id):
        print(self._find_habit(habit_id).tracking)
