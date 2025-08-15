#X if condition else Y

num = 5
a = 6
b = 7
age = 13
temperature = 30
user_role = "A"

print("positive" if num > 0 else "negative") #positive


result = "EVEN" if num % 2 == 0 else "ODD" #odd
print(result)

max_num = a if a > b else b #7
print(max_num)

min_num = a if a < b else b #6
print(min_num)

status = "Adult" if age >= 18 else  "Child"
print(status)

weather = "HOT" if temperature > 20 else "COLD"
print(weather)

acces_level = "FULL ACCES" if user_role == "ADMIN" else "LIMITED ACCES"
print(acces_level)