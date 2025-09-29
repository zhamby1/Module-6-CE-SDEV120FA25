#lets say we have a list of test scores that our students took
#they didnt do so well, so we are adding 5 pts to each score

test_scores = [70,80,90,55]

#first lets display all the test scores with a added 5 pts

# for score in test_scores:
#     score = score + 5
#     print(score)

#so we can solve this problem on of two ways
#1. make a new list and append the changed values

new_scores = []

for score in test_scores:
    score = score + 5
    new_scores.append(score)

print(new_scores) #printing off a list is a debugging feature..not used to separate values

#you can also use a fo in range loop to create a more traditional looping structure
#this allows us to modify the original list, because we can use an index
#the other cool thing is that we may not know the length of list if users have added data to the list
#instead we can use the len() function to grab how many items are in the list to use our loop

for i in range(len(test_scores)):
    test_scores[i] = test_scores[i] + 5

print(test_scores)