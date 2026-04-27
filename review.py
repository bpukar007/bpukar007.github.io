def check():
    age = 17
    if age < 20: 
        print("You have started early!")

def information():
    name = "Pukar Budhathoki"
    country = "Nepal"
    print("My name is", name)
    print("I am from", country)
    age = 17
    print("I am", age, "years old")

def my_goals():
    goal = "to be sucessful so that my family will live a better life"
    print("My goal is", goal)

def my_skills():
    skills = ["Python" , "Discipline" , "Hardwork"]
    print("My skills are:")
    for skill in skills:
        print("-", skill)


information()
print("-----------------------------")
my_goals()
print("-----------------------------")
my_skills()
print("-----------------------------")
check()