"""Module contains class Habit."""

from datetime import datetime


class Habit:
    """Class Habit models a habit with the following attributes: name, period, spec, _tracked, creation_datetime, id,
    _tracking, _longest_streak."""
    last_id = 0

    def __init__(self, name, period, spec='', tracked=False, creation_datetime=datetime.now(),
                 tracking=None, longest_streak=0):
        self.name = name
        self.spec = spec
        self.period = period
        self._tracked = tracked
        self.creation_datetime = creation_datetime
        self.id = Habit._generate_order_id()
        self._tracking = tracking
        self._longest_streak = longest_streak

    @ classmethod
    def _generate_order_id(cls):
        """Class method generates Habit id."""
        Habit.last_id += 1
        return Habit.last_id

    @ property
    def tracked(self):
        return self._tracked

    @ tracked.setter
    def tracked(self, value):
        self._tracked = value

    @ property
    def tracking(self):
        return self._tracking

    @ tracking.setter
    def tracking(self, value):
        self._tracking = value

    @ property
    def longest_streak(self):
        return self._longest_streak

    @ longest_streak.setter
    def longest_streak(self, value):
        self._longest_streak = value
