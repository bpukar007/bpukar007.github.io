def introduce_myself():
    name = "Pukar Budhathoki"
    age = 17
    country = "Nepal"
    print("My name is", name)
    print("I am", age, "years old")
    print("I am from", country)
    
def my_skills():
    skills = ["Python" , "Discipline" , "Hunger" , "Focus"]
    print("My current skills:")
    for skill in skills:
        print("-", skill)

def my_goals():
    goals = ["Learn Python" , "Get first client" , "Earn in dollars" , "Be financially free"]
    print("my goals:")
    for goal in goals:
        print("-", goal)

introduce_myself()
print("-----------------------------")
my_skills()
print("-----------------------------")
my_goals()