import re

with open('chars1.txt', 'r') as f1:
   row = f1.readlines()

   #numText = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
   numDic ={
     "one" : "1",
     "two" : "2",
     "three" : "3",
     "four" : "4",
     "five" : "5",
     "six" : "6",
     "seven" : "7",
     "eight" : "8",
     "nine" : "9",
   }
   pattern = re.compile("one|two|three|four|five|six|seven|eight|nine")
   newRow = []
   #temp = []
   #for r in range(len(row)):
   #    var1 = re.findall(pattern, row[r])
   #    if len(var1) > 0:
   #            for v in var1:
   #                row[r] = re.sub(v, numDic[v], row[r])
   #                temp.append(row[r])
   #            newRow.append(row[r])
   #    elif len(var1) == 0:
   #        newRow.append(row[r])
   #print(temp)
   #for r in row:
   #   v1 = re.findall(pattern, r)
   #   if len(v1) > 0:
   #    for x in range(len(v1)):
   #       r = r.replace(str(v1[x]),str(numDic[v1[x]]))
   #    newRow.append(r)
   #   else:
   #    newRow.append(r)
   #row = f.readlines()
 # map = {
 #   "one" : 1,
 #   "two": 2,
 #   "three" : 3,
 #   "four" : 4,
 #   "five" : 5,
 #   "six" : 6,
 #   "seven" : 7,
 #   "eight" : 8,
 #   "nine" : 9,
  #}
  #pattern = re.compile("one|two|three|four|five|six|seven|eight|nine")
  #tA = []

   for r in row:
    v1 = re.findall(pattern, r)
    print(v1)
    for x in range(len(v1)):
      r = r.replace(str(v1[x]),str(numDic[v1[x]]))
    newRow.append(r.rstrip())

   nums = ["1", "2","3","4","5","6","7","8","9"]
   numArray = []
   total = 0
   for x in range(len(newRow)):
      tempArray = []
      for y in newRow[x]:
         y.encode('latin1').decode('cp1252')
         for n in nums:
            if y == n:
              tempArray.append(y)
      if len(tempArray) > 1:
            numArray.append(int(str(tempArray[0]) + str(tempArray[len(tempArray) - 1])))
      elif len(tempArray) == 1:
            numArray.append(int(str(tempArray[0]) + str(tempArray[0])))
   for p in numArray:
    #print(p)
    total += p
   print(total)
               
               