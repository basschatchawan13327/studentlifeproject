import json
import os
from typing import List, Dict
from datetime import datetime, timedelta

DATA_FILE = "student_life.json"

student_sessions = [] #empty list to hold data from student_life.json
assignments = []
expenses = []
habits = []

#==================== Data Loading and Saving Functions =========================

def load_data():  # Load data from JSON file or initialize empty lists
    global student_sessions, assignments, expenses, habits

    default_data = {
        "student_sessions": [],
        "assignments": [],
        "expenses": [],
        "habits": []
    }

    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            try:
                data = json.load(f)
            except json.JSONDecodeError:
                data = {}
    else:
        data = {}

    # fill missing keys with default empty lists
    for key, value in default_data.items():
        if key not in data:
            data[key] = value

    student_sessions = data["student_sessions"]
    assignments = data["assignments"]
    expenses = data["expenses"]
    habits = data["habits"]

    return student_sessions, assignments, expenses, habits

def save_data(student_sessions, assignments, expenses, habits):     #saves data to student_life.json
    data = {
        "student_sessions": student_sessions,
        "assignments": assignments,
        "expenses": expenses,
        "habits": habits
    }
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, ensure_ascii=False, indent = 4)

#==================== Utility Functions =========================

def get_input(field):                                   
    return input(f"Enter: {field}")

def format_vnd(amount):                                 #function to format VND currency with dot as thousand separator
    return f"{int(round(amount)):,}".replace(",", ".")

#==================== Validation Function =========================

def check_date_format(date_text):                   #function to check if date is in correct format
    try:
        datetime.strptime(date_text, "%Y-%m-%d")
        return True
    except ValueError:
        return False
    
def check_positive_integer(value):                  #function to check if input is a positive integer
    try:
        val = int(value)
        return val >= 0
    except ValueError:
        return False
    
def check_non_empty_string(value):                  #function to check if input is a non-empty string
    return isinstance(value, str) and len(value.strip()) > 0

def check_list_index(index, lst):                   #function to check if input index is valid for a given list
    try:
        idx = int(index)
        return 0 <= idx < len(lst)
    except ValueError:
        return False
    
def check_integer(value):                           #function to check if input is an integer
    try:
        int(value)
        return True
    except ValueError:
        return False
    
def check_duration(value):                          #function to check if input duration is a positive integer greater than zero
    try:
        val = int(value)
        return val > 0
    except ValueError:
        return False
    
def check_amount(value):                            #function to check if input amount is a positive integer greater than zero
    try:
        val = int(value)
        return val > 0
    except ValueError:
        return False
    
def check_noseperator(value):                       #function to check if input string contains no separator characters
    separators = ['.', ',', ' ']
    for sep in separators:
        if sep in value:
            return False
    return True

#==================== Main Program Loop =========================
# Display main menu and route user to selected feature

student_sessions, assignments, expenses, habits = load_data()           #loading data to lists at the start of the program

while True :                     #main menu loop
    print("\n===Student Life Tracker===\n1. Study\n2. Assignments\n3. Expenses\n4. Habits\n5. Weekly Summary\n0. Exit\n")
    main_choice = get_input("")
    if not check_integer(main_choice):
        print("Invalid input, Please put a number 0-5.")
        continue
    elif main_choice not in ["0", "1", "2", "3", "4", "5"]:
        print("Invalid choice, Please put a number 0-5.")
        continue

#==================== Exiting the Program =========================

    if main_choice == "0":                         
        save_data(student_sessions, assignments, expenses, habits)
        print("\nGood bye")
        break
    
