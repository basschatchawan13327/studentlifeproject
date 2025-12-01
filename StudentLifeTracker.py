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
    
        student_sessions = data.get("student_sessions",[]) #take data from student_sessions key in json file and put in student_sessions list
        assignments = data.get("assignments",[]) #take data from assignments key in json file and put in assignments list
        expenses = data.get("expenses",[]) #take data from expenses key in json file and put in expenses list
        habits = data.get("habits",[]) #take data from habits key in json file and put in habits list
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
#=================================Khanh part=============================================

#=================================Jenny part=============================================


