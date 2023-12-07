with open('chars.txt', 'r') as f1:
   row = f1.readlines()
   nums = ["1", "2","3","4","5","6","7","8","9"]
   numText = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
   numArray = []
   total = 0
   for x in range(1000):
      tempArray = []
      for y in row[x]:
         y.encode('latin1').decode('cp1252')
         for n in nums:
            if y == n:
               tempArray.append(y)


      if len(tempArray) > 1:
            numArray.append(int(str(tempArray[0]) + str(tempArray[len(tempArray) - 1])))
      elif len(tempArray) == 1:
            numArray.append(int(str(tempArray[0]) + str(tempArray[0])))
   for p in numArray:
    print(p)
    total += p
   print(total)
    