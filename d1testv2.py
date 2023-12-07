import re
with open("chars1.txt", 'r') as f:
  row = f.readlines()
  map = {
    "one" : 1,
    "two": 2,
    "three" : 3,
    "four" : 4,
    "five" : 5,
    "six" : 6,
    "seven" : 7,
    "eight" : 8,
    "nine" : 9,
  }
  pattern = re.compile("one|two|three|four|five|six|seven|eight|nine")
  tA = []

  t = 0
  for r in row:
    v1 = re.findall(pattern, r)
    for x in range(len(v1)):
      r = r.replace(str(v1[x]),str(map[v1[x]]))
    print(r)
    for l in r:
      fd = None
      ld = None
      if l.isdigit():
        ld = l
        if fd == None:
          fd = l
      print(fd)
      print(ld)
      #t += int(str(fd) + str(ld))
  #print(t)
      
        
    #tA.append(r.rstrip())
  
    
   #oA = []
  #for x in tA:
   # temp = []
   # for y in x:
   #   if y.isdigit():
   #     temp.append(y)
   # if len(temp) > 1:
   #    oA.append(int(str(temp[0]) + str(temp[-1])))
   # elif len(temp) == 1:
   #     oA.append(int(str(temp[0]) + str(temp[0])) )
  #print(oA)
  #print(sum(oA))

 # r=0
 # for v in tA:
 #   fd= None
 #   ld= None
 #   for w in v:
 #     if w.isdigit():
 #       ld = w
 #       if fd == None:
 #         fd = w
 #   r += int(str(fd) + str(ld))
 # print(r)

 # r = 0
 # for v in tA:
 #   fd = None
 #   ld = None
 #   for w in v:
 #     if w.isdigit():
 #       ld = w
 #       if fd == None:
 #         fd = w
 #   r += (int(str(fd) + str(ld)))
  #print(r)


