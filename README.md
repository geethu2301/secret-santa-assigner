# Secret Santa Game - Python Project

This project automates Secret Santa assignments among a group of participants. It ensures that each person is assigned a unique secret child (recipient), avoiding self-assignments and preventing repeats from previous years.

## Features

- One-to-one Secret Santa assignments
- Prevents self-assignment
- Avoids repeating last year's pairings
- Input files in `.xlsx` format
- Output file in `.csv` format
- Clean and modular object-oriented design

## Technologies Used

- Python 3.x
- pandas
- openpyxl

## Folder Structure

secret_santa_game/
│
├── data/
│ ├── Employee-List.xlsx
│ └── Secret-Santa-Game-Result-2023.xlsx
│
├── output/
│ └── Secret-Santa-Game-Result-2025.csv ← Generated output
│
├── secret_santa/
│ ├── init.py
│ ├── employee.py
│ ├── file_handler.py
│ ├── assignment.py
│ └── secret_santa_manager.py
│
├── main.py
└── README.md

## How to Run

### 1. Prerequisites

Ensure Python 3 is installed and the required libraries are available:

pip install pandas openpyxl
2. Steps
Place your input Excel files inside the data/ folder:

Employee-List.xlsx

Secret-Santa-Game-Result-2023.xlsx (optional but recommended)

Open terminal or command prompt and navigate to the project directory:


cd C:\Users\HP\OneDrive\Desktop\secret_santa_game
Run the main script:


python main.py
The result will be saved as:


output/Secret-Santa-Game-Result-2025.csv
Input File Formats
Employee-List.xlsx
A list of participants with two columns:

Employee_Name, Employee_EmailID
Alice Smith, alice.smith@example.com
Bob Johnson, bob.johnson@example.com
...
Secret-Santa-Game-Result-2023.xlsx
(Used to avoid duplicate pairings from the previous year)

Employee_Name, Employee_EmailID, Secret_Child_Name, Secret_Child_EmailID
Alice Smith, alice.smith@example.com, Bob Johnson, bob.johnson@example.com
...
Output File Format
The generated CSV file will contain:


Employee_Name, Employee_EmailID, Secret_Child_Name, Secret_Child_EmailID
Design Overview
The code is written using modular object-oriented principles:

Employee class: Represents each participant

FileHandler class: Loads and writes Excel/CSV files

AssignmentEngine class: Assigns Secret Santa pairs while checking constraints

SecretSantaManager class: Orchestrates the whole process

Error Handling
Detects missing or corrupted input files

Prevents duplicate names or emails

Handles impossible assignments (e.g., too few valid pairing options)
