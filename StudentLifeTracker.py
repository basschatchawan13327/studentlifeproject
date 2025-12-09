import json
import os
from typing import List, Dict
from datetime import datetime, timedelta

DATA_FILE = "student_life.json"

student_sessions = []       #empty list to hold data from student_life.json
assignments = []
expenses = []
habits = []


def load_data(): #function to load data from student_life.json if it exists, otherwise initializes empty lists
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

def save_data(student_sessions, assignments, expenses, habits): #function to save data to student_life.json
    data = {
        "student_sessions": student_sessions,
        "assignments": assignments,
        "expenses": expenses,
        "habits": habits
    }
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, ensure_ascii=False, indent = 4)

def get_input(field):   #function to get user input
    return input(f"Enter: {field}")

def format_vnd(amount):
    return f"{int(round(amount)):,}".replace(",", ".")              #function to format number to VND format ex. input 1000000 -> output 1.000.000

student_sessions, assignments, expenses, habits = load_data()       #initialize loading data from student_life.json

while True :
    print("===Student Life Tracker===\n1. Study\n2. Assignments\3. Expenses\n4. Habits\n5. Weekly Summary\n0. Exit\n")
    main_choice = get_input("")
    
    if main_choice == "0":
        print("Good bye")
        break
#=================================Khanh part=============================================

#=================================Jenny part=============================================
    elif main_choice == "3" :                                    
        print("1. Add\n2. List\n3. Total\n")
        e_choice = get_input("Enter your choice: ")

        if e_choice == "1" :
            date = get_input("Date (YYYY-MM-DD): ")
            category = get_input("Amount (VND): ")    
            amount = get_input("Category: ")
            expenses.append ({"date": date, "amount":amount, "category": category})

        elif e_choice == "2" :
            for e in expenses:
                print("\nDate:", e["date"])
                print("Category:", e["category"])
                print("Amount: ", e["amount"])                     

        elif e_choice == "3" :
            total = 0
            for e in expenses:
                total = total + e["amount"]
                print("Total Expenses:  " , format_vnd(total), "VND")

    elif main_choice == "4" :
        print("1. Add Habit\n2. Record Today\n3. View Stats\n")
        h_choice = get_input("")

        if h_choice == "1" :
            habit_name = input("habit_name: ")
            habits.append ({"name": habit_name, "count": 0})

        elif h_choice == "2" :
            index = int(get_input("Index to record: "))
            if  0 <= index < len(habits):
                habits[index]["count"] += 1
            else:
                print("Invalid index")

        elif h_choice == "3" :
            for h in habits:
                print("\nName:", h["name"])
                print("Count:", h["count"])             

    elif main_choice == "5" :
        print("Enter week start date:(YYYY-MM-DD)")
        start_date = datetime.strptime(get_input("Enter start date(YYYY-MM-DD)"), "%Y%m%d")
        end_date = start_date + timedelta(days=6)
            
        print("Study Summary for week\n")
        for s in study_sessions:
            session_date = datetime.strptime(s['date'], "%Y%m%d")
            if start_date <= session_date <= end_date:
                print("\nDate:", s["date"])
                print("Subject:", s["subject"])
                print("Duration:", s["duration"])

        print("Assignment Due this week")
        for a in assignments:
            assignment_date = datetime.strptime(a["due_date"], "%Y%m%d")
            if start_date <= assignment_date <= due_date:
                    print("Title:", a["title"])
                    print("Due date:", a["due_date"])
                    print("Done:", a["done"])

        print("Expenses Summary for week")
        total_week = 0
        for e in expenses:
            expense_date = datetime.strptime(e["date"], "%Y%m%d")
            if start_date <= expense_date <= end_date:
                print("\nDate:", e["date"])
                print("Category:", e["category"])
                print("Amount: ", e["amount"])

            print("Habits Stats\n")
            for h in habits:
                print("Habit:", h["name"])
                print("Times:", h["count"])

        else:
            print("Invalid choice")
#=================================End of Jenny part======================================
    save_data(student_sessions, assignments, expenses, habits) #saving data after each loop iteration
