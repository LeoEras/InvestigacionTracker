import re
from datetime import datetime, timedelta
import sys
from random import randint

def randomColor(array):
    return str(array[randint(0,len(array) - 1)])

def loadNodes(dictionary, string):
    fob = open("nodes" + string + ".csv", 'w')
    cont = 0    #El id de los nodos
    fob.write("Id;Label;Start;End\n")

    if "App" in string or "Doc" in string:
        for items in objects:
            if string in items[7]:
                if items[6] != "":
                    if items[6] not in dictionary:
                        dictionary[items[6]] = cont
##                        dateSTR = str(items[1]).split("-", len(items[1]))
##                        dateSTR = "" + dateSTR[2] + "-" + dateSTR[1] + "-" + dateSTR[0]
##                        hourSTR = str(items[2]).split(":", len(items[2]))
##                        hourSTR = "" + hourSTR[0] + ":" + hourSTR[1]
##                        hourEND = str(items[4]).split(":", len(items[4]))
##                        hourEND = "" + hourEND[0] + ":" + hourEND[1]
                        #print(items[1])
                        fob.write(str(cont) + ";" + items[6] + ";" + items[1] + " " + items[2] + ";" + items[3] + " " + items[4] + "\n")
                        cont += 1
    else:
        for items in objects:
            if items[6] != "":
                if items[6] not in dictionary:
                    dictionary[items[6]] = cont
                    fob.write(str(cont) + ";" + items[6] + "\n")
                    cont += 1
    fob.close()

def loadEdges(dictionary, string):
    fob = open("edges" + string + ".csv", 'w')
    fob.write("Source;Target;Label;Weight\n")
    dict_sum = {}
    pair = ""
    for index in range(0, len(objects)):
        next_item = index + 1
        if next_item < len(objects):
            if objects[index][6] == "" or objects[next_item][6] == "":
                continue
            else:
                if objects[index][6] in dictionary and objects[next_item][6] in dictionary_items:
                    pair = str(dictionary[objects[index][6]]) + ";" + str(dictionary[objects[next_item][6]])
                    if pair not in dict_sum:
                        dict_sum[pair] = 1
                    else:
                        dict_sum[pair] += 1
    for item in dict_sum:
        fob.write(item + ";" + str(dict_sum[item]) + ";" + str(dict_sum[item]) + "\n")
    fob.close()
    
objects = []
linearr = []
fob = open("output.csv", 'r')
reload(sys)
sys.setdefaultencoding('utf8')
#    \timestart          \timeend        \
#desc\datestart\hourstart\dateend\hourend\elapsedtime\process\type
for line in fob: #begin for
    linearr = line.split("|", len(line))
    if len(linearr) == 6:
        desc = linearr[1]
        timestart = linearr[2].split("T", len(linearr[2]))
        timeend = linearr[3].split("T", len(linearr[3]))
        datestart = timestart[0]
        hourstart = re.sub(r'\.\d*', "", str(timestart[1]))
        dateend = timeend[0]
        hourend = re.sub(r'\.\d*', "", str(timeend[1]))
        time_object1 = datetime.strptime(str(datestart) + " "+ str(hourstart), '%Y-%m-%d %H:%M:%S')
##        sjts = datetime.strptime("2016-02-24 00:00:00", '%Y-%m-%d %H:%M:%S')
##        
##        if time_object1 > sjts:
##            pass
##        else:
##            continue
        time_object2 = datetime.strptime(str(dateend) + " "+ str(hourend), '%Y-%m-%d %H:%M:%S')
        elapsedtime = time_object2 - time_object1
        process = str(linearr[4])
        pType = linearr[5].split("/", len(linearr))[1]
        linearr = [desc, datestart, hourstart, dateend, hourend, elapsedtime, process, pType]
        objects.append(linearr)
    #end for
fob.close()

dictionary_items = {}
if len(sys.argv) >= 2:
    if str(sys.argv[1]) == "App" or str(sys.argv[1]) == "Doc" or str(sys.argv[1]) == "All":    
        loadNodes(dictionary_items, str(sys.argv[1]))
        loadEdges(dictionary_items, str(sys.argv[1]))
    else:
        print("No se reconoce a " + str(sys.argv[1]) + " como argumento valido")
        quit()
else:
    print("Falta un argumento")
    quit()
