print("Welcome to my  quiz!")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print("Okay! Let's play :)")
score = 0

answer = input("Quand a débuté la Première Guerre mondiale ? ")
if answer.lower() == "1914":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input(" Quand a eu lieu la Saint Barthelemy ? ")
if answer.lower() == "1572":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("Quand a t-on découvert l'Amérique ? ")
if answer.lower() == "1492":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("Quand a débuté la Seconde Guerre Mondiale ? ")
if answer.lower() == "1939":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("Quand a eu lieu la nuit des longs couteaux ? ")
if answer.lower() == "1934":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")
    

print("You got " + str(score) + " questions correct!")
print("You got " + str((score / 5) * 100) + "%.")