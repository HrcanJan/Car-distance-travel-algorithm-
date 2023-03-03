with open('./ADS2021_cvicenie2data.txt') as f:
    towns = f.readlines()[:]

arr = []

def createArray():
    global towns
    for i in range(len(towns)):
        x = towns[i].split()
        x = list(map(int, x))
        arr.append(x)

createArray()

def fun():
    print

fun()