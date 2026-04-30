def my_journey(day, hours_studied):
    skills = ["Python", "AI Automation", "Problem Solving", "Frontend"]

    print("------------------------------")
    print("Day: ", day)
    print("Hours studied: ", hours_studied)
    print("------------------------------")

    print("Skills i am building: ")
    for skill in skills:
        print("-", skill)

    if hours_studied >= 3:
        print("Status: On track. Keep going")
    elif hours_studied >=1:
        print("Status: Good, Push harder tomorrow")
    else:
        print("status: Do better tomorrow")

my_journey(3, 3.5)
