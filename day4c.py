# Writing to a file
with open("/Users/mac/Desktop/my_journey.txt", "w") as file:
    file.write("Name: Pukar Budhathoki\n")
    file.write("Day: 4\n")
    file.write("Skill: Python and AI automation\n")
    file.write("Goal: International clients\n")
    file.write("Status: Unstoppable\n")

print("File has been created")

# Writing to a file
with open("/Users/mac/Desktop/my_journey.txt", "r") as file:
    contents = file.read()
    print("\nfile contents:")
    print(contents)

with open("/Users/mac/Desktop/my_journey.txt", "a") as file:
    file.write("Day 4 complete. Still showing up.\n")

print("File updated sucessfullly")


