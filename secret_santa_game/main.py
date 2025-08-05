import os
from secret_santa.secret_santa_manager import SecretSantaManager

def main():
    base_path = os.path.dirname(os.path.abspath(__file__))
    employee_file = os.path.join(base_path, 'data', 'Employee-List.xlsx')
    previous_file = os.path.join(base_path, 'data', 'Secret-Santa-Game-Result-2023.xlsx')  # optional
    output_file = os.path.join(base_path, 'output', 'Secret-Santa-Game-Result-2025.csv')

    try:
        manager = SecretSantaManager(employee_file, previous_file, output_file)
        manager.run()
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
