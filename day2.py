import re

#part1
with open('chars2.txt') as f: 
    row = f.readlines()
    map = {
        'red':12,
        'green':13,
       'blue':14,
    }
    pattern = re.compile("\d.green+|[0-5][0-9].green+|\d.blue+|[0-5][0-9].blue+|\d.red+|[0-5][0-9].red+|;")
    tA = []
    for r in row:
      tV = 0
      var1 = re.findall(pattern, r.strip().replace(";", " "))
      for v in var1:
         var2 =v.split()
         if int(var2[0]) <= map[var2[1]]:
            tV += 1
      if tV /len(var1) == 1:
     
         tA.append(int((r.split())[1].replace(":", " ")))
    print(sum(tA))

#part2
with open('chars2.txt') as f: 
    row = f.readlines()
    pG = re.compile("\d.green|[0-5][0-9].green")
    pB = re.compile("\d.blue|[0-5][0-9].blue")
    pR = re.compile("\d.red|[0-5][0-9].red")
    pattern = re.compile("\d.green|[0-5][0-9].green|\d.blue|[0-5][0-9].blue|\d.red|[0-5][0-9].red|;")
    tA = []
    t = 0
    for r in row:
      tV = 0
      var1 = re.findall(pattern, r.strip().replace(";", " "))
      vG = re.findall(pG, str(var1))
      gA =[]
      for vg in vG:
         vg1 = vg.split()
         if len(vg1) > 0:
          gA.append(int(vg1[0]))
      vB = re.findall(pB, str(var1))
      bA =[]
      for vb in vB:
         vb1 = vb.split()
         if len(vb1) > 0:
          bA.append(int(vb1[0]))
      vR = re.findall(pR, str(var1))
      rA =[]
      for vr in vR:
         vr1 = vr.split()
         if len(vr1) > 0:
          rA.append(int(vr1[0]))
     
      t += (max(bA) * max(gA) * max(rA))
    print(t)
  
      
     





     

    
    

