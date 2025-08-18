import calendar
year= int(input("Enter the year: "))
month= int(input("Enter the month(in numbers): "))
cal= calendar.month(year, month)
print("\n")
print(cal)