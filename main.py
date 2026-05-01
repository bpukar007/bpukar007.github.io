import datetime

def generate_email(name, service, target, problem, tone):
    date = datetime.date.today().strftime("%B %d, %Y")
    
    if tone == "1":
        opening = "I hope this message finds you well."
        closing = "Looking forward to hearing from you."
    elif tone == "2":
        opening = "I'll get straight to the point."
        closing = "Let's talk. I think we can do something great together."
    else:
        opening = "I wanted to reach out personally."
        closing = "I'd love to connect and explore how I can help."

    email = f"""
Date: {date}

Subject: Helping {target} solve {problem}

Hi {target} Team,

{opening}

My name is {name} and I specialize in {service}.

I work with businesses that are struggling with {problem} and help 
them solve it efficiently using Python and AI Automation — saving 
them hours of manual work every single week.

I would love to show you exactly how this works in a free 
15 minute call with zero obligation.

{closing}

Best regards,
Pukar Budhathoki
Python & AI Automation Developer
Portfolio: https://bpukar007.github.io
GitHub: https://github.com/bpukar007
Upwork: https://www.upwork.com/freelancers/~017228f074c44f4f2f
"""
    return email

def main():
    print("================================")
    print("   BUSINESS EMAIL GENERATOR")
    print("   By Pukar Budhathoki")
    print("================================\n")
    
    name = input("Your name: ")
    service = input("Your service: ")
    target = input("Target client name: ")
    problem = input("Problem you solve: ")
    
    print("\nChoose email tone:")
    print("1 - Professional")
    print("2 - Direct and bold")
    print("3 - Personal")
    tone = input("Enter 1, 2 or 3: ")
    
    email = generate_email(name, service, target, problem, tone)
    
    print("\n================================")
    print("YOUR GENERATED EMAIL:")
    print("================================")
    print(email)
    
    save = input("Save email to Desktop? (yes/no): ")
    if save.lower() == "yes":
        with open("/Users/mac/Desktop/generated_email.txt", "w") as file:
            file.write(email)
        print("Saved to your Desktop!")

main()
