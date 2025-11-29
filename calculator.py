def get_number(prompt):
    
    while True:
        try:
            user_input = input(prompt)
            number = float(user_input)
            return number
        except ValueError:
          
            print("  Error: Shudhu number input din please.")



print("Starting the loop...")


while True:
    print("\n")
    print("----- OPTIONS -----")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Stop")
    print("-------------------")
    
    choice = input("Enter your choice (1-5): ")
    

    if choice in ["5", "stop", "exit", "quit"]:
        print("\nThank you for using the calculator. Program is closing.")
        break
        

    if choice not in ["1", "2", "3", "4"]:
        print("  Invalid choice. Please enter a number between 1 and 5.")
        continue


    try:
        num1 = get_number("  Enter the first number: ")
        num2 = get_number("  Enter the second number: ")
        
    except KeyboardInterrupt:
        print("\n\nProgram cancelled by user.")
        break

    result = 0.0
    op_symbol = ""
  
    if choice == "1":
        result = num1 + num2
        op_symbol = "+"
        
    elif choice == "2":
        result = num1 - num2
        op_symbol = "-"
        
    elif choice == "3":
        result = num1 * num2
        op_symbol = "*"
        
    elif choice == "4":
        op_symbol = "/"
        if num2 == 0:
            result = "Error! Cannot divide by zero."
        else:
            result = num1 / num2
            

    print("\n  -----------------")
    if isinstance(result, str):
       
        print(f"  {result}") 
    else:
   
        print(f"  Result: {num1} {op_symbol} {num2} = {result}")
    
    print("  -----------------")

print("\n done")

