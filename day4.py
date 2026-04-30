goals = ["First Client", "Earn in dollars", "Financial Freedom"]
print("My goals:")
for goal in goals:
    print("-", goal)

my_profile = {
    "name": "Pukar Budhathoki",
    "age": 17,
    "country": "Nepal",
    "skill": "Python and AI automation",
    "days_coding": 4
}

print("\nMy profile:")
for key, value in my_profile.items():
    print(key+ ":", value)

roadmap = {
    "month_1": ["Learn Python basics", "Build first project"],
    "month_2": ["learn AI automation", "Get first client"],
    "month_3": ["Raise rates", "Build portfolio"]
}

print("\nMy roadmap:")
for month, tasks in roadmap.items():
    print(month + ":")
    for task in tasks:
        print(" -", task)


