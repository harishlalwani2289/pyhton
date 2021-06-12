import random

# ball_result_list = [0,1,2,3,4,5,6,"No Ball", "Wide", "Wicket"]
#
# print(random.choice(ball_result_list))

result = [0,1,2,3,4,6,'W','N','Wd']

random_output = random.choices(result, weights=[15,15,9,3,8,8,5,3,5],k=60)
print(random_output)