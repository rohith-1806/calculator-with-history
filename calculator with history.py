HISTORY_FILE = "history.txt"

def show_history():
    try:
        with open(HISTORY_FILE, 'r') as file:
            lines = file.readlines()
            if not lines:
                print("No history found")
            else:
                for line in reversed(lines):
                    print(line.strip())
    except FileNotFoundError:
        print("No history found")

def clear_history():
    with open(HISTORY_FILE, 'w'):
        pass
    print("Your calculation history was cleared")

def save_to_history(equation, result):
    with open(HISTORY_FILE, 'a') as file:
        file.write(f"{equation} = {result}\n")

def calculate(user_input):
    parts = user_input.split()

    if len(parts) != 3:
        print("Invalid input. Example: 5 + 3")
        return

    try:
        num1 = float(parts[0])
        op = parts[1]
        num2 = float(parts[2])
    except ValueError:
        print("Please enter valid numbers")
        return

    if op == "+":
        result = num1 + num2
    elif op == "-":
        result = num1 - num2
    elif op == "*":
        result = num1 * num2
    elif op == "/":
        if num2 == 0:
            print("Cannot divide by zero")
            return
        result = num1 / num2
    elif op == "%":
        result = num1 % num2
    else:
        print("Invalid operator. Use + - * / %")
        return

    if result == int(result):
        result = int(result)

    print("Your result is:", result)
    save_to_history(user_input, result)

def main():
    print("WELCOME TO Simple Calculator with Python")
    print("(type history, clear, or exit)\n")

    while True:
        user_input = input("Enter calculation or command: ").strip().lower()

        if user_input == "exit":
            print("Thank you for using our service")
            break
        elif user_input == "history":
            show_history()
        elif user_input == "clear":
            clear_history()
        else:
            calculate(user_input)

main()
