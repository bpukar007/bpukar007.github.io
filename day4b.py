import datetime
import random
import math

motivation = [
    "You are building something real.",
    "Day 4 most people never get here.",
    "Kathmandu to the world, watch",
    "Every line of code is progress.",
    "Your future self will thank you"
]

print("Today's motivation: "
      + random.choice(motivation))

datetime = datetime.datetime.now()
print("\nToday's date:", datetime.strftime("%Y-%m-%d"))
print("Time right now:", datetime.strftime("%H:%M:%S"))

hours_per_day = 3
days_per_year = 365
total_hours = math.floor(hours_per_day * days_per_year)
print("\nTotal hours i will study this year:", total_hours)
print("This is more than most people study in 5 years.")