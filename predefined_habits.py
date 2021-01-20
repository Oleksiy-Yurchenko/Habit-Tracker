import datetime

PREDEFINED_HABITS = [
    {
        "id": 1,
        "name": "Run",
        "spec": "run every week",
        "period": 1,
        "creation_date": datetime.date.today(),
        "tracked": True,
        "tracking": [datetime.date(2021, 1, 18)],
        "longest_streak": 0
    },
    {
        "id": 2,
        "name": "Exercise in gym",
        "spec": "Exercise in gym every week",
        "period": 1,
        "creation_date": datetime.date.today(),
        "tracked": True,
        "tracking": [datetime.date(2021, 1, 5), datetime.date(2021, 1, 18)],
        "longest_streak": 0
    },
    {
        "id": 3,
        "name": "Brush teeth",
        "spec": "Brush teeth every morning",
        "period": 1,
        "creation_date": datetime.date.today(),
        "tracked": True,
        "tracking": [],
        "longest_streak": 0
    }
]
