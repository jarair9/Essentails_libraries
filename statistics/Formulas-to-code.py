import math

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
    "Finding varaince"
    sumdb = sum(data)
    mean = sumdb/len(data)
    sd = []
    for n in data:
        var = (n - mean)**2
        sd.append(var)
    
    return math.sqrt(round(sum(sd)/(len(data)-1)))/mean*100

print(cv([1,3,5,7,9,5,3,56,7,9,5,3,5,6]))

        
def percentile(data,pl):
    if not pl or data:
        return "Missing values"
    if pl > data[::-1]:
        return "Pl is Higher keep pl under data."

    if pl < data[0]:
        return "pl is lower than first value correct it."
    data = data.sort()
    return (pl / 100)*(len(data)-1)

print(percentile([1,3,5,7,9,5,3,56,7,9,5,3,5,6],))
