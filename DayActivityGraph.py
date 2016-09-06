from datetime import datetime, timedelta
import numpy as np
import matplotlib.pyplot as plt
import sys
import re
from Base import *

def strToSeconds(string):
    new_time = [int(token) for token in string.split(":", len(string))] 
    return ((new_time[0] * 3600) + (new_time[1] * 60) + new_time[2])

def secToString(integer):
    hour = int(integer/3600)
    minute = int((integer - hour*3600)/60)
    second = integer - hour*3600 - minute*60
    if minute < 10:
        if second < 10:
            return "" + str(hour) + ":0" + str(minute) + ":0" + str(second)
        else:
            return "" + str(hour) + ":0" + str(minute) + ":" + str(second)
    else:
        if second < 10:
            return "" + str(hour) + ":" + str(minute) + ":0" + str(second)
        else:
            return "" + str(hour) + ":" + str(minute) + ":" + str(second)

def strToDate(string):
    new_date = [int(token) for token in string.split("-", len(string))] 
    return datetime(new_date[0], new_date[1], new_date[2])

def findItems(item_type, date_start):
    result = []
    for item in objects:
        d_start = strToDate(date_start)
        item_date_start = strToDate(item[1])
        if d_start == item_date_start:
            if item_type == "All":
                if "Google" in item[6]:
                    continue
                else:
                    result.append(item)
            elif item_type in item[7]:
                result.append(item)
    return result

def findItemByTime(x_value):
    for items in findItems("", item_type, input_start_date):
        if x_value > strToSeconds(items[4]):
            continue
        elif x_value > strToSeconds(items[2]) and x_value <= strToSeconds(items[4]):
            return items

def setImportance(description, process):
    if "python" in description or "python" in process:
        return 1
    elif "stack" in description or "stack" in process:
        return 1
    elif "Komodo" in description or "Komodo" in process:
        return 1
    elif "Notepad++" in description or "Notepad++" in process:
        return 1
    elif "cmd.exe" in description or "cmd.exe" in process:
        return 1
    elif "localhost" in description or "localhost" in process:
        return 1
    else:
        return 0 

#print(re.split(r'(s*)', "Here are some words"))
#print(re.split(r'[a-z][A-Z]', "Google Chrome", re.I|re.M))
#word = re.findall(r'\d{3,5}\s\w+\s\w+\.', "kdwplsjsof324 main street.dsadksadkasdks")
#print(word[0])

item_type = "All"
input_start_date = "2016-01-01"
#scale = 3600
reload(sys)  
sys.setdefaultencoding('utf8')

if len(sys.argv) > 1 and len(sys.argv) == 3:
    item_type = str(sys.argv[1])
    input_start_date = str(sys.argv[2])
    #scale = int(str(sys.argv[3]))
else:
    print("Error al leer parametros")
    print("Trabajando con valores predeterminados")

objects = []
collection = []
dictionary_items = {}
objects = getList("output.csv")

if item_type == "App":
    title = "Aplicaciones usadas"
elif item_type == "Doc":
    title = "Documentos usados"
elif item_type == "All":
    title = "Aplicaciones y documentos usados"

selected = findItems(item_type, input_start_date)
starting_time = [strToSeconds(item[2]) for item in selected]
ending_time = [strToSeconds(item[4]) for item in selected]
x = np.arange(min(starting_time), max(ending_time))
y_vals = [0, 1]
my_bits = [0 for item in x]
#cont = 0

for items in selected:
    #cont += int(items[5].seconds)
    for value in range(int(items[5].seconds)):
        my_bits[(strToSeconds(items[2]) + value) - x[0]] = items[8]

#print(cont)
print("Tiempo trabajado: %s" % secToString(sum(my_bits)))
day_start_time = min(starting_time)
day_end_time = max(ending_time)
total_time = day_end_time - day_start_time
print("Tiempo total de uso: %s" % secToString(total_time))
#print("Tiempo inactivo: %s" % secToString(total_time - sum(my_bits)))

fig = plt.figure(title + " durante el dia " + input_start_date)
ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])
ax.set_ylim(ymin=-1, ymax=2)
ax.step(x, my_bits, color='g')
ax.grid()
ax.set_yticks((0, 1))
ax.set_xlabel('Tiempo en segundos')
ax.set_ylabel('Valor')
#if scale < 3600: plt.xticks(rotation=90)
#plt.xticks(range(x[0], x[-1], scale), [secToString(value) for value in range(x[0], x[-1] + scale, scale)], size='small')
plt.show()



