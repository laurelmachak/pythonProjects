week = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

janFirst = 4


K = int(input("day (1-365) of year: "))

day = week[(((K%7)-1)+janFirst)%7]

print(day)
