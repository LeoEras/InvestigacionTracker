from datetime import datetime, timedelta, date
from warnings import filterwarnings
import sys
import re
import MySQLdb

##dates_table = []
activity_table = []
application_table = []

filters = []

def getFilters(filefilters):
    file_object = open(filefilters, 'r', encoding='utf8')
    for line in file_object:
        word = line.replace("\n", "")
        filters.append(word)
    return filters

filterwarnings('ignore', category = MySQLdb.Warning)

def depurate(item):
    item = item.replace('"', '').strip()
    item = item[0:250]
    if "c:" in item or "C:" in item:
        word = re.findall(r'\w+\.\w+', item)
        if len(word) > 0:
            return word[-1]
        else:
            return ""
    else:
        return item

def setImportance(filters, description, process):
    for item in filters:
        if item in description or item in process:
            return 1
    return 0

def dateStrToInt(date_str):
    list_of_strings = date_str.split("-")
    return int(list_of_strings[0]), int(list_of_strings[1]), int(list_of_strings[2])

def populateDatesApplication(filename, user):
    conn = MySQLdb.connect(host= "localhost",
                           user="root", passwd="1234",
                           db="Base", use_unicode=True,
                           charset="utf8")
    x = conn.cursor()
    file_object = open(filename + user + ".csv", 'r', encoding='utf8')
    new_dir = filename.split('\\')
    objects = []
    collection = []    
    #    	    \date_time_start      \date_time_end    \
    #description\date_start\time_start\date_end\time_end\elapsed_time\process\process_type\importance
    for line in file_object:
        if "ComputerUsage" in line or "Away" in line or "Power" in line:
                continue
        collection = line.split("|", len(line))
        if len(collection) == 6:
            if str(collection[4]) == "":
                continue
            collection[1] = collection[1].replace("\"", "", 2)
            collection[2] = collection[2].replace("\"", "", 2)
            collection[3] = collection[3].replace("\"", "", 2)
            activity = depurate(collection[1])
            if "T" in collection[2]:
                date_time_start = collection[2].split("T", len(collection[2]))
                date_time_end = collection[3].split("T", len(collection[3]))
            else:
                date_time_start = collection[2].split(" ", len(collection[2]))
                date_time_end = collection[3].split(" ", len(collection[3]))
            date_start = date_time_start[0]
            date_end = date_time_end[0]
            application = depurate(collection[4])

            if activity not in activity_table:
                activity_table.append(activity)

            if application not in application_table:
                application_table.append(application)

    new_activity = [(None, item) for item in activity_table]
    new_app = [(None, item) for item in application_table]

    try:
        x.executemany("""INSERT IGNORE INTO Activity VALUES (%s, %s)""", new_activity)
        conn.commit()
    except:
        conn.rollback()
    print("Done populating table Activity")
        
    try:
        x.executemany("""INSERT IGNORE INTO Application VALUES (%s, %s)""", new_app)
        conn.commit()
    except:
        conn.rollback()
    print("Done populating table Application")
    
    conn.close()
    file_object.close()

def populateLog(filename, user, term):
    conn = MySQLdb.connect(host= "localhost",
                           user="root", passwd="1234",
                           db="Base", use_unicode=True,
                           charset="utf8")
    x = conn.cursor()
    file_object = open(filename + user + ".csv", 'r', encoding='utf8')
    new_dir = filename.split('\\')
    collection = []
    objects = []

    activity_dict = {}
    application_dict = {}
    class_dict = {}
    users_dict = {}
    dates_dict = {}
    
    x.execute("""SELECT * FROM Activity""")
    for item in x.fetchall():
        activity_dict[item[1]] = item[0]
        
    x.execute("""SELECT * FROM Application""")
    for item in x.fetchall():
        application_dict[item[1]] = item[0]

    x.execute("""SELECT * FROM Class""")
    for item in x.fetchall():
        class_dict[item[1]] = item[0]

    #    	    \date_time_start      \date_time_end    \
    #description\date_start\time_start\date_end\time_end\elapsed_time\process\process_type\importance
    for line in file_object:
        if "ComputerUsage" in line or "Away" in line or "Power" in line:
            continue
        collection = line.split("|", len(line))
        if len(collection) == 6:
            if str(collection[4]) == "":
                continue
            collection[1] = collection[1].replace("\"", "", 2)
            collection[2] = collection[2].replace("\"", "", 2)
            collection[3] = collection[3].replace("\"", "", 2)
            description = depurate(collection[1])
            if "T" in collection[2]:
                date_time_start = collection[2].split("T", len(collection[2]))
                date_time_end = collection[3].split("T", len(collection[3]))
            else:
                date_time_start = collection[2].split(" ", len(collection[2]))
                date_time_end = collection[3].split(" ", len(collection[3]))
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
            description = activity_dict[description]
            process = application_dict[process]
            process_type = class_dict[process_type]
            collection = (None, term, description, date_start, time_start, date_end, time_end, elapsed_time, process, process_type, importance, user)
            objects.append(collection)

    file_object.close()
    print("Done building list")
    
    try:
        x.executemany("""INSERT INTO Log VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)""", objects)
        conn.commit()
    except:
        conn.rollback()

    print("Done populating table Log")

getFilters(sys.argv[4])
populateDatesApplication(sys.argv[1], sys.argv[2])
populateLog(sys.argv[1], sys.argv[2], sys.argv[3])

