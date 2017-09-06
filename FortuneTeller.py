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

while ageInt < 1 or ageInt > 120:
    if ageInt < 1:
        while ageInt < 1:
            age = getNumber("Your age has to be greater than zero.\n  Please enter a valid age: ")
        continue
    elif ageInt > 120:
        while ageInt > 120:
            age = getNumber("No one lives longer than 120 years.  What is your real age? ")
        continue
    else:
        break
print()
userBirthMonth = getNumber("What is your 2 digit birth month? ")

if userBirthMonth == "quit":
    quitter()

userIntBirthMonth = int(userBirthMonth)

while userIntBirthMonth < 1 or userIntBirthMonth > 12:
    if userIntBirthMonth < 1:
        userBirthMonth = getNumber("Come on! What is a negative month?""\nPlease enter a valid 2 digit birth month: ")

        continue
    elif userIntBirthMonth > 12:
        userBirthMonth = getNumber("You know there are only 12 months in a year?!?."
                                   "\nPlease enter a valid 2 digit birth month: ")

        continue
    else:
        break

userFavColor = input("What is your favorite color? ")

if userFavColor == "quit":
    quitter()





