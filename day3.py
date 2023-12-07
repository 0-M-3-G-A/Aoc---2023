import re

with open("chars3.txt", 'r') as f:
    row = f.readlines()
                          
    #pattern = re.compile("/[!£$%^&*@~?¬]/\d/[!£$%^&*@~?¬]/|/[!£$%^&*@~?¬]/[0-0][0-9]/[!£$%^&*@~?¬]/|/[!£$%^&*@~?¬]/[0-9][0-9][0-9]/[!£$%^&*@~?¬]/")
    #pattern = re.compile("/[^\p{L}\d\s@#]/u")
    #pattern1d = re.compile("/[^\p{L}\d\s@#]/u\d/[^\p{L}\d\s@#]/u")
    #pattern1d = re.compile("^/[-!$%^&*()_+|~=`{}\[\]:;'<>?,.\/]/\d/[-!$%^&*()_+|~=`{}\[\]:;'<>?,.\/]/|^/[-!$%^&*()_+|~=`{}\[\]:;'<>?,.\/]/\d/[-!$%^&*()_+|~=`{}\[\]:;'<>?,.\/]/$")
    #pattern2d = re.compile("/[\W\S_]/\d{2}/[\W\S_]/")
    #pattern3d = re.compile("/[\W\S_]/\d{3}/[\W\S_]/")

    #for r in row:
    #    var1 = re.findall(pattern1d, r)
    ##    print(var1)
    #    var2 = re.findall(pattern2d, r)
    #    var3 = re.findall(pattern3d, r)
    cleanedArray = []
    #pattern = re.compile("^[!|/|@|*|#|+|=|&|-|$]\d|^\d[!|/|@|*|#|+|=|&|-|$]|^[!|/|@|*|#|+|=|&|-|$][0-9][0-9]|[0-9][0-9]|[!|/|@|*|#|+|=|&|-|$]|[0-9][0-9][0-9]|[0-9][0-9][0-9][!|/|@|*|#|+|=|&|-|$]")
    #pattern = re.compile("\d|[0-9][0-9]|[0-9][0-9][0-9]")
    symbols = ["!","$","%","^","*","@","#","?"]
    for r in row:
        cleanedArray.append([r.replace(".", " ").rstrip()])
    print(cleanedArray)
    for c in range(len(cleanedArray)):
        index1 = c
        index2 = c + 1
        index = c - 1
        var1 = str(cleanedArray[c]).split()
        for v1 in range(len(var1)):
            indexc1 = v1
            indexc2 = v1 + 1
            indexc3 = v1 - 1
            if (v1 > 1) and ((var1[indexc2] == symbols) or (var1[indexc3] == symbols)):
                print("true")

        
        
    #for c in cleanedArray:
       # print(re.findall(pattern, str(c))) 
    #    print(r.replace(".", " ").rstrip())
        #for x in range(len(cleanedArray)):
        # indeX = x
        # indeY = x + 1
        # fS = re.findall(pattern, str(cleanedArray[indeY]))
        # for f in fS:
         #   print(cleanedArray[r].index(f))
            #if ( cleanedArray[(cleanedArray.index(f))] or cleanedArray[(cleanedArray.index(f)) + 1] or cleanedArray[(cleanedArray.index(f)) -1] ).isdigit():
            #    print("true")

