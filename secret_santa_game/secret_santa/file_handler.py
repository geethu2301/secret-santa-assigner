import csv
from secret_santa.employee import Employee

class FileHandler:

    @staticmethod
    def read_employees(file_path):
        employees = []
        try:
            with open(file_path, mode='r', newline='', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    employees.append(Employee(row['Employee_Name'], row['Employee_EmailID']))
        except Exception as e:
            raise Exception(f"Error reading employee file: {e}")
        return employees

    @staticmethod
    def read_previous_assignments(file_path):
        previous_pairs = {}
        try:
            with open(file_path, mode='r', newline='', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    giver = Employee(row['Employee_Name'], row['Employee_EmailID'])
                    receiver = Employee(row['Secret_Child_Name'], row['Secret_Child_EmailID'])
                    previous_pairs[giver] = receiver
        except Exception as e:
            raise Exception(f"Error reading previous assignment file: {e}")
        return previous_pairs

    @staticmethod
    def write_assignments(assignments, file_path):
        try:
            with open(file_path, mode='w', newline='', encoding='utf-8') as file:
                fieldnames = ['Employee_Name', 'Employee_EmailID', 'Secret_Child_Name', 'Secret_Child_EmailID']
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                writer.writeheader()
                for giver, receiver in assignments.items():
                    writer.writerow({
                        'Employee_Name': giver.name,
                        'Employee_EmailID': giver.email,
                        'Secret_Child_Name': receiver.name,
                        'Secret_Child_EmailID': receiver.email
                    })
        except Exception as e:
            raise Exception(f"Error writing result file: {e}")
