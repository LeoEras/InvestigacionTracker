from datetime import datetime, timedelta
import numpy as np
import matplotlib.pyplot as plt
import sys
import re
from Base import *
#import time

def strToDate(string):
    new_date = [int(token) for token in string.split("-", len(string))] 
    return datetime(new_date[0], new_date[1], new_date[2])

def correctAll(item):
    if "App" in item[7]:
        if "Chrome" in item[6]:
            return True
        elif "Reader" in item[6]:
            return True
        elif "Point" in item[6]:
            return True
        elif "Word" in item[6]:
            return True
        elif "Notepad" in item[6]:
            return True
    else:
        return False

def depurate(item):
    if "c:" in item or "C:" in item:
        word = re.findall(r'\w+\.\w+', item)
        if len(word) > 0:
            return word[0]
        else:
            return ""
    else:
        return item

def findItems(name, item_type, date_start, date_end):
    result = []
    for item in objects:
        d_start = strToDate(date_start)
        item_date_start = strToDate(item[1])
        d_end = strToDate(date_end)
        item_date_end = strToDate(item[3])           
        if d_start <= item_date_start and item_date_end <= d_end:
            if name == "":
                if item_type == "All":
                    if correctAll(item):
                        continue
                    else:
                        result.append(item)
                elif item_type in item[7]:
                    result.append(item)
            elif name in item[6]:
                result.append(item)
    return result

def graph(name, item_type, input_scale, date_start, date_end):
    dictionary = {}
    item_list = findItems(name, item_type, date_start, date_end)
    if date_start == date_end:
        for item in item_list:
            item[0] = depurate(item[0])    
            if str(item[0]) not in dictionary:
                dictionary[str(item[0])] = item[5]
            else:
                dictionary[str(item[0])] += item[5]
    else:
        for item in item_list:
            item[1] = depurate(item[1])
            if str(item[1]) not in dictionary:
                dictionary[str(item[1])] = item[5]
            else:
                dictionary[str(item[1])] += item[5]
            
    x_axis = range(1, len(dictionary.keys()) + 1)
    y_axis = []
    fig = plt.figure(name + ": tiempo de uso por dia")
    for key in sorted(dictionary.keys()):
        y_axis.append(int(dictionary[key].seconds))
    plt.bar(x_axis, y_axis, align='center')
    plt.xticks(rotation=90)
    plt.xticks(range(1, len(dictionary.keys()) + 1), sorted(dictionary.keys()), size='small')
    plt.yticks(range(0, max(y_axis) + input_scale, input_scale), [timedelta(seconds = y) for y in range(0, max(y_axis) + input_scale, input_scale)], size='small')
    plt.show()

def onclick(event):
    if event.button == 1 and event.dblclick:
        name = getNameFromBar(event.xdata, event.ydata, dictionary_items)
        if name:
            graph(name, item_type, input_scale, input_start_date, input_end_date)
            
def getNameFromBar(x_axis_value, y_axis_value, dictionary):
    new_dictionary = {}
    cont = 0
    for item in dictionary.items():
        new_dictionary[cont] = item[1]
        cont += 1
    new_x_axis_values = range(1, len(dictionary.keys()) + 1)
    for value in new_x_axis_values:
        if ((int(value) - 0.4 ) <= x_axis_value <= (int(value) + 0.4)) and 0 <= int(y_axis_value) <= (new_dictionary[value - 1]).seconds:
            return dictionary.keys()[int(round(x_axis_value)) - 1]
    return {}

def setImportance(filters, description, process):
    importance = 0
    for item in filters:
        if item in description or item in process:
            importance = 1
            continue
    return importance

#print(re.split(r'(s*)', "Here are some words"))
#print(re.split(r'[a-z][A-Z]', "Google Chrome", re.I|re.M))
#word = re.findall(r'\d{3,5}\s\w+\s\w+\.', "kdwplsjsof324 main street.dsadksadkasdks")
#print(word[0])

#start_time = time.time()
item_type = "All"
input_start_date = "2016-01-01"
input_end_date = "2020-01-01"
input_scale = 3600
filters = []
reload(sys)  
sys.setdefaultencoding('utf8')

if len(sys.argv) > 1 and len(sys.argv) == 6:
    item_type = str(sys.argv[1])
    input_start_date = str(sys.argv[2])
    input_end_date = str(sys.argv[3])
    input_scale = int(str(sys.argv[4]))
else:
    print("Error al leer parametros")
    print("Trabajando con valores predeterminados")

#Getting importance from filters.txt
file_object = open("filters.txt", 'r')
for line in file_object:
    line = re.sub(r'\n', "", str(line))
    filters.append(line)

file_object.close()

objects = []
dictionary_items = {}
objects = getList(str(sys.argv[5]))


items = findItems("", item_type, input_start_date, input_end_date)
for item in items:
    item[6] = depurate(item[6])
    if str(item[6]) not in dictionary_items:
        dictionary_items[str(item[6])] = item[5]
    else:
        dictionary_items[str(item[6])] += item[5]

x = range(1, len(dictionary_items.keys()) + 1)

if item_type == "App":
    title = "Aplicaciones usadas"
elif item_type == "Doc":
    title = "Documentos usados"
elif item_type == "All":
    title = "Aplicaciones y documentos usados"

#print("--- %s seconds ---" % (time.time() - start_time))

if input_start_date == input_end_date:
    fig = plt.figure(title + " durante el dia " + input_start_date)
else:
    fig = plt.figure(title + " desde el " + input_start_date + " hasta el " + input_end_date)
    
y = [int(item.seconds) for item in dictionary_items.values()]
plt.bar(x, y, align='center')
cid = fig.canvas.mpl_connect('button_press_event', onclick)
plt.xticks(rotation=90)
plt.xticks(range(1, len(dictionary_items.keys()) + 1), dictionary_items.keys(), size='small')
plt.yticks(range(0, max(y) + input_scale, input_scale), [timedelta(seconds=y) for y in range(0, max(y) + input_scale, input_scale)], size='small')
plt.show()
