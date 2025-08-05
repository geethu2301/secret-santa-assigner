class Employee:
    def __init__(self, name, email):
        self.name = name.strip()
        self.email = email.strip()

    def __eq__(self, other):
        return isinstance(other, Employee) and self.email.lower() == other.email.lower()

    def __hash__(self):
        return hash(self.email.lower())

    def __repr__(self):
        return f"{self.name} <{self.email}>"
