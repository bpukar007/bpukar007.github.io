class FreeLanceProject:
    def __init__(self, project_name, client_name, rate, hours_worked):
        self.project_name = project_name
        self.client_name = client_name
        self.rate = rate
        self.hours_worked = hours_worked

    def calculate_earnings(self):
        return self.rate * self.hours_worked
    
    def show_details(self):
        total = self.calculate_earnings()
        details = (
            f"Project Name: {self.project_name}\n"
            f"Client Name: {self.client_name}\n"
            f"Rate: ${self.rate}/hour\n"
            f"Hours Worked: {self.hours_worked:.2f}\n"
            f"Total Earnings: ${total:.2f}"
        )
        print(details)

    def is_profitable(self):
        total = self.calculate_earnings()
        if total >= 100:
            print("Status: Profitable")
        else:
            print("Status: Keep Pushing")

project1 = FreeLanceProject("Email Generator", "ABC company", 15, 3)
project2 = FreeLanceProject("Tally Automation", "XYZ company", 50, 5)

print("=====================================")
print("            PROJECT INVOICE               ")
print("=====================================")
project1.show_details()
project1.is_profitable()
print("=====================================")

print("=====================================")
print("            PROJECT INVOICE               ")
print("=====================================")
project2.show_details()
project2.is_profitable()
print("=====================================")