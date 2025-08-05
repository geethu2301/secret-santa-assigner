import random

class AssignmentEngine:

    @staticmethod
    def assign_secret_santa(employees, previous_assignments):
        if len(employees) < 2:
            raise ValueError("Need at least two employees for Secret Santa!")

        attempts = 1000
        for _ in range(attempts):
            shuffled = employees[:]
            random.shuffle(shuffled)
            assignments = {}
            success = True

            for giver, receiver in zip(employees, shuffled):
                if giver == receiver or previous_assignments.get(giver) == receiver:
                    success = False
                    break
                assignments[giver] = receiver

            if success:
                return assignments

        raise Exception("Unable to generate valid Secret Santa assignments after multiple attempts.")
