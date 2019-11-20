import statistics
tab = [2,3,5,2,9,8,1,3,9,1,1,4,7,7,1,4]

def mediana(x):
    return statistics.median(x)

def dominant(x):
    return statistics.mode(x)

print('Median: ', mediana(tab),'Mode: ',dominant(tab))

