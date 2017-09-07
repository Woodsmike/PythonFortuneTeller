# This project is to tell the future of a user using their input.
# I used two functions:
# 1. Is to let the user type quit anywhere in the program to exit
# 2. is to make sure the user is only allowed to enter numbers for their age and birth month.
def quitter():
    print("Nobody likes a quitter...")
    exit()


def getNumber(prompt):
    while True:
        response = input(prompt).lower()
        if response == "quit":
            quitter()
        else:
            try:
                return int(response)
            except ValueError:
                print("Please enter a valid number or 'quit' to exit.")

# In this first section I am asking the user for their information
print("Welcome, I am Marvin the Marvelous! \nI will tell you predict your future.\nI will tell you when you retire\n"
      "I will tell you what your future transportation will be.\nI will tell you where your vacation house will be"
      "located.\nI will foresee the fortunes that you will acquire.")
print()
print("At any time in this program you may type 'Quit' to end this session")
print()
print("All I need from you is six personal facts.  These must be true, because I will know if you are lying!")
print()

firstName = input("To begin, What is your first Name? ").lower()
print()

if firstName == "quit":
    quitter()

lastName = input("What is your last name? ").lower()

if lastName == "quit":
    quitter()
print()

age = getNumber("What is your age?  Ladies, your age will not be disclosed. ")

if age == "quit":
    quitter()

ageInt = int(age)

# I wanted only reasonable ages entered. The user's age
while ageInt < 1 or ageInt > 120:
    if ageInt < 1:
        while ageInt < 1:
            age = getNumber("Your age has to be greater than zero.\n  Please enter a valid age: ")
            ageInt = int(age)
        continue
    elif ageInt > 120:
        while ageInt > 120:
            age = getNumber("No one lives longer than 120 years.  What is your real age? ")
            ageInt = int(age)
        continue
    else:
        break
print()
userBirthMonth = getNumber("What is your 2 digit birth month? ")

if userBirthMonth == "quit":
    quitter()

userIntBirthMonth = int(userBirthMonth)
# The user had to enter a valid birth month which was used to determine the money in the user's retirement account.
while userIntBirthMonth < 1 or userIntBirthMonth > 12:
    if userIntBirthMonth < 1:
        userBirthMonth = getNumber("Come on! What is a negative month?""\nPlease enter a valid 2 digit birth month: ")
        userIntBirthMonth = int(userBirthMonth)
        continue
    elif userIntBirthMonth > 12:
        userBirthMonth = getNumber("You know there are only 12 months in a year?!?."
                                   "\nPlease enter a valid 2 digit birth month: ")
        userIntBirthMonth = int(userBirthMonth)
        continue
    else:
        break

# The user's favorite color was used to determine their future transportation
userFavColor = input("What is your favorite color? ").lower()

if userFavColor == "quit":
    quitter()

# The user was only allowed to pick a color from 'ROYBGIV' colors
while (userFavColor != "red" and userFavColor != "orange" and userFavColor != "yellow" and
       userFavColor != "green" and userFavColor != "blue" and userFavColor != "indigo" and
       userFavColor != "violet" and userFavColor != "help"):
    userFavColor = input("Please enter a 'ROYGBIV' color or enter 'Help': ").lower()
    if userFavColor == "quit":
        quitter()
    if userFavColor == "help":
        print("The following colors are 'ROYGBIV' colors:\nRed, Orange, Yellow, Green, Blue, Indigo, Violet.")
        userFavColor = input("Please enter one of these colors: ")

if userFavColor == "help":  # I had to use this condition just in case the user typed 'help' again
    while (userFavColor != "red" and userFavColor != "orange" and userFavColor != "yellow" and
           userFavColor != "green" and userFavColor != "blue" and userFavColor != "indigo" and
           userFavColor != "violet"):
        userFavColor = input("Please enter a 'ROYGBIV' color: ").lower()
        if userFavColor == "quit":
            quitter()

# The amount of siblings was used to determine the user's retirement location
siblings = input("How many siblings do you have?: ")

siblingCount = int(siblings)

if siblings == "quit":
    quitter()

# This part of the code uses the data entered to tell the user their fortune
# If the user's age is an even int then they will retire in 20 years, if odd the 30 years

retireInYears = ""
if ageInt % 2:
    retireInYears = "20 years"
else:
    retireInYears = "30 years"

# Birth month determines the amount of money the user will have in the bank at retirement

amountOfMoney = ""
if 1 <= userBirthMonth <= 4:
    amountOfMoney = "$1,875,043.10"
elif 4 < userBirthMonth <= 8:
    amountOfMoney = "$1,293,485.67"
elif 8 < userBirthMonth <= 12:
    amountOfMoney = "$1,090,088.80"
else:
    amountOfMoney = "$0"

# The number of siblings will determine their vacation home location.

vacationHome = ""
if siblingCount == 0:
    vacationHome = "Kauai, Hawaii"
elif siblingCount == 1:
    vacationHome = "Viti Levu, Fiji"
elif siblingCount == 2:
    vacationHome = "Toronto, CA"
elif siblingCount == 3:
    vacationHome = "Los Cabos, Mexico"
elif siblingCount > 3:
    vacationHome = "Greece"
else:
    vacationHome = "a foreign Insane Asylum"

# Color selected will determine the user's current mode of transportation
# Used a dictionary to change things up from the if statements above.
transportation = {'red': 'sports car',
                  'orange': 'skateboard',
                  'yellow': 'banana seat bike',
                  'green': 'Honda Prius',
                  'blue': 'Learjet 60 airplane',
                  'indigo': 'helicopter',
                  'violet': 'Mini Cooper'}

userTrans = transportation.get(userFavColor, "")

print("{0} {1} will retire in {2} with {3} in the bank, a vacation home in {4} with a {5}."
      .format(firstName, lastName, retireInYears, amountOfMoney, vacationHome, userTrans))

