import sys

n_dice = int(sys.stdin.readline())

match_index = {0:5, 1:3, 2:4, 3:1, 4:2, 5:0}
#[[0, 5], [1, 3], [2, 4]]

side_maxv = [0]*6
upside = [[] for _ in range(6)]

#init
dice = list(map(int, sys.stdin.readline().split()))
for i in range(6):
    dice_up, dice_down = dice[i], dice[match_index[i]]
    upside[i].append(dice[i])
    if dice_up!=6 and dice_down!=6:
        side_maxv[i] += 6
    elif dice_up!=5 and dice_down!=5:
        side_maxv[i] += 5
    else:
        side_maxv[i] += 4

for _ in range(n_dice-1):
    dice = list(map(int, sys.stdin.readline().split()))
    for i in range(6):
        dice_down = upside[i][-1]  #dice.index(dice_up)
        dice_up = dice[match_index[dice.index(dice_down)]]
        upside[i].append(dice_up)
        if dice_up!=6 and dice_down!=6:
            side_maxv[i] += 6
        elif dice_up!=5 and dice_down!=5:
            side_maxv[i] += 5
        else:
            side_maxv[i] += 4
print(max(side_maxv))




