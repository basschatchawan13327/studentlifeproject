import json
import os

DATA_FILE = "student_life.json"

student_sessions = []
assignments = []
expenses = []
habits = []


def load_data():
    global student_sessions, assignments, expenses, habits
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            data = json.load(f)
    
        student_sessions = data.get("student_sessions",[])
        assignments = data.get("assignments",[])
        expenses = data.get("expenses",[])
        habits = data.get("habits",[])
    else:
        student_sessions = []
        assignments = []
        expenses = []
        habits = []
    return student_sessions, assignments, expenses, habits

def save_data(student_sessions, assignments, expenses, habits):
    data = {
        "student_sessions": student_sessions,
        "assignments": assignments,
        "expenses": expenses,
        "habits": habits
    }
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, ensure_ascii=False, indent = 4)

def get_input(field):
    return input(f"Enter: {field}")

while True :
    print("===Student Life Tracker===\n1. Study\n2. Assignments\3. Expenses\n4. Habits\n5. Weekly Summary\n0. Exit\n")
    main_choice = get_input("")
    
    if main_choice == "0":
        print("Good bye")
        break
    elif main_choice == "1":
        print("1.Add\n2.List\n3.Delete\n")
        s_choice = get_input("")
        if s_choice == "1":
            date = get_input("")
            subject = get_input("")
            duration = get_input("")
            student_sessions, assignments, expenses, habits = load_data()

            student_sessions.append({"date": date, 
                                     "subject": subject, 
                                     "duration": duration})
            
            save_data(student_sessions, assignments, expenses, habits)

        elif s_choice == "2":
            load_data()
            for s in student_sessions:
                print("Date: ", s["date"])
                print("Subject: ", s["subject"])
                print("Duration: ", s["duration"])

        elif s_choice == "3":
            load_data()
            
