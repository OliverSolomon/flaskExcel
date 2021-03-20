import pandas as pd
from glob import glob
from datetime import datetime
import os

def removeDups(file):
    df = pd.read_excel(file)
    # Keep only FIRST record from set of duplicates
    df_first_record = df.drop_duplicates(subset="Date/Time", keep="first")
    #creates an excel file with sorted times
    if glob("noDupsTime.xlsx"):
        pass
    else:
        df_first_record.to_excel("./downloads/noDupsTime.xlsx", index=False)

# removeDups()

def create_dict():
    os.chdir('./downloads')
    df=pd.read_excel("noDupsTime.xlsx")
    names_list=list(df['Name'])
    dates_list=list(df['Date/Time'])
    custom_dict={}#dictionary of names as keys and al lthe datetime as values
    modified_dict={}
    for name,date_time  in zip(names_list,dates_list):
        if name not in custom_dict.keys():
            custom_dict[name]=[date_time]
        else:
            custom_dict[name].append(date_time)
    for name in custom_dict.keys():
        #for each name go through each date,then split date_time into date and time,
        #create a dictionary with each day as the key and the values an array of times
        date_dict={}
        for dateTime in custom_dict[name]:
        #iterate over datetimes of each person
            date = dateTime.split()[0]
            time = dateTime.split()[-1]
            if date not in date_dict.keys():
                date_dict[date]=[time]
            else:
                date_dict[date].append(time)
        modified_dict[name]=date_dict#create new dictionary with the name as the key
    print(modified_dict)
    return modified_dict

def create_report(create_dict):

    data=create_dict()
    lst_of_names=[]
    length=0
    lst_of_dates=[]
    lst_of_timein=[]
    lst_of_timeout=[]
    lst_of_durations=[]
    total=0
    #iterate over all the names
    for name in data.keys():
        length+=1
        days=data[name]
        dates=data[name].keys()#gets dates for each name
        print(f'each_day:{type(days)}')
        no_of_names=len(dates)
        lst_of_names.extend([name for i in range(no_of_names)])#make name array same size as dates array
        lst_of_dates.extend(dates)
        for day in days.values():
            print('day:',day)
            total+=1
            first_time = datetime.strptime(day[0], '%H:%M:%S')
            last_time = datetime.strptime(day[-1], '%H:%M:%S')
            time_diff_Hours = (last_time - first_time).seconds//3600
            rem_minutes = ((last_time-first_time).seconds% 3600)//60
            time_diff = str(time_diff_Hours) + ":" + str(rem_minutes)


            lst_of_timein.append(first_time.time())
            lst_of_timeout.append(last_time.time())
            lst_of_durations.append(time_diff)

        #lst_of_durations.extend(data[name].values()[0])

    print(f'total:{total}')
    print(f"old length:{length}\nnew length:{len(lst_of_names)}")
    print(f"no of dates:{len(lst_of_dates)}")
    print(f'{len(lst_of_timein)}')
    print(f'{len(lst_of_timeout)}')
    df=pd.DataFrame({"Names":lst_of_names,"Date":lst_of_dates,"Time_in":lst_of_timein,"Time_out":lst_of_timeout,"Time Spent":lst_of_durations})
    #df2=pd.DataFrame({"Time_in":lst_of_timein,"Time_out":lst_of_timeout})
    #df=pd.DataFrame({"Names":lst_of_names,"Date":lst_of_dates})
    df.to_excel('report.xlsx')
    #df2.to_excel('fingers2.xlsx')
# create_report(create_dict)

def report(file):
    removeDups(file)
    create_report(create_dict)
