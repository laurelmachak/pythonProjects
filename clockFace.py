#determine angle by which the minute hand turned since the start of the current hour
# 360/60 = 6
#input is degrees hour hand turned since midnight

hourHandDegrees = int(input("degrees hour hand turned since midnight: "))

hours = hourHandDegrees//30

print("hour", hours)

minutes = (hourHandDegrees%30)*2

print("minutes", minutes)

minuteHandDegrees = minutes*6

print("degrees of minute hand", minuteHandDegrees)
