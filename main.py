import random
from datetime import datetime, timedelta

lowerbound_year = int(input("Input lower bound year: "))
upperbound_year = int(input("Input upper bound year: "))

# Generate a random date within the bounds
start_date = datetime(lowerbound_year, 1, 1)
end_date = datetime(upperbound_year, 12, 31)

# Calculate the number of days between start and end
days_between = (end_date - start_date).days

# Pick a random number of days to add to the start date
random_days = random.randint(0, days_between)
random_date = start_date + timedelta(days=random_days)

print(f"Random date: {random_date.strftime('%Y-%m-%d')}")



