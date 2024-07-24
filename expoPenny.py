numDays = input("How many days will you need to double your money? ")
xNumDays = 1
xNumPayments = 0.01
while xNumDays < int(numDays):
    print("It is day " + (str(xNumDays) + " and you will double what you have today."))
    print("You will double your $" + (str(xNumPayments) + " and it will show the next day... "))
    xNumDays += 1
    xNumPayments *= 2
    print("It's a new day,\nDay Number " + (str(xNumDays) + "."))
    print("New balance is | $" + (str(xNumPayments) + " |."))
if xNumDays >= 30:
    print("That's right! \nYou should have $" + str(xNumPayments) + "! That's a lot of money!...")
elif xNumDays >= 20:
    print("That's right! \nYou should have $" + str(xNumPayments) + "! That's not too bad!...")
else:
    print("That's right! \nYou should have $" + str(xNumPayments) + "! You could do better!...")