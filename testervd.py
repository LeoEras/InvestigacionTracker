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

f = file("vary-density.csv", "r")
parse = ""
coor = []
iden = 1
for line in f:
    parse = line.split(" ")
    try:
        if "Cluster1" in parse[2]:
            coor.append([float(parse[0]), float(parse[1]), iden, 0])
            iden = iden + 1
        elif "Cluster2" in parse[2]:
            coor.append([float(parse[0]), float(parse[1]), iden, 1])
            iden = iden + 1
        elif "Cluster3" in parse[2]:
            coor.append([float(parse[0]), float(parse[1]), iden, 2])
            iden = iden + 1
    except:
        continue
f.close()

f = file("results_vd.txt", "w")
it = 0
pc1 = 0
pc2 = 0
pc3 = 0
avg = 0
maxtest = 1000
f.write("####################### " + str(maxtest) + " tests " + "############################\n")
f.write("Test with Vary-Density, forgy K-means\n")
while(it < maxtest):
    mg, mem = km.kmeans(coor, 3, km.distance, "f")

    arr = [cpr(0, 50, 0, mem), cpr(0, 50, 1, mem), cpr(0, 50, 2, mem)]
    greater = arr.index(max(arr))
    arrleft = [cpr(50, 100, 0, mem), cpr(50, 100, 1, mem), cpr(50, 100, 2, mem)]
    greaterleft = arrleft.index(max(arrleft))
    arrright = [cpr(100, 150, 0, mem), cpr(100, 150, 1, mem), cpr(100, 150, 2, mem)]
    greaterright = arrright.index(max(arrright))
        
    results = []
    c1 = 0
    c2 = 0
    c3 = 0
    for i in range(len(coor)):
        if i >= 0 and i < 50:
            if (mem[i] - greater) == coor[i][3]:
                results.append(1)
                c1 += 1
            else:
                results.append(0)
        if i >= 50 and i < 100:
            if (mem[i] - greaterleft + 1) == coor[i][3]:
                results.append(1)
                c2 += 1
            else:
                results.append(0)
        if i >= 100 and i < 150:
            if (mem[i] - greaterright + 2) == coor[i][3]:
                results.append(1)
                c3 += 1
            else:
                results.append(0)
        
    count = 0
    for w in range(len(results)):
        if results[w] == 1: 
            count += 1
            
    pc1 += float(c1)/50
    pc2 += float(c2)/50
    pc3 += float(c3)/50
    avg += float(count)/len(results)
    it += 1

f.write("Average total correct matches of 150 points\n")
f.write("Average total = " + str(avg/maxtest) + "\n\n")
f.write("Average correct matches per cluster\n")
f.write("Cluster 1 = " + str(pc1/maxtest) + "\n")
f.write("Cluster 2 = " + str(pc2/maxtest) + "\n")
f.write("Cluster 3 = " + str(pc3/maxtest) + "\n\n\n")

f.write("Test with Vary-Density, random K-means\n")
it = 0
pc1 = 0
pc2 = 0
pc3 = 0
avg = 0
while(it < maxtest):
    mg, mem = km.kmeans(coor, 3, km.distance, "f")

    arr = [cpr(0, 50, 0, mem), cpr(0, 50, 1, mem), cpr(0, 50, 2, mem)]
    greater = arr.index(max(arr))
    arrleft = [cpr(50, 100, 0, mem), cpr(50, 100, 1, mem), cpr(50, 100, 2, mem)]
    greaterleft = arrleft.index(max(arrleft))
    arrright = [cpr(100, 150, 0, mem), cpr(100, 150, 1, mem), cpr(100, 150, 2, mem)]
    greaterright = arrright.index(max(arrright))
        
    results = []
    c1 = 0
    c2 = 0
    c3 = 0
    for i in range(len(coor)):
        if i >= 0 and i < 50:
            if (mem[i] - greater) == coor[i][3]:
                results.append(1)
                c1 += 1
            else:
                results.append(0)
        if i >= 50 and i < 100:
            if (mem[i] - greaterleft + 1) == coor[i][3]:
                results.append(1)
                c2 += 1
            else:
                results.append(0)
        if i >= 100 and i < 150:
            if (mem[i] - greaterright + 2) == coor[i][3]:
                results.append(1)
                c3 += 1
            else:
                results.append(0)
        
    count = 0
    for w in range(len(results)):
        if results[w] == 1: 
            count += 1
            
    pc1 += float(c1)/50
    pc2 += float(c2)/50
    pc3 += float(c3)/50
    avg += float(count)/len(results)
    it += 1

f.write("Average total correct matches of 150 points\n")
f.write("Average total = " + str(avg/maxtest) + "\n\n")
f.write("Average correct matches per cluster\n")
f.write("Cluster 1 = " + str(pc1/maxtest) + "\n")
f.write("Cluster 2 = " + str(pc2/maxtest) + "\n")
f.write("Cluster 3 = " + str(pc3/maxtest))
f.close()
