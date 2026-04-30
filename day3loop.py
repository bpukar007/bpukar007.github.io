#Day3- loop

# for loop
skills = ["Pythom", "AI Automation", "Problem Solving", "Frontend"]
for skill in skills:
    print(skill)

# while loop
day = 1
while day <= 7:
    print("Day ", day, "Of building my future")
    day += 1

def countdown(num):
    while num > 0:
        print("Days left until my first client: ", num)
        num -= 1
    print("client acquired!")

countdown(5)
