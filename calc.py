
totalCal = int(0)
calBurnt = int(0)

qA = input("Would you like to input calories? y/n ")
## Calculates Calories Consumed
while qA.lower() != "n":
    meal = int(input("Input calories of meal: "))
    totalCal = totalCal + meal
    qA = input("Would you like to continue inputting calories? y/n ")
print(str(totalCal) + " calories consumed.")

weight = int(input("Enter Weight (in Pounds): "))
height = int(input("Enter Height: (in inches): "))
age = int(input("Enter Age: "))
gender = input("Enter gender: m/f: ")

def caloriesBurned(w , h , a ,g):
    if g.lower() == "m":
       calBurnt = 66 + (6.2*w) + (2.7*h) - (6.76*a)
    elif g.lower() == "f":
        calBurnt = 655.1 + (4.35*w) + (4.7*h) - (4.7*a)
    else:
        return "Error: incorrect gender input"
    return calBurnt

print(caloriesBurned(weight,height,age,gender))

def calDeficit(calBurnt):
    if (totalCal > calBurnt):
        return(f"You consumed {totalCal - calBurnt} excess Calories.")
    elif totalCal < calBurnt:
        return(f"You are in a caloric deficit by {calBurnt - totalCal} calories")
    else:
        return "You have reached your daily caloric count"
print(caloriesBurned(weight, height, age, gender))
print(calDeficit(caloriesBurned(weight, height, age, gender)))