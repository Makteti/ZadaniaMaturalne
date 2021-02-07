def isContrasting (x, y):
    if x - y > 128 or y - x > 128:
        return True
    else:
        return False
contrastCounter = 0
variable = []
biggest = 0
smallest = 0
with open("D:\matura\Matura2017\Dane_PR2\przyklad.txt", "r") as f:
    for x in f:
        line = f.readline() # each line in a string line
        splited = line.split()
        mapObject = map(int, splited) # mapping each string to int
        listMapped = list(mapObject) #creating a list of string elements converted to int(mapped)
       # print(min(listMapped)) #for each line
        if max(listMapped) > biggest:
            biggest = max(listMapped)
        else:
            biggest = biggest
        if min(listMapped) < smallest:
            smallest = max(listMapped)
        else:
            smallest = smallest
    print("Najciemniejszy: ",smallest,"Najjasniejszy: ", biggest) #4.1
##########################################################################################