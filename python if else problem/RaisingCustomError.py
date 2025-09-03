a=int(input("Enter a number: "))
if a<5 or a>9:
    raise ValueError("Invalid input! Please enter a number between 5 and 9.")