student_scores = [150, 142, 185, 120, 171, 184, 149,
                  24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]
print(range(1, 10))


total_sum_of_score = sum(student_scores)
print(total_sum_of_score)


sumScore = 0
for score in student_scores:
    sumScore += score

print(sumScore)

print(max(student_scores))


# Challenge without using max():

# taking the 0th indices positional value of student_score list in biggestScore
biggestScore = student_scores[0]

# iterating to find the biggest number without the use of max()
for stuScore in student_scores:
    # checking if current positional value in stuScore is bigger than biggestScore
    if stuScore > biggestScore:
        # if the stuScore value is bigger, then place it in biggestScore(update it)
        biggestScore = stuScore


print(f"the biggest score in in student_scores with the use of max(): {
      biggestScore}.")


# literally my actual solution - (thought this was wrong logic proceeded to do the above one).
biggestNumberWif = 0

for eachScore in student_scores:
    if eachScore > biggestNumberWif:
        biggestNumberWif = eachScore

print(biggestNumberWif)
