score = 0

print("Welcome to the Python quiz game!\n")

answer1 = input("What programming language are we using?\n").lower()
if(answer1 == "python"):
    score += 1
    print("Correct!")

else:
    print("Incorrect! The correct answer is Python!")
    

answer2 = input("What color is the sky?\n").lower()
if(answer2 == "blue"):
    score += 1
    print("Correct!")

else:
    print("Incorrect! The correct answer is Python!")
    

answer3 = input("What is the first letter of the alphabet\n").lower()
if(answer3 == "a"):
    score += 1
    print("Correct!")

else:
    print("Incorrect! The correct answer is Python!")
    


print("Your score: ", score, " out of 3")
if(score == 3):
    print("Wow! You are a genius!")

else:
    print("Study up and try again!")
    
print("Thank you for playing :)")