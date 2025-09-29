#we can use inputs to append things like scores in to a list
#we just ask a question, and create a flag to end the input of items on the list
#in our case, we will use -1 to exit the loop
#then we can grab a list of scores and get an average

average = 0
sum = 0
scores = []
score_input = float(input("Please enter a value you wish to add to the scores list. Press -1 and enter to exit "))

while score_input != -1:
    scores.append(score_input)
    score_input = float(input("Please enter another score or -1 to exit "))

#Then I can use a loop to sum all of the scores
for score in scores:
    sum = sum + score

average = sum / len(scores)
print("Your average is", average)