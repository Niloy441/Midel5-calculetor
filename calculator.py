def add(num1, num2):
  
    return num1 + num2


def subtract(num1, num2):
   
    return num1 - num2


def multiply(num1, num2):
  
    return num1 * num2


def divide(num1, num2):

    if num2 == 0:
        return "Error: Cannot divide by zero!"
    return num1 / num2



def get_valid_number(prompt):
   
    while True:
        try:
            user_input = input(prompt)
            number = float(user_input)
            return number
        except ValueError:
            print(f"Invalid input: '{user_input}' is not a valid number. Please try again.")


def basic_calculator():
   
    print("\n" + "="*50)
    print("BASIC CALCULATOR")
    print("="*50)
    
    num1 = get_valid_number("Enter the first number: ")
    num2 = get_valid_number("Enter the second number: ")
    
    # Display results in formatted way
    print("\n--- Results ---")
    print(f"{num1} + {num2} = {add(num1, num2)}")
    print(f"{num1} - {num2} = {subtract(num1, num2)}")
    print(f"{num1} * {num2} = {multiply(num1, num2)}")
    
    division_result = divide(num1, num2)
    print(f"{num1} / {num2} = {division_result}")
    print()


class Calculator:
   
    
    def add(self, num1, num2):
        """Add two numbers."""
        return num1 + num2
    
    def subtract(self, num1, num2):
        """Subtract two numbers."""
        return num1 - num2
    
    def multiply(self, num1, num2):
        """Multiply two numbers."""
        return num1 * num2
    
    def divide(self, num1, num2):
       
        if num2 == 0:
            return "Error: Cannot divide by zero!"
        return num1 / num2
    
    def menu(self):
        """Display available calculator options."""
        print("\n" + "="*50)
        print("MENU-DRIVEN CALCULATOR")
        print("="*50)
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exit")
        print("="*50)
    
    def run(self):
       
        print("\n" + "="*50)
        print("WELCOME TO THE CALCULATOR")
        print("="*50)
        
        while True:
            # Display menu
            self.menu()
            
            # Get user choice
            choice = input("Enter your choice (1-5): ").strip()
            
            # Check for exit
            if choice == "5":
                print("\nThank you for using the calculator. Goodbye!")
                break
            
            # Validate choice
            if choice not in ["1", "2", "3", "4"]:
                print("Invalid choice. Please enter a number between 1 and 5.")
                continue
            
            # Get two numbers from user
            try:
                num1 = get_valid_number("Enter the first number: ")
                num2 = get_valid_number("Enter the second number: ")
            except KeyboardInterrupt:
                print("\nCalculation cancelled.")
                continue
            
            # Perform the selected operation
            result = None
            operation_symbol = ""
            
            if choice == "1":
                result = self.add(num1, num2)
                operation_symbol = "+"
            elif choice == "2":
                result = self.subtract(num1, num2)
                operation_symbol = "-"
            elif choice == "3":
                result = self.multiply(num1, num2)
                operation_symbol = "*"
            elif choice == "4":
                result = self.divide(num1, num2)
                operation_symbol = "/"
            
            # Display formatted result
            print(f"\nResult: {num1} {operation_symbol} {num2} = {result}\n")


if __name__ == "__main__":
    # Create a Calculator object
    calculator = Calculator()
    
    # Start the calculator by calling the run() method
    calculator.run()
