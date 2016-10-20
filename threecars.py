#!encoding=utf8
# 有三辆车比赛，各有70%的概率向前走一步，一共5次机会，打印出3辆车的前行状态

from random import random
 









###########################################
# time = 5
# car_positions = [1, 1, 1]
 
# while time:
#     # decrease time
#     time -= 1
 
#     print ''
#     for i in range(len(car_positions)):
#         # move car
#         if random() > 0.3:
#             car_positions[i] += 1
 
#         # draw car
#         print '-' * car_positions[i]



##########################################


# from random import random
# L = [0]*3
# reduce(lambda ll,_: map(lambda x:(x+1) if random() > 0.3 else x, ll), range(5), L)
