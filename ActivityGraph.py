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


def findItemsByRelevance(name, item_type, date_start, date_end, importance):
    raw_items = findItems(name, item_type, date_start, date_end)
    result = []
    for item in raw_items:
        if item[8] == importance:
            result.append(item)
    return result

def graph(name, item_type, input_scale, date_start, date_end):
    dictionary = {}
    for item in findItems(name, item_type, date_start, date_end):
        if date_start == date_end:
            if str(item[0]) not in dictionary:
                dictionary[str(item[0])] = item[5]
            else:
                dictionary[str(item[0])] += item[5]
        else:
            if str(item[1]) not in dictionary:
                dictionary[str(item[1])] = item[5]
            else:
                dictionary[str(item[1])] += item[5]
    x_axis = range(1, len(dictionary.keys()) + 1)
    fig = plt.figure(name + ": tiempo de uso por dia")
    y_axis = []
    for key in sorted(dictionary.keys()):
        y_axis.append(int(dictionary[key].seconds))
    plt.bar(x_axis, y_axis, align='center')
    plt.xticks(rotation=90)
    plt.xticks(range(1, len(dictionary.keys()) + 1), sorted(dictionary.keys()), size='small')
    plt.yticks(range(0, max(y_axis) + input_scale, input_scale), [timedelta(seconds = y) for y in range(0, max(y_axis) + input_scale, input_scale)], size='small')
    plt.show()

def onclick(event):
    #print ('button=%d, x=%d, y=%d, xdata=%f, ydata=%f'%(event.button, event.x, event.y, event.xdata, event.ydata))
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

def axisUsefulUseless(importance):
    dictionary = {}
    items = findItemsByRelevance("", item_type, input_start_date, input_end_date, importance)
    for item in items:
        if str(item[1]) not in dictionary:
            dictionary[str(item[1])] = item[5]
        else:
            dictionary[str(item[1])] += item[5]
    x_axis = range(1, len(dictionary.keys()) + 1)
    y_axis = []
    for key in sorted(dictionary.keys()):
        y_axis.append(int(dictionary[key].seconds))
        
    return x_axis, y_axis

def setImportance(filters, description, process):
    importance = 0
    for item in filters:
        if item in description or item in process:
            importance = 1
            continue
    return importance

#start_time = time.time()
item_type = "All"
input_start_date = "2016-01-01"
input_end_date = "2020-01-01"
input_scale = 3600
filters = []
reload(sys)  
sys.setdefaultencoding('utf8')

item_type = str(sys.argv[1])
input_start_date = str(sys.argv[2])
input_end_date = str(sys.argv[3])
input_scale = int(str(sys.argv[4]))

objects = []
objects = getList("output.csv")

fig = plt.figure("Grafica tiempo Actividades Utiles (Azul) vs No Utiles (Rojo)")
x1, y1 = axisUsefulUseless(1)
x2, y2 = axisUsefulUseless(0)
dictionary = {}
items = findItems("", item_type, input_start_date, input_end_date)
for item in items:
    if str(item[1]) not in dictionary:
        dictionary[str(item[1])] = item[5]
    else:
        dictionary[str(item[1])] += item[5]

x_axis = range(1, len(dictionary.keys()) + 1)
y_axis = []
for key in sorted(dictionary.keys()):
    y_axis.append(int(dictionary[key].seconds))

plt.xticks(rotation=90) 
plt.xticks(range(1, len(dictionary.keys()) + 1), sorted(dictionary.keys()), size='small')
plt.yticks(range(0, max(y_axis) + input_scale, input_scale), [timedelta(seconds = y) for y in range(0, max(y_axis) + input_scale, input_scale)], size='small')
plt.plot(x1, y1, 'b')
plt.plot(x2, y2, 'r')
plt.plot(x_axis, y_axis, 'g')
plt.show()
