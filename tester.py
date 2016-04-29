import examplekmeans as km
import matplotlib.pyplot as plt
import matplotlib.colors as colors
from random import randint
  
def test(fake, value, arr):
    result = []
    if fake == 0:
        for i in range(0, 290):
            if arr[i] == value:
                result.append(1)
            else:
                result.append(0)
        return result
    elif fake == 1:
        for i in range(290, 390):
            if arr[i] == value:
                result.append(1)
            else:
                result.append(0)
        return result
    elif fake == 2:
        for i in range(390, 490):
            if arr[i] == value:
                result.append(1)
            else:
                result.append(0)
        return result

def cpr(start, end, value, arr):
    result = 0
    for w in range(start, end):
        if arr[w] == value:
            result += 1
    return result

f = file("mouse.csv", "r")
parse = ""
coor = []
count_mouse = [290, 100, 100, 10]
iden = 1
for line in f:
    parse = line.split(" ")
    try:
        if "Head" in parse[2]:
            coor.append([float(parse[0]), float(parse[1]), iden, 0])
            iden = iden + 1
        elif "Ear_l" in parse[2]:
            coor.append([float(parse[0]), float(parse[1]), iden, 1])
            iden = iden + 1
        elif "Ear_r" in parse[2]:
            coor.append([float(parse[0]), float(parse[1]), iden, 2])
            iden = iden + 1
        elif "Noi" in parse[2]:
            coor.append([float(parse[0]), float(parse[1]), iden, 3])
    except:
        continue
f.close()

f = file("results_mouse.txt", "w")
it = 0
pcH = 0
pcLE = 0
pcRE = 0
avg = 0
maxtest = 1000
f.write("####################### " + str(maxtest) + " tests " + "############################\n")
f.write("Test with Mouse, forgy K-means\n")
while(it < maxtest):
    mg, mem = km.kmeans(coor, 3, km.distance, "f")

    arr = [cpr(0, 290, 0, mem), cpr(0, 290, 1, mem), cpr(0, 290, 2, mem)]
    greater = arr.index(max(arr))
    arrleft = [cpr(290, 390, 0, mem), cpr(290, 390, 1, mem), cpr(290, 390, 2, mem)]
    greaterleft = arrleft.index(max(arrleft))
    arrright = [cpr(390, 340, 0, mem), cpr(390, 490, 1, mem), cpr(390, 490, 2, mem)]
    greaterright = arrright.index(max(arrright))
        
    results = []
    cH = 0
    cLE = 0
    cRE = 0
    for i in range(len(coor)):
        if i >= 0 and i < 290:
            if (mem[i] - greater) == coor[i][3]:
                results.append(1)
                cH += 1
            else:
                results.append(0)
        if i >= 290 and i < 390:
            if (mem[i] - greaterleft + 1) == coor[i][3]:
                results.append(1)
                cLE += 1
            else:
                results.append(0)
        if i >= 390 and i < 490:
            if (mem[i] - greaterright + 2) == coor[i][3]:
                results.append(1)
                cRE += 1
            else:
                results.append(0)
        
    count = 0
    for w in range(len(results)):
        if results[w] == 1: 
            count += 1
            
    pcH += float(cH)/290
    pcLE += float(cLE)/100
    pcRE += float(cRE)/100
    avg += float(count)/len(results)
    it += 1

f.write("Average total correct matches of 490 points\n")
f.write("Average total = " + str(avg/maxtest) + "\n\n")
f.write("Average correct matches per cluster\n")
f.write("Head cluster = " + str(pcH/maxtest) + "\n")
f.write("Left Ear cluster = " + str(pcLE/maxtest) + "\n")
f.write("Right Ear cluster = " + str(pcRE/maxtest) + "\n\n\n")

f.write("Test with Mouse, random K-means\n")
it = 0
pcH = 0
pcLE = 0
pcRE = 0
avg = 0
while(it < maxtest):
    mg, mem = km.kmeans(coor, 3, km.distance, "r")

    arr = [cpr(0, 290, 0, mem), cpr(0, 290, 1, mem), cpr(0, 290, 2, mem)]
    greater = arr.index(max(arr))
    arrleft = [cpr(290, 390, 0, mem), cpr(290, 390, 1, mem), cpr(290, 390, 2, mem)]
    greaterleft = arrleft.index(max(arrleft))
    arrright = [cpr(390, 340, 0, mem), cpr(390, 490, 1, mem), cpr(390, 490, 2, mem)]
    greaterright = arrright.index(max(arrright))
        
    results = []
    cH = 0
    cLE = 0
    cRE = 0
    for i in range(len(coor)):
        if i >= 0 and i < 290:
            if (mem[i] - greater) == coor[i][3]:
                results.append(1)
                cH += 1
            else:
                results.append(0)
        if i >= 290 and i < 390:
            if (mem[i] - greaterleft + 1) == coor[i][3]:
                results.append(1)
                cLE += 1
            else:
                results.append(0)
        if i >= 390 and i < 490:
            if (mem[i] - greaterright + 2) == coor[i][3]:
                results.append(1)
                cRE += 1
            else:
                results.append(0)
        
    count = 0
    for w in range(len(results)):
        if results[w] == 1: 
            count += 1
            
    pcH += float(cH)/290
    pcLE += float(cLE)/100
    pcRE += float(cRE)/100
    avg += float(count)/len(results)
    it += 1

f.write("Average total correct matches of 490 points\n")
f.write("Average total = " + str(avg/maxtest) + "\n\n")
f.write("Average correct matches per cluster\n")
f.write("Head cluster = " + str(pcH/maxtest) + "\n")
f.write("Left Ear cluster = " + str(pcLE/maxtest) + "\n")
f.write("Right Ear cluster = " + str(pcRE/maxtest))
f.close()
