import random
from .file_handler import FileHandler
from .employee import Employee

class SecretSantaManager:
    def __init__(self, employee_file: str, previous_file: str, output_file: str):
        self.employee_file = employee_file
        self.previous_file = previous_file
        self.output_file = output_file

    def run(self):
        employees = FileHandler.read_employees(self.employee_file)
        previous_assignments = FileHandler.read_previous_assignments(self.previous_file)
        assignments = self.generate_assignments(employees, previous_assignments)
        FileHandler.write_assignments(self.output_file, assignments)

    def generate_assignments(self, employees, previous_assignments):
        max_attempts = 1000
        for _ in range(max_attempts):
            receivers = employees.copy()
            random.shuffle(receivers)
            assignment = list(zip(employees, receivers))

            if all(giver.email != receiver.email for giver, receiver in assignment) and \
               all((giver.email, receiver.email) not in previous_assignments for giver, receiver in assignment):
                return assignment

        raise Exception("Could not find valid assignments after multiple attempts.")
