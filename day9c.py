
class EmailTemplate:
    def __init__(self, sender_name, service, target_client, problem_solved, tone="professional"):
        super().__init__()  # Beginner-style super call
        self.sender_name = sender_name
        self.service = service
        self.target_client = target_client
        self.problem_solved = problem_solved
        self.tone = tone

class EmailGenerator:
    def __init__(self):
        super().__init__()  # Added super call here too
        self.emails = []
    
    def generate_email(self, template):
        if template.tone == "professional":
            email = f"""
Subject: Quick question about {template.target_client}'s {template.problem_solved}

Hi {template.target_client} Team,

My name is {template.sender_name} and I help businesses like {template.target_client} 
solve {template.problem_solved} through {template.service}.

I noticed that many companies in your space struggle with {template.problem_solved} 
and end up losing time and money as a result.

I have built a solution that directly addresses this and would love 
to show you how it works in a quick 15 minute call.

Would you be open to connecting this week?

Best regards,
{template.sender_name}
Python & AI Automation Developer
GitHub: [https://github.com/bpukar007](https://github.com/bpukar007)
Portfolio: [https://bpukar007.github.io](https://bpukar007.github.io)
"""
        elif template.tone == "direct":
            email = f"""
Subject: Fix your {template.problem_solved} now

{template.target_client} Team,

{template.sender_name} here. I solve {template.problem_solved} with {template.service}.

Your competitors lose money on this. I fix it.

15 min call this week?

{template.sender_name}
Python & AI Automation Developer
"""
        elif template.tone == "personal":
            email = f"""
Subject: Hey {template.target_client} - about your {template.problem_solved}

Hi {template.target_client} Team,

I'm {template.sender_name} and I've been helping companies just like yours with {template.service}.

I saw you're probably dealing with {template.problem_solved} too - it's super common and costly.

Want me to show you my solution? Just 15 minutes :)

Cheers,
{template.sender_name}
Python & AI Automation Developer
"""
        else:
            email = self.generate_email(EmailTemplate(template.sender_name, template.service, 
                                                    template.target_client, template.problem_solved, "professional"))
        
        self.emails.append(email)
        return email
    
    def save_all_emails(self, filename="generated_emails.txt"):
        with open(filename, "w") as file:
            for i, email in enumerate(self.emails, 1):
                file.write(f"=== EMAIL {i} ===\n")
                file.write(email)
                file.write("\n" + "="*50 + "\n\n")
        print(f"All {len(self.emails)} emails saved to {filename}")
    
    def show_all_emails(self):
        if not self.emails:
            print("No emails generated yet.")
            return
        print(f"\n=== {len(self.emails)} GENERATED EMAILS ===\n")
        for i, email in enumerate(self.emails, 1):
            print(f"--- EMAIL {i} ---")
            print(email)
            print("-" * 50)
    
    def count_emails(self):
        return len(self.emails)

def main():
    generator = EmailGenerator()
    
    print("=== Business Email Generator (OOP) ===")
    print("By Pukar Budhathoki\n")
    
    sender_name = input("Enter your name: ") or "Pukar Budhathoki"
    
    while True:
        print("\n(1) Professional (2) Direct (3) Personal")
        tone_choice = input("Choose tone (1-3) or 'q' to quit: ").strip()
        
        if tone_choice.lower() == 'q':
            break
        
        service = input("Enter your service: ")
        target = input("Enter target client name: ")
        problem = input("Enter the problem you solve: ")
        
        tone_map = {"1": "professional", "2": "direct", "3": "personal"}
        tone = tone_map.get(tone_choice, "professional")
        
        template = EmailTemplate(sender_name, service, target, problem, tone)
        email = generator.generate_email(template)
        
        print("\n=== YOUR GENERATED EMAIL ===")
        print(email)
    
    print(f"\nTotal emails generated: {generator.count_emails()}")
    
    generator.show_all_emails()
    
    save_choice = input("\nSave all emails to file? (y/n): ").strip().lower()
    if save_choice == 'y':
        generator.save_all_emails()
    
    print("Done!")

main()

