import re
import math

with open("chars4.txt", 'r') as f:
    row = f.readlines()

    pattern = re.compile("[0-9]|[0-9][0-9]|[0-9][0-9][0-9]")
    t = 0
    for r in row:
        wN = []
        counter = 0
        var1 = r.split()
        var1.pop(0)
        var1.pop(2)
        str(var1).replace("|", " ")
        var2 = re.findall(pattern, str(var1))
        print(var2)
       # for v1 in range(10):
       #     #var1.append(v1)
       # for v2 in range(10, (len(var1)-10)):
       #     if var1[v2] == wN:
       #         counter += 1
       # t += counter * 2
    #print(t)        
    





    #t = 0
    #for r in row:
    #    pattern = re.compile("\d|[0-9][0-9]|[0-9][0-9][0-9]")
    #    var1 = r.replace("|", " ")
    #    var2 = re.findall(pattern, str(var1))
    #    wN = []
    #    cN = []
    #    for x in range(10):
    #        wN.append(var2[x])
    #    for x in range(10, (len(var2)-10)):
    #        cN.append(var2[x])
        
        

        #for y in range(10, (len(var2) - 10)):
        #    if var2[y] == wN:
        #        counter += 1
        #t += counter * 2
            
    #print(t)
        