#==================== Study Session Menu =========================

    elif main_choice == "1":
        print("=====Study Session Tracker=====\n")                         
        print("1.Add\n2.List\n3.Delete\n4.Back\n")
        while True:                 
            s_choice = get_input("")
            if not check_integer(s_choice):
                print("Invalid input, Please put a number 1-4.")
                continue
            elif s_choice not in ["1", "2", "3", "4"]:
                print("Invalid choice, Please put a number 1-4.")
                continue
            else:
                break

        if s_choice == "1":
            print("=====Adding a new study session=====\n")                        
            while True:                 
                date = get_input("Date (YYYY-MM-DD): ")
                if not check_date_format(date):
                    print("Invalid date format or input, Please enter YYYY-MM-DD.")
                    continue

                subject = get_input("Subject: ")
                if not check_non_empty_string(subject):
                    print("Invalid subject input, Please enter a non-empty string.")
                    continue

                duration = get_input("Duration (in minutes): ")           
                if not check_integer(duration):
                    print("Invalid duration input, Please enter an integer.")
                    continue
                elif not check_positive_integer(duration):
                    print("Duration must be a positive integer.")
                    continue
                elif check_duration(duration) == False:
                    print("Duration must be greater than zero.")
                    continue
                duration = int(duration)

                student_sessions.append({"date": date, 
                                     "subject": subject, 
                                     "duration": duration})
                break

        elif s_choice == "2":
            print("=====Listing all study sessions=====\n")                         
            for s in student_sessions:
                print("\nDate: ", s["date"])
                print("Subject: ", s["subject"])
                print("Duration: ", s["duration"]//60, "Hrs", s["duration"]%60, "mins\n")
                print("-" * 20)

        elif s_choice == "3":
            print("=====Deleting a study session=====\n")                         
            for s in student_sessions:              
                print("\nIndex: ", student_sessions.index(s))
                print("Date: ", s["date"])
                print("Subject: ", s["subject"])
                print("Duration: ", s["duration"]//60, "Hrs", s["duration"]%60, "mins\n")
                print("-" * 20)

            index = get_input("index to delete (Press Enter to cancel): ")
            if index == "":
                print("Cancelled deletion")
            elif not check_integer(index):
                print("Invalid input please enter a number")
            elif not check_list_index(index, student_sessions):
                print("Invalid index")
            else:
                del student_sessions[int(index)]

        elif s_choice == "4":
            print("Returning to main menu\n")
            continue

#==================== Assignments Menu =========================

    elif main_choice == "2":
        print("=====Assignment Tracker=====\n")                        
        print("1.Add\n2.List\n3.Complete\n4.Delete\n5.Back\n")
        while True:                 
            a_choice = get_input("")
            if not check_integer(a_choice):
                print("Invalid input, Please put a number 1-5.")
                continue
            elif a_choice not in ["1", "2", "3", "4", "5"]:
                print("Invalid choice, Please put a number 1-5.")
                continue
            else:
                break

        if a_choice == "1":
            print("=====Adding a new assignment=====\n")
            while True:                         
                title = get_input("Assignment Title: ")
                if not check_non_empty_string(title):
                    print("Assignment name can't be blank")
                    continue
                due_date = get_input("Due Date (YYYY-MM-DD): ")
                if not check_date_format(due_date):
                    print("Invalid date format or input, Please enter YYYY-MM-DD.")
                    continue
                assignments.append({"title": title, 
                                    "due_date": due_date, 
                                    "Done": False})
                break

        elif a_choice == "2":
            print("=====Listing all assignments=====\n")                         
            for a in assignments:
                print("\nTitle: ", a["title"])
                print("Due Date: ", a["due_date"])
                print("Done: ", a["Done"], "\n")
                print("-" * 20)

        elif a_choice == "3":
            print("=====Marking an assignment as complete=====\n")
            for a in assignments:              
                print("\nIndex: ", assignments.index(a))
                print("Title: ", a["title"])
                print("Due Date: ", a["due_date"])
                print("Done: ", a["Done"], "\n")
                print("-" * 20)

            index = get_input("Index to mark as complete: ")
            if not check_integer(index):
                print("Invalid input please enter a number")
            elif not check_list_index(index, assignments):
                print("Invalid index")
            else:
                assignments[int(index)]["Done"] = True

        elif a_choice == "4":
            print("=====Deleting an assignment=====\n")                         
            for a in assignments:                     
                print("\nIndex: ", assignments.index(a))
                print("Title: ", a["title"])
                print("Due Date: ", a["due_date"])
                print("Done: ", a["Done"], "\n")
                print("-" * 20)

            index = get_input("Index to delete (Press Enter to cancel): ")
            if index == "":
                print("Cancelled deletion")
            elif not check_integer(index):
                print("Invalid input please enter a number")
            elif not check_list_index(index, assignments):
                print("Invalid index")
            else:
                del assignments[int(index)]

        elif a_choice == "5":
            print("Returning to main menu\n")
            continue