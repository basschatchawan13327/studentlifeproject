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
#=================================Khanh part=============================================

#=================================Jenny part=============================================


