"""Module contains class HabitsList."""

from habit import Habit
from database import Database
from datetime import datetime


class HabitsList(Database):
    """Class HabitsList provides a core functionality of this app to work with the instances of class Habit. Database
    Class is a mixin. It is inherited by HabitsList Class."""

    def __init__(self):
        self.habits = []

    def new_habit(self, name, period, spec, tracked=False, creation_datetime=datetime.now(), tracking=None,
                  longest_streak=0):
        """Method creates new habit and submits it to database."""
        habit = Habit(name,
                      period,
                      spec,
                      tracked,
                      creation_datetime,
                      tracking if tracking else [],
                      longest_streak if longest_streak else 0)
        self.habits.append(habit)
        self.submit_to_db(habit, Database.name)

    def _find_habit(self, habit_id):
        """Method finds habit and takes habit_id as an argument."""
        if self.habits:
            for habit in self.habits:
                if habit.id == habit_id:
                    return habit

    def delete_habit(self, habit_id):
        """Method deletes the habit and takes habit_id as an argument. A database row is deleted accordingly."""
        habit = self._find_habit(habit_id)
        if self.habits:
            self.delete_row(habit, Database.name)
            self.habits.remove(habit)

    def track_habit(self, habit_id, tracked=True):
        """Method tracks habit and takes habit_id as an argument. if the Flag tracked is set to false method track off
        habit. A database row is updated accordingly."""
        habit = self._find_habit(habit_id)
        if habit:
            habit.tracked = tracked
            self.update_db_row(habit, Database.name)

    def check_off(self, habit_id):
        """Method checks off habit and takes habit_id as an argument. Method looks for the last entry in the
        habit.tracking and resets habit.tracking if habit's streak is broken. A database row is updated accordingly."""
        habit = self._find_habit(habit_id)
        if not habit.tracking:
            habit.tracking.append(datetime.now())
        else:
            last_entry = habit.tracking[-1]
            if isinstance(last_entry, str):
                last_entry = datetime.strptime(last_entry, '%Y-%m-%d %H:%M:%S.%f')
            if (datetime.now() - last_entry).days - habit.period > 0:
                habit.tracking = [datetime.now()]
            else:
                habit.tracking.append(datetime.now())
        self.update_db_row(habit, Database.name)
