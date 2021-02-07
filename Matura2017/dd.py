def prime(n):
    if n == 2:
        return True
    if n % 2 == 0 or n <= 1:
        return False
eqlCounter = 0
octals = []
smallest = 99
with open("D:\matura\Matura2017\Dane_PR2\liczby.txt", "r") as f:
    for x in f:
        lines = f.readline()
        splited = lines.split()
        toInt = int(splited[1], 8) #oct to int(dec)
        octals.append(toInt)
        if int(splited[0]) == toInt:
            eqlCounter += 1
    low = min(octals)
    maxx = max(octals)
    print("same nmbrs: ", eqlCounter) #a
    print("min: ", min(octals),"at: ",octals.index(low))
    print("max: ", max(octals),"at: ",octals.index(maxx))
    

    


