class Developer:
    def __init__(self, name, age, country, skill):
        self.name = name
        self.age = age
        self.country = country
        self.skill = skill
        self.project = []

    def introduce(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Country: {self.country}")
        print(f"Skill: {self.skill}")

    def add_project(self, project):
        self.project.append(project)
        print(f"Project added: {project}")

    def show_projects(self):
        print(f"Projects for {self.name}:")
        for projecter in self.project:
            print(f" - {projecter}")

    def pitch(self):
        print(f"\nHi I am {self.name} from {self.country}.")
        print(f"I specialize in {self.skill}")
        print(f"I have built {len(self.project)} projects so far.")
        print(f"I am hungry, disciplined and ready to deliver")

Pukar = Developer("Pukar", 19, "Nepal", "Python")
Pukar.introduce()
Pukar.add_project("Expense Tracker")
Pukar.add_project("Tally to Google Sheet Automation")
Pukar.add_project("Business Email Generator")
Pukar.add_project("Personal Portfolio Website")
Pukar.show_projects()
Pukar.pitch()
