from datetime import datetime, timedelta
import sys
import re

def depurate(item):
    item = item.replace('"', '').strip()
    item = item[0:300]
    if "c:" in item or "C:" in item:
        word = re.findall(r'\w+\.\w+', item)
        if len(word) > 0:
            return word[-1]
        else:
            return ""
    else:
        return item

def setImportance(filters, description, process):
    importance = 0
    for item in filters:
        if item in description or item in process:
            importance = 1
            continue
    return importance

def getList(filename, user):
    filters = []
    
    #Getting importance from filters.txt
    file_object = open("filters.txt", 'r')
    for line in file_object:
        line = re.sub(r'\n', "", str(line))
        filters.append(line)

    file_object.close()

    file_object = open(filename + user + ".csv", 'r')
    file_object_writter = open("Outputs\depurado" + user + ".csv", 'w')
    objects = []
    collection = []
    #    	    \date_time_start      \date_time_end    \
    #description\date_start\time_start\date_end\time_end\elapsed_time\process\process_type\importance
    for line in file_object:
        collection = line.split("|", len(line))
        if len(collection) == 6:
            if str(collection[4]) == "":
                continue
            description = depurate(collection[1])
            date_time_start = collection[2].split("T", len(collection[2]))
            date_time_end = collection[3].split("T", len(collection[3]))
            date_start = date_time_start[0]
            time_start = re.sub(r'\.\d*', "", str(date_time_start[1]))
            date_end = date_time_end[0]
            time_end = re.sub(r'\.\d*', "", str(date_time_end[1]))
            time_object_1 = datetime.strptime(str(date_start) + " " + str(time_start), '%Y-%m-%d %H:%M:%S')
            time_object_2 = datetime.strptime(str(date_end) + " " + str(time_end), '%Y-%m-%d %H:%M:%S')
            elapsed_time = time_object_2 - time_object_1
            process = depurate(collection[4])
            process_type = collection[5].split("/", len(collection))[1].splitlines()[0]
            importance = setImportance(filters, description, process)
            collection = [description, date_start, time_start, date_end, time_end, elapsed_time, process, process_type, importance]
            file_object_writter.write(str(description) + "|" +
                                      str(date_start) + "|" +
                                      str(time_start) + "|" +
                                      str(date_end) + "|" +
                                      str(time_end) + "|" +
                                      str(elapsed_time) + "|" +
                                      str(process) + "|" +
                                      str(process_type) + "|" +
                                      str(importance) + "|" +
                                      str(user) + "\n")

    file_object.close()
    file_object_writter.close()
    return objects

reload(sys)
getList(sys.argv[1], sys.argv[2])
