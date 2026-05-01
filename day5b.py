# Day 5 - APIs and JSON
# Understanding how real API responses work

import json

# This is exactly what a real API sends back
fake_api_response = {
    "status": "success",
    "developer": {
        "name": "Pukar Budhathoki",
        "age": 17,
        "country": "Nepal",
        "skills": ["Python", "AI Automation", "Frontend"],
        "goal": "International clients paying in dollars",
        "days_coding": 5
    },
    "message": "This is what APIs return. JSON data."
}

# Parsing the response exactly like a real API
data = fake_api_response["developer"]

print("=== API Response ===")
print("Name:", data["name"])
print("Age:", data["age"])
print("Country:", data["country"])
print("Days coding:", data["days_coding"])
print("Goal:", data["goal"])
print("\nSkills:")
for skill in data["skills"]:
    print("-", skill)

# Converting to JSON string
json_string = json.dumps(fake_api_response, indent=4)
print("\n=== Raw JSON ===")
print(json_string)