Secret Santa Game - Python Project
This project automates Secret Santa assignments among a group of participants. It ensures that each person is assigned a unique secret child (recipient), avoiding self-assignments and preventing repeats from previous years.

Features
One-to-one Secret Santa assignments

Prevents self-assignment

Avoids repeating last year's pairings

Input and output handled via CSV files

Clean and modular object-oriented design

No external dependencies required

Technologies Used
Python 3

Standard Python libraries (csv, random, os, typing)

Folder Structure
secret_santa_game/
│
├── data/
│   ├── Employee-List.csv
│   └── Secret-Santa-Game-Result-2023.csv
│
├── output/
│   └── Secret-Santa-Game-Result-2025.csv  # Generated after running the program
│
├── secret_santa/
│   ├── __init__.py
│   ├── employee.py
│   ├── file_handler.py
│   ├── assignment.py
│   └── secret_santa_manager.py
│
├── main.py
└── README.md

How to Run
Clone or download this repository

Make sure Python 3 is installed

Place your CSV input files in the data/ folder

Open a terminal or command prompt in the root project folder

Run the program:

python main.py

The result will be saved to:

output/Secret-Santa-Game-Result-2025.csv

Employee-List.csv

Contains the list of participants:

Employee_Name,Employee_EmailID

Alice Smith,alice.smith@example.com
Bob Johnson,bob.johnson@example.com
...

Secret-Santa-Game-Result-2023.csv

Optional file to avoid repeating last year’s assignments:

Employee_Name,Employee_EmailID,Secret_Child_Name,Secret_Child_EmailID
Alice Smith,alice.smith@example.com,Bob Johnson,bob.johnson@example.com
...
Output File Format
The result CSV will contain:


Employee_Name,Employee_EmailID,Secret_Child_Name,Secret_Child_EmailID

Design Overview

The project uses object-oriented programming for scalability and readability:

Employee class: Represents an individual participant

FileHandler class: Reads and writes CSV files

AssignmentEngine class: Handles fair and conflict-free Secret Santa assignments

SecretSantaManager class: Coordinates the overall process

Error Handling
Handles missing or corrupt input files

Prevents duplicate names or emails

Detects and reports assignment impossibilities

License

This project is provided for educational and demonstration purposes.

