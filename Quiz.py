print("Hi Austin")

name = input("What is your name? ")

playing = input("Do you want to play, " + name + "? ")

if playing.upper() != "YES":
    quit("Fuck you then. Bye!")
else:
    print("Okay, let's fucking do this then!")
print()

score = 0

print()

answer = input("Question #1: \n Do you love Joshua Nelson Vazquez? ")
if answer.upper() == "YES":
    print("\tCORRECT, GOOD JOB!")
    score += 1
else:
    print("\tINCORRECT, TRY AGAIN!")

print()

answer = input("Question #2: \n Would you do anything for him? ")
if answer.upper() == "YES":
    print("\tThat's what I'm talking about!")
    score += 1
else:
    print("\tINCORRECT, TRY AGAIN!")

print()

answer = input("\tHow about anal? ")
if answer.upper() == "YES":
    answer_one = input("\t\tWow really??? ")
    if answer_one.upper() != "YES":
        answer_two = input("\t\tAwesome, when?!! ")
    print("\tWOW, okay then!")
else:
    print("Just kidding, moving on.")

print()

answer = input("Question 3: What is 2 + 2? ")
if answer == "4":
    print("Correct, I'm proud of you!!")
    score += 1
else:
    print("TRY AGAIN!\n^^^Not the question, I mean kindergarten.' ")

print()

answer = input("Do you want to love me forever?? ")
if answer.upper() == "YES":
    print("Aw, I love you too!!")
    score += 1
else:
    print(" :( ")

print()

answer = input("Did you enjoy your time on this program? ")
if answer.upper() == "YES":
    print("Good, I'm glad!")
    score += 1
else:
    print("Wow, Biiiiiitch!")

print("You got " + str(score/4 * 100) + "%")
