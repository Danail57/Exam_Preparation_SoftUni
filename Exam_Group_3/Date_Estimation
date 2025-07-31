import datetime

exam_date = datetime.date(2018, 8, 26)
date_user = input().split("-")

year, month, day = map(int, date_user)
given_date = datetime.date(year, month, day)

if given_date < exam_date:
    print("Passed")
elif given_date == exam_date:
    print("Today date")
else:
    number_of_days_left = (given_date - exam_date).days + 1
    print(f"{number_of_days_left} days left")
