def greet(name):
    return "Hello, "+ name

def calculate_earnings(hours, rate):
    return hours*rate

def my_goals(year):
    if year == 1:
        return "First Inteernational Client"
    elif year == 2:
        return "Earning 3000 per month"
    elif year == 3:
        return "Fully financially free"
    
print(greet("Pukar"))
print("Earnings_today: ", calculate_earnings(3,3))
print("Year 1 goal: ", my_goals(1))
print("Year 2 goal: ", my_goals(2))
print("Year 3 goal: ", my_goals(3))