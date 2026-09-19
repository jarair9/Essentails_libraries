import math

# This Function is already built in modules like pandas and numpy But for Understanding I coded it.

def variance(data):
    "Finding varaince"
    sumdb = sum(data)
    mean = sumdb/len(data)
    varaincen = []
    for n in data:
        var = (n - mean)**2
        varaincen.append(var)

    return round(sum(varaincen)/(len(data)-1))

print(variance([1,3,5,7,9,5,3,56,7,9,5,3,5,6]))

        
def standard_deviation(data):
    "Finding standard devaition"
    sumdb = sum(data)
    mean = sumdb/len(data)
    sd = []
    for n in data:
        var = (n - mean)**2
        sd.append(var)

    return math.sqrt(round(sum(sd)/(len(data)-1)))

print(standard_deviation([1,3,5,7,9,5,3,56,7,9,5,3,5,6]))

def cv(data):
    "Finding co-effienct of varaince"
    sumdb = sum(data)
    mean = sumdb/len(data)
    sd = []
    for n in data:
        var = (n - mean)**2
        sd.append(var)
    
    return math.sqrt(round(sum(sd)/(len(data)-1)))/mean*100

print(cv([1,3,5,7,9,5,3,56,7,9,5,3,5,6]))

        
def percentile(data,pl):
    
    if not pl or not data:
        return "Missing values"
    if pl > data[-1]:
        return "Pl is Higher keep pl under data."

    if pl < data[0]:
        return "pl is lower than first value correct it."
    
    return (pl / 100)*(len(data)+1)

print(percentile(data=[6,213,241,260,290,314,321,350,1500],pl=50))


def covarine(s1,s2):
    "Finding covaraince"
    sums1 = sum(s1)
    sums2 = sum(s2)

    means1 = sums1/len(s1)
    means2 = sums2/len(s2)
    x = 0
    y = 0
    for n in s1:
        x = n - means1
        for m in s2:
            y = m - means2 

    return x*y/(len(s1)-1)   # for sample -1 and population only n

print(covarine([2,5,8,12,13],[1,2,5,12,10]))

