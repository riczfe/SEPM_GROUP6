import datetime


def get_time():
    strTime = datetime.datetime.now().strftime("%H:%M:%S")
    result = "It's " + strTime + "."
    return result
