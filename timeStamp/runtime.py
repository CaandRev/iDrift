import time

def starttime():
    starttime = time.time()
    return starttime

def stoptime(starttime):
    stoptime = time.time()
    run= stoptime-starttime
    return run

def converttime(run):
    hour, minute = divmod(run,3600)
    minutes, sec = divmod(minute, 60)
    return int(hour), int(minutes), int(sec)
