from datetime import timedelta
from functools import reduce


def tracked(habits_list):
    return [habit for habit in habits_list if habit.tracked]

    '''
    for habit in habits_list:
        if habit.tracked:
            tracked_habits.append(habit)
    '''
    #for habit in tracked_habits:
        #print("{0}: {1}\n{2}".format(tracked_habits.index(habit) + 1, habit.name, habit.period, habit.spec))

def same_period(habits_list, period):
    return [habit for habit in habits_list if habit.period == period]

    '''
    same_period = []
    for habit in habits_list:
        if habit.period == period:
            same_period.append(habit)
    for habit in same_period:
        print("{0}: {1}\n{2}".format(habit.id, habit.name, habit.spec))
        '''

def longest_streak(habits_list):
    tracked_list = tracked(habits_list)
    streaks_list = sorted(tracked_list, key=lambda habit: streak(habit.tracking)
        if len(habit.tracking) > habit.longest_streak else habit.longest_streak, reverse=False)
    return streaks_list[:1]

def streak(check_off_list):
    return (check_off_list[-1] - check_off_list[0]).days


