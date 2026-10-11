from datetime import datetime

print("jorkee0238 Spreadsheet Automation Menu")

print("Please select from an option below:")
print("1. Input Data")
print("2. View Current Date")
print("3. Generate Report")

selection = input()
now = datetime.now()

print(f"You chose {selection} at {now}") 
