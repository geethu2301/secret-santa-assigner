from secret_santa.secret_santa_manager import SecretSantaManager

def main():
    employee_file = 'data/Employee-List.csv'
    previous_file = 'data/Secret-Santa-Game-Result-2023.csv'
    output_file = 'output/Secret-Santa-Game-Result-2025.csv'

    try:
        manager = SecretSantaManager(employee_file, previous_file, output_file)
        manager.run()
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
