def lastc(x):
    return x[-12:]

def roundamount():
    return lambda a: round(a/1000000, 1)*100000

def roundamountmonth():
    return lambda a: round(a/1000000, 3)*100000

def roundscore():
    return lambda a: round(a/100, 2)

def getdigit():
    return re.findall(r'\d+')


