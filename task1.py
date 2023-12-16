from collections import defaultdict
from datetime import datetime
import calendar

# Sample data
users = [
    {"name": "Antonina Sych", "birthday": datetime(1990, 12, 17)},
    {"name": "Oleksii Aleksieiev", "birthday": datetime(1990, 12, 17)},
    {"name": "Tetiana Chapaliuk", "birthday": datetime(1989, 12, 18)},
    {"name": "Yaroslav Plakhtyna", "birthday": datetime(1985, 12, 15)},
    {"name": "Yuliia Melnyk", "birthday": datetime(1992, 12, 19)},
    {"name": "Olesia Kovalchuk", "birthday": datetime(1988, 12, 20)},
    {"name": "Mariia Illarionova", "birthday": datetime(1993, 12, 21)}
]

def get_birthdays_per_week(users):
    # Get list of dictionaries where each dictionary contains the user's name and date of birth
    birthdays = defaultdict(list)

    # Get current date
    today = datetime.now().date()

    # Iterate through the users from the list of dictionaries
    for user in users:
        name = user["name"]
        birthday = user["birthday"].date()
        birthday_this_year = birthday.replace(year=today.year)

        # Calculate the difference in days
        delta_days = (birthday_this_year - today).days

        # If birthday has already passed this year, will celebrate next year
        if delta_days < 0:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)
            delta_days = (birthday_this_year - today).days

        # Check if the birthday is within the next week and not on a weekend
        if 0 <= delta_days < 7:
            day_of_week = calendar.day_name[birthday_this_year.weekday()]
            # If birthday is on the weekend, shift it to Monday
            if day_of_week in ["Saturday", "Sunday"]:
                day_of_week = "Monday"
            birthdays[day_of_week].append(name)

    # Print the birthdays per day
    for day in calendar.day_name:
        if birthdays[day]:
            print(f"{day}: {', '.join(birthdays[day])}")



get_birthdays_per_week(users)
