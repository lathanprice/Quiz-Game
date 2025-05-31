score = 0

print("Welcome to the Python Quiz Game!\n")

# Question 1
answer1 = input("What programming language are we using?\n").lower()
if answer1 == "python":
    print("Correct!\n")
    score += 1
else:
    print("Incorrect, we're using Python!\n")

# Question 2
answer2 = input("What color is the sky?\n").lower()
if answer2 == "blue":
    print("Correct!\n")
    score += 1
else:
    print("No, the sky is blue!\n")

# Question 3
answer3 = input("What is the first letter of the alphabet?\n").lower()
if answer3 == "a":
    print("Nice job!\n")
    score += 1
else:
    print("Incorrect. The first letter of the alphabet is 'A'.\n")

print(f"You got {score} out of 3 questions correct!")
if(score == 3):
    print("Perfect score! You're a Python expert!")
print("Thanks for playing! :)")