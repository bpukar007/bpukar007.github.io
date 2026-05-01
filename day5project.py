import json
import datetime

def log_day(days, hours, topic, wins):
    entry = {
        "day": days,
        "date": str(datetime.date.today()),
        "hours_studied": hours,
        "topic": topic,
        "wins": wins
    }
    return entry

def show_progress(entries):
    print("==================================")
    print(".    MY CODING JOURNEY LOG.       ")
    print("==================================")
    total_hours = 0
    for entry in entries:
        print(f"\nDay {entry['day']} - {entry['date']}")
        print(f"Topic: {entry['topic']}")
        print(f"Hours: {entry['hours_studied']}")
        print(f"Wins: {entry['wins']}")
        print("----------------------------------")
        total_hours += entry['hours_studied']
    print(f"\n=================================")
    print(f"Total hours invested: {total_hours}")
    print(f"Days completed: {len(entries)}")
    print("===========================")

# Log your actual journey
entries = [
    log_day(1, 6, "Python basics and setup", "First code ever ran"),
    log_day(2, 4.5, "Variables, conditions, portfolio", "Portfolio live on internet"),
    log_day(3, 3, "Functions and loops", "Built from memory"),
    log_day(4, 4, "Lists, dictionaries, file handling", "Pushed to GitHub"),
    log_day(5, 3, "Error handling, APIs, JSON", "First real project built")
]

show_progress(entries)
