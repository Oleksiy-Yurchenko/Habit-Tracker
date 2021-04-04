"""Module analytics contains functions tracked(), same_period(), longest_streak()."""


def tracked(habits_list, tracked_status=True):
    """Function takes a list with habits as an argument and returned the list of habits with the tracked status set to
    True by default. If the flag tracked_status is set to false function will return a list of habits with the tracked
    status set to False."""
    return [habit for habit in habits_list if habit.tracked == tracked_status]


def same_period(habits_list, period):
    """Function takes a list with habits and period as arguments and returned the list of habits with the period.
    Argument period is of type int. In current version it can be 1 - Daily or 7 - Weekly."""
    return [habit for habit in habits_list if habit.period == period]


def longest_streak(habits_list):
    """Function takes a list with habits an returns a list containing a habit with the longest streak."""
    streaks_list = sorted(habits_list, key=lambda habit: habit.longest_streak, reverse=True)
    return streaks_list[:1]
