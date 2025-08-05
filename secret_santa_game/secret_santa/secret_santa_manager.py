from secret_santa.file_handler import FileHandler
from secret_santa.assignment import AssignmentEngine

class SecretSantaManager:

    def __init__(self, employee_file, previous_file, output_file):
        self.employee_file = employee_file
        self.previous_file = previous_file
        self.output_file = output_file

    def run(self):
        employees = FileHandler.read_employees(self.employee_file)
        previous = FileHandler.read_previous_assignments(self.previous_file)
        assignments = AssignmentEngine.assign_secret_santa(employees, previous)
        FileHandler.write_assignments(assignments, self.output_file)
        print(f"Secret Santa assignments written to {self.output_file}")
