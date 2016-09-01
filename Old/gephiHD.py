import re
from datetime import datetime, timedelta
import sys

def loadNodes(dictionary, string):
    id = 0
    no_times = {}
    detail = []
    file_object = open("nodes" + string + ".csv", 'w')
    file_object.write("Id;Label;Description;Importance\n")

    if "App" in string or "Doc" in string:
        for items in objects:
            if string in items[7]:
                #items[0] = depurado(items[0])
                dictionary[id] = items[0]
                file_object.write(str(id) + ";" + items[0] + ";" + items[6] + ";" + str(items[8]) + "\n")
                id += 1
    else:
        for items in objects:
            if "App" in items[7]:                    
                if "Google" in items[6] or "Internet Explorer" in items[6]:
                    continue
            #items[0] = depurado(items[0])    
            dictionary[id] = items[0]
            file_object.write(str(id) + ";" + items[0] + ";" + items[6] + ";" + str(items[8]) + "\n")
            id += 1
    file_object.close()

def loadEdges(dictionary, string):
    file_object = open("edges" + string + ".csv", 'w')
    file_object.write("Source;Target\n")
    pair = ""
    for index in range(0, len(dictionary) - 1):
        next_item = index + 1
        if next_item < len(objects):
            file_object.write(str(index) + ";" + str(next_item) + "\n")
    file_object.close()

def setImportance(filters, description, process):
    importance = 0
    for item in filters:
        if item in description or item in process:
            importance = 1
            continue
    return importance

def depurado(string):
    if "cmd" in string:
        return "cmd.exe"
    elif "Komodo" in string or "komodo" in string:
        return string.split(" ", len(string))[0]
    elif "C:" in string or "c:" in string:
        word = re.findall(r'\w+\.\w+', string)
        if len(word) > 0:
            return word[0]
        else:
            return ""
    elif "q=" in string:
        return "Web search"
    elif ".com" in string or ".org" in string or "http:" in string:
        temp = string.split("/", len(string))[-1]
        temp = re.sub(r'-', " ", str(temp))
        return temp
    elif "mail" in string:
        return "mail"
    else:
        return string

objects = []
linearr = []
filters = []
input_start_date = "2016-01-01"
input_end_date = "2020-01-01"

reload(sys)
sys.setdefaultencoding('utf8')

file_object = open("filters.txt", 'r')
for line in file_object:
    line = re.sub(r'\n', "", str(line))
    filters.append(line)

file_object.close()

if len(sys.argv) == 3:
    input_start_date = sys.argv[2]
    input_end_date = input_start_date
    
if len(sys.argv) == 4:
    input_start_date = sys.argv[2]
    input_end_date = sys.argv[3]

file_object = open("output.csv", 'r')

#    \timestart          \timeend        \
#desc\datestart\hourstart\dateend\hourend\elapsedtime\process\type\importance
for line in file_object: #begin for
    linearr = line.split("|", len(line))
    if len(linearr) == 6:
        if str(linearr[4]) != "":
            process = str(linearr[4])
        else:
            continue
        desc = linearr[1]
        timestart = linearr[2].split("T", len(linearr[2]))
        timeend = linearr[3].split("T", len(linearr[3]))
        datestart = timestart[0]
        hourstart = re.sub(r'\.\d*', "", str(timestart[1]))
        dateend = timeend[0]
        hourend = re.sub(r'\.\d*', "", str(timeend[1]))
        time_object1 = datetime.strptime(str(datestart) + " "+ str(hourstart), '%Y-%m-%d %H:%M:%S')
        time_object2 = datetime.strptime(str(dateend) + " "+ str(hourend), '%Y-%m-%d %H:%M:%S')
        limitstart = datetime.strptime(input_start_date + " 00:00:00", '%Y-%m-%d %H:%M:%S')
        limitend = datetime.strptime(input_end_date + " 23:59:59", '%Y-%m-%d %H:%M:%S')
        if time_object1 >= limitstart and time_object2 <= limitend:
            pass
        else:
            continue
        elapsedtime = time_object2 - time_object1
        pType = linearr[5].split("/", len(linearr))[1]
        imp = setImportance(filters, desc, process)
        linearr = [desc, datestart, hourstart, dateend, hourend, elapsedtime, process, pType, imp]
        objects.append(linearr)

file_object.close()

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
