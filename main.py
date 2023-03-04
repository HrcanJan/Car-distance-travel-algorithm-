import sys
sys.setrecursionlimit(1500)

with open('./ADS2021_cvicenie2data.txt') as f:
    towns = f.readlines()[:]

arr = []

def createArray():
    global towns
    for i in range(len(towns)):
        x = towns[i].split()
        x = list(map(int, x))
        arr.append(x[0])

createArray()

def getPenalty(i):
    return (400 - i) ** 2

def funIteration():
    memo = [-1] * (len(arr))
    memo[0] = 0
    stays = [0] * (len(arr))
    count = 0

    for i in range(len(arr)):
        penalty = getPenalty(arr[i])
        for j in range(i):
            tmp = memo[i - j] + getPenalty(arr[i] - arr[i - j])
            if(tmp < penalty):
                penalty = tmp
        
        memo[i] = penalty

    print(memo)
    return penalty

print(funIteration())