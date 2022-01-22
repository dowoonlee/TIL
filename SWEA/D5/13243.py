from itertools import combinations

t = int(input())

def TC_sec(pos):
    p1, p2, p3 = pos[0], pos[1], pos[2]
    d12 = abs(p1[0]-p2[0]) + abs(p1[1] - p2[1])
    d13 = abs(p1[0]-p3[0]) + abs(p1[1] - p3[1])
    d23 = abs(p2[0]-p3[0]) + abs(p2[1] - p3[1])
    if d12==d13 and d13==d23:
        return 1
    else:
        return 0

for num_prob in range(1, t + 1):
    H, W = map(int, input().split())
    position = []
    for x in range(H, 0, -1):
        tiles = str(input())
        for j, y in enumerate([k for k in range(1, len(tiles)+1)]):
            if tiles[j] =='#':
                position.append((x, y))
    comb = list(combinations(position, 3))
    ans = 0
    for combo in comb:
        ans += TC_sec(combo)
    print("#%d %d"%(num_prob, ans))



