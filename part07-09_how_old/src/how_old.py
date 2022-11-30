day = int(input("Day: "))
month = int(input("Month: "))
year = int(input("Year: "))
from datetime import datetime, timedelta

millenium = datetime(2000, 1, 1)
birth = datetime(year, month, day)

if year >= 2000:
    print("You weren't born yet on the eve of the new millennium.")
else:
    n = millenium - birth
    print(f"You were {n.days-1} days old on the eve of the new millennium.")