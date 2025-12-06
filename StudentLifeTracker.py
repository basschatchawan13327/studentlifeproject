import json
import os
from typing import List, Dict
from datetime import datetime, timedelta

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
    elif choice == "3" :
        print("1. Add\n2. List\n3. Total\n") 
        e_choice = get_input("")

        if e_choice == "1" :
            date = get_input("")
            category = get_input("")
            amount = get_input("")
            expenses.append ({"date": date, "category": category, "amount":amount})

    elif e_choice == "2" :
        for e in expenses:
            print("Date: ", e["date"])
            print("Category: ", e["category"])
            print("Amount: ", e["amount"])
    elif e_choice == "3" :
        total = 0
        for e in expenses:
            total = total + e["amount"]
            print("Total= ", total)

    elif choice == "4" :
        print("1. Add Habit\n2. Record Today\n3. View Stats\n")
        h_choice = get_input("")

        if h_choice == "1" :
            habit_name = input("habit_name: ")
            habits.append ({"name": habit_name, "count": 0})

        elif h_choice == "2" :
            index = int(get_input(""))
            habits[index]['count'] += 1

        elif h_choice == "3" :
            for h in habits:
                print("h")

        elif choice == "5" :
            print("Enter week start date (yyyymmdd): ")
            start_date = get_input("")
            print("Enter week end date (yyyymmdd): ")
            end_date = start_date + timedelta(days=6)
            
            print("Study Summary for week")
            for s in study_sessions:
                if s['date'] >= start_date and s['date'] <= end_date:
                    print(s)

            print("Assignment Due this week")
            for a in assignments:
                if a['due_date'] >= start_date and a['due_date'] <= end_date:
                    print(a)

            print("Expenses Summary for week")
              total_week = 0
                for e in expenses:
                if e['date'] >= start_date and e['date'] <= end_date:
                    print(e)

            print("Habits Stats (overall, simple)")
            for h in habits:
                    print(h)

        else:
            print("Invalid choice")