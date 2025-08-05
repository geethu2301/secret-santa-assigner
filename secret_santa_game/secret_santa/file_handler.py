import pandas as pd
import os
import csv
from typing import List, Tuple
from .employee import Employee

class FileHandler:
    @staticmethod
    def read_employees(filepath: str) -> List[Employee]:
        if not os.path.exists(filepath):
            raise FileNotFoundError(f"File not found: {filepath}")

        try:
            df = pd.read_excel(filepath)
            employees = []
            for _, row in df.iterrows():
                employees.append(Employee(
                    name=row['Employee_Name'].strip(),
                    email=row['Employee_EmailID'].strip()
                ))
            return employees
        except Exception as e:
            raise ValueError(f"Error reading employee file: {e}")

    @staticmethod
    def read_previous_assignments(filepath: str) -> List[Tuple[str, str]]:
        if not os.path.exists(filepath):
            return []

        try:
            df = pd.read_excel(filepath)
            previous_pairs = []
            for _, row in df.iterrows():
                giver_email = row['Employee_EmailID'].strip()
                receiver_email = row['Secret_Child_EmailID'].strip()
                previous_pairs.append((giver_email, receiver_email))
            return previous_pairs
        except Exception as e:
            raise ValueError(f"Error reading previous assignments: {e}")

    @staticmethod
    def write_assignments(filepath: str, assignments: List[Tuple[Employee, Employee]]):
        try:
            with open(filepath, mode='w', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                writer.writerow(['Employee_Name', 'Employee_EmailID', 'Secret_Child_Name', 'Secret_Child_EmailID'])
                for giver, receiver in assignments:
                    writer.writerow([giver.name, giver.email, receiver.name, receiver.email])
        except Exception as e:
            raise ValueError(f"Error writing output file: {e}")
