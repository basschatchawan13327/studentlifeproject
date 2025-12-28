# studentlifeproject# Student Life Tracker
Student Life Tracker is **a command-line Python application** designed to help students manage their daily academic and personal activities.

The program allows users to record and track:

1. Student sessions

2. Assignments

3. Expenses

4. Habits

5. Weekly Summaries

## Table of content

- [Features](#features)
- [How to run the program](#how-to-run-the-program)
- [Testing Summary](#testing-summary)
- [Team Members](#team-members)

## Features

- Menu-based navigation system

- Add, view, update and delete study sessions

- Assignment tracking with completion status

- Expense tracking with formatted VND currency display

- Habit tracking and progress counting

- Weekly summary combining multiple data categories

- Persistent data storage using a JSON file

- Input validation to prevent invalid or unexpected user input

  
## How to run the Program

  
**Requirements**

- Python 3.13.7 or lastest version

**Steps**

If you don't have **Python3** on your computer:

1. Download **Python 3 Installer** from link : [Click here](https://www.python.org)

![Downloading Python](pictures/download-python.png)

---
2. Open **Installer** and click **Install Python**
 
![Downloading Python](pictures/Install-python.png)

---
3. Type **"Y"** and press Enter

![Downloading Python](pictures/Install-python-2.png)

---
4. Type **"Y"** if you want to view online help or type **"N"** to close windows and end installation.
   
![Downloading Python](pictures/Install-python-3.png)  

---
If you have **Python3** on your computer already:

1. Open **Command Prompt (Windows)** or **Terminal (MacOS)**

For MacOS :

1. Press **Command key (⌘) + Space Bar** to open Sportlight search
2. Type **"Terminal"** and press Enter

![Downloading Python](pictures/terminal.png)
*Figure 1: How to open Termilnal on MacOS

---
For Windows : 

1. Press **Windows** to open Menu
2. Type **"cmd"** and press Enter

![Downloading Python](pictures/cmd.png)
*Figure 2: How to open Command Prompt on Windows 11

---
2. Download the project

Download by Git enter this command:

```
git clone https://github.com/basschatchawan13327/studentlifeproject.git
```

or

Download by GitHub Website

Click on the **green button "<> Code"** and **download as zip** or [Click here](https://github.com/basschatchawan13327/studentlifeproject/archive/refs/heads/main.zip) 

3. Navigate to the project directory.
```
cd studentlifeproject
```

5. Run the program using the following command:
```
python3 StudentLifeTracker.py
```
  
(The data file **"student_life.json"** will be created automatically if it does not already exist.)

  
## Testing Summary

- **Main Menu**
  
  ![Student Life Tracker Main Menu](pictures/main-menu.png)

- **Study Session Function**
  
  ![Study Session Main Menu](pictures/study-session.png)
  
    - **Add**
      
      ![Study Session Add](pictures/study-session-add.png)
      
    - **List**
      
      ![Study Session List](pictures/study-session-list.png)
      
    - **Delete**
      
      ![Study Session Delete](pictures/study-session-delete.png)
      
- **Assignment Function**
  
  ![Assignment Main Menu](pictures/assignment.png)
  
    - **Add**
      
      ![Assignment Add](pictures/assignment-add.png)
      
    - **List**
      
      ![Assignment List](pictures/assignment-list.png)
      
    - **Done**
      
      ![Assignement Done1](pictures/assignment-done-1.png)
      
      Select the index to mark as done :
      
      ![Student Life Tracker Main Menu](pictures/assignment-done-2.png)
      
      Result :
      
      ![Student Life Tracker Main Menu](pictures/assignment-done-3.png)
      
    - **Delete**
      
      ![Student Life Tracker Main Menu](pictures/assignment-delete-1.png)
      
      ![Student Life Tracker Main Menu](pictures/assignment-delete-2.png)
      
- **Expenses Function**
  
  ![Student Life Tracker Main Menu](pictures/expense-menu.png)
  
    - **Add**
      
      ![Student Life Tracker Main Menu](pictures/expense-add.png)
      
    - **List**
      
      ![Student Life Tracker Main Menu](pictures/expense-list.png)
      
    - **Total**
      
      ![Student Life Tracker Main Menu](pictures/expense-total.png)
      
- **Habits Funtion**
  
  ![Student Life Tracker Main Menu](pictures/habit-menu.png)
  
    - **Add**
      
      ![Student Life Tracker Main Menu](pictures/habit-add.png)
      
    - **Record**
      
      ![Student Life Tracker Main Menu](pictures/habit-record.png)
      
    - **View Stats**
      
      ![Student Life Tracker Main Menu](pictures/habit-stats.png)
      
- **Weekly Summaries**
  
  ![Student Life Tracker Main Menu](pictures/weekly-summary.png)

## Team Members

- Chatchawan Jiamprasut **(Project Leader)**
- Truong Gia Khanh **(Collaborator 1)**
- Tran Nguyen Kim Thuy **(Collaborator 2)**
