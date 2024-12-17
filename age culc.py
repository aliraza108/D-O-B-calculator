name = input("What is your name: ")
year = int(input("What is the year of birth: "))
month = int(input("What is the month of birth: "))
day = int(input("What is the day of birth: "))
to_year = 2022
to_month = 10
to_day = 11

total_input_days = (year * 365) + (month * 30) + day
total_fix_days = (to_year * 365) + (to_month * 30) + to_day

days_total = total_fix_days - total_input_days
months_total = days_total / 30
years_total = days_total / 365

year2 = int(days_total / 365)
month2 = int((days_total - (year2 * 365)) / 30)
day2 = int(days_total - ((year2 * 365) + (month2 * 30)))

print("\n*****---___Date of Birth Calculation___---*****")
print(f"Total years: {int(years_total)}")
print(f"Total months: {int(months_total)}")
print(f"Total days: {days_total}")
print(f"Hey {name}, you are {day2}-{month2}-{year2} days old")
print(f"Year: {year2}")
print(f"Month: {month2}")
print(f"Day: {day2}")
print("*****---___Thanks for visiting___---*****\n")