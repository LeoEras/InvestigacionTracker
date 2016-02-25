import re
from datetime import datetime, timedelta
import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
import sys

#print 'Number of arguments:', len(sys.argv), 'arguments.'
#print 'Argument List:', str(sys.argv)

def stodate(string):
    d = [int(value) for value in string.split("-", len(string))] 
    return datetime(d[0], d[1], d[2])

def findobj(name, typeof, datestart, dateend):
    result = []
    for obj in objects:
        dstart = stodate(datestart)
        odstart = stodate(obj[1])
        dend = stodate(dateend)
        odend = stodate(obj[3])           
        if dstart <= odstart and odend <= dend:
            if name == "":
                if typeof == "All":
                    result.append(obj)
                elif typeof in obj[7]:
                    result.append(obj)
            elif name in obj[6]:
                result.append(obj)
    return result

##IDEAS:
##    1.) buscar aplicacion por fecha retorna el tiempo total empleado en esa aplicacion ese dia
##    2.) buscar aplicacion retorna el tiempo total por cada dia

def graph(name, vtime, datestart, dateend):
    dictionary = {}
    for w in findobj(name, "App", datestart, dateend):
        if str(w[1]) not in dictionary:
            dictionary[str(w[1])] = w[5]
        else:
            dictionary[str(w[1])] += w[5]
    x=range(1, len(dictionary.keys()) + 1)
    fig = plt.figure(name + ": tiempo de uso por dia")
    yvalues=[]
    for key in sorted(dictionary.keys()):
        yvalues.append(int(dictionary[key].seconds))
    plt.bar(x, yvalues, align='center')
    plt.xticks(rotation=90)
    plt.xticks(range(1, len(dictionary.keys()) + 1), sorted(dictionary.keys()), size='small')
    plt.yticks(range(0, max(yvalues) + vtime, vtime), [timedelta(seconds=y) for y in range(0, max(yvalues) + vtime, vtime)], size='small')
    plt.show()

def onclick(event):
    #print ('button=%d, x=%d, y=%d, xdata=%f, ydata=%f'%(event.button, event.x, event.y, event.xdata, event.ydata))
    if event.button == 1 and event.dblclick:
        my_app = valid(event.xdata, event.ydata, d_doc)
        if my_app:
            graph(my_app, vtime, ti, te)
            
def valid(x, y, dictionary):
    ndict = {}
    cont = 0
    for obj in dictionary.items():
        ndict[cont] = obj[1]
        cont += 1
    newX = range(1, len(dictionary.keys()) + 1)
    for value in newX:
        if ((int(value) - 0.4 ) <= x <= (int(value) + 0.4)) and 0 <= int(y) <= (ndict[value - 1]).seconds:
            return dictionary.keys()[int(round(x)) - 1]
    return {}

#print(re.split(r'(s*)', "Here are some words"))
#print(re.split(r'[a-z][A-Z]', "Google Chrome", re.I|re.M))
#word = re.findall(r'\d{3,5}\s\w+\s\w+\.', "kdwplsjsof324 main street.dsadksadkasdks")
#print(word[0])
typeof = "Doc"
ti = "2016-01-01"
te = "2020-01-01"
vtime = 3600
reload(sys)  
sys.setdefaultencoding('utf8')

if len(sys.argv) > 1:
    ti = str(sys.argv[1])
    te = str(sys.argv[2])
    vtime = int(str(sys.argv[3]))

fob = open("output.csv", 'r')
objects = []
linearr = []
d_app = {}
d_doc = {}
#    \timestart          \timeend        \
#desc\datestart\hourstart\dateend\hourend\elapsedtime\process\type
for line in fob: #begin for
    linearr = line.split("|", len(line))
    if len(linearr) == 6:
        word = re.findall(r'^\w\:', linearr[1])
        if len(word):
            continue
        word = re.findall(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', linearr[1])
        if "www." in linearr[1] or ".com" in linearr[1] or ".org" in linearr[1] or "localhost" in linearr[1] or len(word) >= 1:
            pass
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
        elapsedtime = time_object2 - time_object1
        if str(linearr[4]) != "":
            process = str(linearr[4])
        else:
            continue
        pType = linearr[5].split("/", len(linearr))[1]
        linearr = [desc, datestart, hourstart, dateend, hourend, elapsedtime, process, pType]
        objects.append(linearr)
    #end for
fob.close()
acum = timedelta(seconds=0)
for w in findobj("", typeof, ti, te):
    if str(w[6]) not in d_doc:
        d_doc[str(w[6])] = w[5]
    else:
        d_doc[str(w[6])] += w[5]

x=range(1, len(d_doc.keys()) + 1)
if typeof == "App":
    title = "Aplicaciones usadas"
elif typeof == "Doc":
    title = "Documentos usados"
elif typeof == "All":
    title = "Aplicaciones y documentos usados"
fig = plt.figure(title + " desde el " + ti + " hasta el " + te)
yvalues = [int(w.seconds) for w in d_doc.values()]
plt.bar(x, yvalues, align='center')
cid = fig.canvas.mpl_connect('button_press_event', onclick)
plt.xticks(rotation=90)
plt.xticks(range(1, len(d_doc.keys()) + 1), d_doc.keys(), size='small')
plt.yticks(range(0, max(yvalues) + vtime, vtime), [timedelta(seconds=y) for y in range(0, max(yvalues) + vtime, vtime)], size='small')
plt.show()

##circle1=plt.Circle((0,0),.2,color='r')
##circle2=plt.Circle((.5,.5),.2,color='b')
##circle3=plt.Circle((1,1),.2,color='g',clip_on=False)
##fig = plt.gcf()
##fig.gca().add_artist(circle1)
##fig.gca().add_artist(circle2)
##fig.gca().add_artist(circle3)
##fig.savefig('plotcircles.png')



