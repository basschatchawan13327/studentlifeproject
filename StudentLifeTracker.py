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
    elif choice == "3" :                                    #misspelling fixed here main_choice not choice
        print("1. Add\n2. List\n3. Total\n") 
        e_choice = get_input("")            #inside the get_input("") please add "Enter your choice: to display when asking for input"

        if e_choice == "1" :
            date = get_input("")            #please add "Date (YYYY-MM-DD):  " inside get_input("")
            category = get_input("")    #please add "Amount (VND): " inside get_input("")
            amount = get_input("")          #please add "Category: " inside get_input("")
            expenses.append ({"date": date, "category": category, "amount":amount}) #please switch amount to the second position in list and move category to the third position

    elif e_choice == "2" :              # be sure it is in the correct indentation level
        for e in expenses:
            print("Date: ", e["date"])          #please add "\n" before printing each expense for better readability, put it in front of "Date: "
            print("Category: ", e["category"])
            print("Amount: ", e["amount"])

    elif e_choice == "3" :            # be sure it is in the correct indentation level
        total = 0
        for e in expenses:
            total = total + e["amount"]
            print("Total= ", total)             #modified to ("Total Expenses: , format_vnd(total), " VND")

    elif choice == "4" :                               #misspelling fixed here main_choice not choice
        print("1. Add Habit\n2. Record Today\n3. View Stats\n")
        h_choice = get_input("")

        if h_choice == "1" :
            habit_name = input("habit_name: ")
            habits.append ({"name": habit_name, "count": 0})

        elif h_choice == "2" :
            index = int(get_input(""))         #please add "Index to record: " inside get_input("")
            habits[index]['count'] += 1         #complete the function by using if..else to check if index is valid

        elif h_choice == "3" :
            for h in habits:                #do like the e_choice == "2" of expenses part 
                print("h")               #delete this line

        elif choice == "5" :                              #misspelling fixed here main_choice not choice
            print("Enter week start date (yyyymmdd): ")     #move the statement inside get_input("")
            start_date = get_input("")              #please change the input to date object using datetime.strptime -> datetime.strptime(get_input("Enter start date(YYYY-MM-DD)"), "%Y%m%d")
            print("Enter week end date (yyyymmdd): ") #remove this line , you have end_date calculated automatically
            end_date = start_date + timedelta(days=6)
            
            print("Study Summary for week")         #please add "\n" after the print statement for better readability
            for s in study_sessions:
                                                #add session_date to convert s["date"] to date object using datetime.strptime for picking correct data
                if s['date'] >= start_date and s['date'] <= end_date:  #check condition again!!!
                    print(s)                    #print the session details like in e_choice == "2" of expenses part

            print("Assignment Due this week")
            for a in assignments:
                                                #add assignment_date to convert a["due_date"] to date object using datetime.strptime for picking correct data
                if a['due_date'] >= start_date and a['due_date'] <= end_date: #check condition again!!!
                    print(a)                    #print the assignment details like in e_choice == "2" of expenses part

            print("Expenses Summary for week")
              total_week = 0
                for e in expenses:
                                                #add expense_date to convert e["date"] to date object using datetime.strptime for picking correct data
                if e['date'] >= start_date and e['date'] <= end_date: #check condition again!!!
                    print(e)                #print the expense details like in e_choice == "2" of expenses part

            print("Habits Stats")           #add "\n" after the print statement for better readability
            for h in habits:
                    print(h)                #print the habit details like in h_choice == "2" of expenses part

        else:
            print("Invalid choice")
#=================================End of Jenny part======================================
    save_data(student_sessions, assignments, expenses, habits) #saving data after each loop iteration
