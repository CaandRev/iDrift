#! python3
#home/casper/Code/chTools/ python3
# """ Adds a timestamp to a log file. You can add a filename ending to the logfile
# and a project/comment to the timestamp. Its limited to work with one logfile at a time.
# To work with multiple file run multiple instances of the program.
# In shortcut.json you can add string shortcuts so you don't need to write the string
# you use often out in full length"""
import datetime as dt
from pathlib import Path
import json
import webbrowser

#Get Current Working Directorie
cwd = Path.cwd() #Can be changed to other dir with os.chdir()
filename = 'logfile.txt'
filepath = Path(cwd/filename)
# filepath = Path(cwd/'logfiles'/filename).mkdir(parents=True, exist_ok=True) # If its needed to store the logfile in a childe folder

# Load the shortcuts
with open("shortcuts.json", "r", encoding="utf-8-sig") as f:
    short = json.load(f)
# Writes the time to a logfile. Creates the file if doesn't exists
# Add filename_ending to file name
def logTime(timestamp, filename_ending ='', comment = ''):
    if filename_ending:
        filename = 'logfile_' + str(filename_ending) + '.txt'
            
    filepath = Path(cwd/filename)
    
    if not Path(filepath).is_file():
        filemode = 'w'
    else:
        filemode = 'a'
        
    with open(filename,filemode, newline='', encoding='utf-8-sig') as log:
        if comment:
            comment = '\t' + comment
        log.write(timestamp)
        log.write(comment)
        log.write('\n')
    return filename

# Makes the needed timestamps
def times():   
    timeDate = dt.datetime.now()
    datestamp = timeDate.strftime('%Y-%m-%d')
    timestamp = timeDate.strftime('%Y-%m-%d  %H:%M:%S')

    return datestamp, timestamp

# Calculates how much time used on each project
def summary(filename):
    sumdict = {}
    count = 0
    delta = dt.timedelta(seconds=0)
    
    with open(filename,'r', encoding='utf-8-sig') as fileh:
        for i in fileh:
            lst = i.split()
            try:
                stoptime = dt.datetime.strptime(lst[1],'%H:%M:%S')
                comment = ' '.join(lst[2:])
                # print(stoptime,comment)
                if count > 0:
                    delta = stoptime-startime
                    # print(delta, lastcomment)
                else: 
                    lastcomment= comment
                startime = stoptime
                count += 1
                if lastcomment not in sumdict:    
                    sumdict[lastcomment] = delta
                else: 
                    sumdict[lastcomment] = sumdict[lastcomment] + delta                
                lastcomment = comment
        
            except:
                continue
    
    return sumdict

def write_to_file(textlst, filename):
    with open(filename,'a', encoding='utf-8-sig') as f:
        f.writelines(textlst)
        f.write('\n')

# Defining needed variables'
count = 0

def timeregistrering():
    webbrowser.open('https://hours.norconsult.com/')

# Logic of the program
try:
    while True:
        if count == 0:
            filename_ending = input('Ending for logfile can be added here(exit or ctrl-c to finish): ')
            datestamp, timestamp = times()
            
            if filename_ending.lower() == 'exit':    
                break
            elif filename_ending =='d':
                filename_ending = datestamp
            elif filename_ending.lower() in short:
                filename_ending = short[filename_ending]

            comment =  input('\nComment for the timestamp can be added here: ')
            if comment.lower() in short:
                comment =  short[comment]
            
            print(f"\n{timestamp} has been added to the log file")
            count =+ 1

        else:
            
            comment = input('\nKeep adding timestamps with or without comments to the file (exit or ctrl-c to finish): ')
            datestamp, timestamp = times()
            if comment.lower() == 'exit':    
                break
            elif comment.lower() in short:
                comment =  short[comment]
            
            print(f"\n{timestamp} has been added to the log filed")

            
        filename = logTime(timestamp, filename_ending, comment)        
                                                      
except: 
    KeyboardInterrupt
    
finally:        
    # Make a final timestamp on exit to calculate the last timedelta
    datestamp, timestamp = times()
    logTime(timestamp, filename_ending, 'Ut')

    # Saves the time and comments to a dictionary and makes the summary on exit and prints it to the logfile
    heading ='\nSummary of the day: \n'+ 40*'-'
    print(heading)
    write_to_file(heading,filename)
    total_time = dt.timedelta(seconds=0)
    sumdict = summary(filename) 
    for comment,time in sumdict.items():
        total_time += time
        time = str(time)
        summation_text = f'you have used {time}\ton {comment}'
        print(summation_text)
        write_to_file(summation_text,filename)
    
    total_time_text = f'\nTotal time used: {str(total_time)}'
    write_to_file(total_time_text,filename)
    print(total_time_text)     
    print('\nThanks for using the program!')
    
    timeregistrering()
   
input()
